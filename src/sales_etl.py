import sqlite3
import pandas as pd 

def read_csv_files(region_a_path,region_b_path):
    # Read Region A data
    df_region_a = pd.read_excel(region_a_path)
    df_region_a['region'] = 'A'
    df_region_a['amount'] = df_region_a['PromotionDiscount'].apply(extract_amount)
    df_region_a = df_region_a.drop(columns=['PromotionDiscount'])

    # Read Region B data
    df_region_b = pd.read_excel(region_b_path)
    df_region_b['region'] = 'b'
    df_region_b['amount'] = df_region_b['PromotionDiscount'].apply(extract_amount)
    df_region_b = df_region_b.drop(columns=['PromotionDiscount'])

    return df_region_a , df_region_b

def transform_data(df_region_a, df_region_b):
    # Combine datasets
    combined_df = pd.concat(df_region_a,df_region_b)
    
    # Add required columns and apply transformations
    combined_df["total_sales"] =  combined_df["QuantityOrdered"] * df["ItemPrice"] 
    combined_df["net_sale"] = combined_df["total_sales"] - combined_df["PromotionDiscount"] 
    transform_df = combined_df.drop_duplicates(["OrderId"])
    transform_df  = transform_df[transform_df["net_sale"] >0]
    
    return transform_df

def load_to_sqlite(df, db_path="sales_data.db"):
    # Convert to Pandas for SQLite loading
    pandas_df = df.toPandas()
    
    conn = sqlite3.connect(db_path)
    pandas_df.to_sql("sales_data", conn, if_exists="replace", index=False)
    conn.close()

def main():
    
    region_a_path = '/Users/vedprakash/Desktop/sales_analysis/input/order_region_a.xlsx'
    region_b_path = '/Users/vedprakash/Desktop/sales_analysis/input/order_region_b.xlsx'

    # Extract
    df_region_a, df_region_b = read_csv_files(region_a_path,region_b_path)
    
    # Transform
    transformed_df = transform_data(df_region_a, df_region_b)
    
    # Load
    load_to_sqlite(transformed_df)


if __name__=='__main__':
    main()

