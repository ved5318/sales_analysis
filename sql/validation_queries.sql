-- Count total records
SELECT COUNT(*) as total_records 
FROM sales_data;

-- Total sales by region
SELECT region, 
       SUM(total_sales) as total_sales_amount
FROM sales_data
GROUP BY region;

-- Average sales per transaction
SELECT AVG(total_sales) as avg_sales_per_transaction
FROM sales_data;

-- Check for duplicate OrderId
SELECT OrderId, COUNT(*) as count
FROM sales_data
GROUP BY OrderId
HAVING count > 1;