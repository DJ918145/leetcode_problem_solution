# Write your MySQL query statement below
Select Sales.year, Sales.price, Product.product_name From Sales Left Join Product on Sales.product_id = Product.product_id;