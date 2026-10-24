use retail_sales;
-- 1. Total sales 
select round(sum(Sales),2) as Total_Sales from sales;
-- ROUND(..., 2) displays the result to two decimal places.

-- 2. Total profit  
select round(sum(Profit),2) as Total_Profit from sales;


-- 3. Total orders  
select count(distinct `Order ID`) as Total_Orders from sales;


-- 4. Total customers  
select count(distinct `Customer ID`) as Total_Customers from sales;


-- 5. Average order value  
select round (sum(sales) / count(distinct `Order ID`),2) 
 as Average_Order_Value from sales;
 
SELECT ROUND(AVG(Sales), 2) AS Average_Sales
FROM sales;


-- 6. Sales by category  
select Category, round(sum(Sales),2) as Total_Sales from sales 
 group by Category order by Total_Sales DESC;
 
 
 -- 7. Sales by region  
 select Region, round(sum(Sales),2) as Total_Sales from sales
 group by Region order by Total_Sales DESC;
 
 
 
 -- 8. Profit by category  
SELECT Category,ROUND(SUM(Profit), 2) AS Total_Profit
FROM sales
GROUP BY Category
ORDER BY Total_Profit DESC;



-- 9. Profit by region  
select Region, round(sum(Profit),2) as Total_Profit
from sales
group by Region
order by Total_Profit DESC;


-- 10. Sales by month
SELECT Month, Month_Name,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM sales
GROUP BY Month, Month_Name
ORDER BY Month;

-- Customer 11. Top 10 customers  
select `Customer ID`, `Customer Name`, round(sum(Sales),2) 
as Total_Sales from sales group by `Customer ID`, `Customer Name` 
order by Total_Sales DESC limit 10;
-- 12. Repeat customers 
select `Customer ID`, `Customer Name`, count(distinct `Order ID`) as Total_Orders 
from sales group by `Customer ID`, `Customer Name` having count(
distinct `Order ID`)>1 order by Total_Orders DESC;

-- Query 13: Average Customer Spending
select round(AVG(Customer_Sales),2) as Average_Customer
from(select `Customer ID`,sum(sales) as Customer_Sales from sales
    GROUP BY `Customer ID`
) AS Customer_Summary;



-- Query 14: Top 10 Products by Sales
select `Product ID`, `Product Name`, round(sum(sales),2) as Total_Sales
from sales group by `Product ID`, `Product Name` order by Total_Sales DESC limit 10;



---  Query 15: Bottom Products by Sales
select `Product ID`, `Product Name`, round(sum(sales),2) as Total_Sales
from sales group by `Product ID`, `Product Name` order by Total_Sales ASC limit 10;

-- Query 16: Most Profitable Products
select `Product ID`, `Product Name`, round(sum(Profit),2) as Total_Profit
from sales GROUP BY `Product ID`, `Product Name`
ORDER BY Total_Profit DESC
LIMIT 10;

-- Query 17: Customer Ranking by Sales
WITH Customer_Summary AS ( SELECT `Customer ID`, `Customer Name`,SUM(Sales) AS Total_Sales
FROM sales GROUP BY `Customer ID`, `Customer Name`
)
SELECT `Customer ID`, `Customer Name`, ROUND(Total_Sales, 2) AS Total_Sales,
    RANK() OVER (ORDER BY Total_Sales DESC) AS Customer_Rank
FROM Customer_Summary ORDER BY Customer_Rank
LIMIT 10;
-- CTE (WITH) creates a temporary named result called Customer_Summary.
-- SUM(Sales) calculates each customer's total sales.
-- RANK() ranks customers from highest to lowest sales.
-- OVER (ORDER BY Total_Sales DESC) assigns rank 1 to the customer with the highest sales.
-- LIMIT 10 displays the top 10 ranked customers

-- Query 18: Product Ranking by Sales
WITH Product_Summary AS (
    SELECT `Product ID`, `Product Name`,
	SUM(Sales) AS Total_Sales FROM sales GROUP BY `Product ID`, `Product Name`
) SELECT `Product ID`, `Product Name`, ROUND(Total_Sales, 2) AS Total_Sales,
    RANK() OVER (ORDER BY Total_Sales DESC) AS Product_Rank
FROM Product_Summary ORDER BY Product_Rank LIMIT 10;


-- Query 19: Monthly Sales Growth
WITH Monthly_Sales AS ( SELECT Year, Month, Month_Name, SUM(Sales) AS Total_Sales
    FROM sales GROUP BY Year, Month, Month_Name ),
Sales_Growth AS ( SELECT Year, Month, Month_Name, Total_Sales, LAG(Total_Sales) OVER (
	ORDER BY Year, Month ) AS Previous_Month_Sales FROM Monthly_Sales
) SELECT Year, Month_Name, ROUND(Total_Sales, 2) AS Total_Sales, ROUND(Previous_Month_Sales, 2) AS Previous_Month_Sales,
ROUND( (Total_Sales - Previous_Month_Sales) / NULLIF(Previous_Month_Sales, 0) * 100, 2
) AS Growth_Percentage FROM Sales_Growth
ORDER BY Year, Month;
-- Monthly_Sales calculates total sales for each month and year.
-- LAG() retrieves the previous month's sales.
-- NULLIF() prevents division by zero.
-- Growth_Percentage calculates the percentage change from the previous month.
-- ORDER BY Year, Month displays the months chronologically.

-- Query 20: Category Ranking by Sales
WITH Category_Summary AS (
    SELECT Category, SUM(Sales) AS Total_Sales FROM sales
    GROUP BY Category
) SELECT Category, ROUND(Total_Sales, 2) AS Total_Sales,
    RANK() OVER (
        ORDER BY Total_Sales DESC
    ) AS Category_Rank
FROM Category_Summary
ORDER BY Category_Rank;

-- WITH (CTE): Creates a temporary result named Category_Summary.
-- SUM(Sales): Calculates total sales for each category.
-- RANK(): Assigns a rank based on total sales.
-- DESC: Places the category with the highest sales first.
-- ROUND(): Displays sales rounded to two decimal places.


