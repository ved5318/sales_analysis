
def validate_data(spark, df):
    # Total records
    print(f"Total Records: {df.count()}")
    
    # Sales by region
    df.groupBy("region") \
      .sum("total_sales") \
      .show()
    
    # Average sales
    df.agg({"total_sales": "avg"}) \
      .show()
    
    # Duplicate check
    duplicates = df.groupBy("OrderId") \
                   .count() \
                   .filter(col("count") > 1)
    
    if duplicates.count() > 0:
        print("Warning: Duplicate OrderIds found!")
    else:
        print("No duplicates found.")