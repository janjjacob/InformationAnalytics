-- In-class 5A ZAGI

-- The database is named “neu_student_xpl_zagi”.
-- It is structured according to the ER diagram and schema shown in the PDF file.
-- You should run the following command and then proceed with the remaining exercises.

USE neu_student_xpl_zagi;

-- Write and execute a query to list all the items from the product table (all columns)
-- and order the results by productname in descending order.

SELECT * FROM product ORDER BY productname DESC;

-- Save your results as a CSV file named “product.csv”.


-- Write and execute a query that selects only productname from the product table
-- when categoryID is FW, assigning productname the alias “Product Name”,
-- and ordering the results by productname (in ascending order).

SELECT productname AS "Product Name" FROM product
WHERE categoryid = "FW"
ORDER BY productname;

-- Copy and paste the results of the query below (including column header).

-- Product Name
-- Action Sandal
-- Cosy Sock
-- Dura Boot
-- Easy Boot
-- Simple Sandal

-- Write and execute a query that produces a list of both categoryname and productname
-- only when the categoryname value is Electronics.
-- Change productname to the alias “Product Name” and categoryname to “Category Name”.

SELECT categoryname AS "Category Name", productname AS "Product Name"
FROM category join product
ON category.categoryid = product.categoryid
WHERE category.categoryname = "Electronics";

-- Copy and paste the results of the query (including column headers).

-- Category Name	Product Name
-- Electronics	Sunny Charger
-- Electronics	Electra Compass
-- Electronics	Mega Camera
-- Electronics	Hi-Tec GPS

-- Display the partial contents of three tables (seek further guidance).

SELECT category.categoryname AS "Category Name", product.productname AS "Product Name", vendor.vendorname as "Vendor Name"
FROM category, product, vendor
WHERE category.categoryid = product.categoryid AND product.vendorid = vendor.vendorid AND
category.categoryname = "Electronics";

-- Copy and paste the results of the query (including column headers).

-- Category Name	Product Name	Vendor Name
-- Electronics	Sunny Charger	Outdoor Adventures
-- Electronics	Electra Compass	Mountain King
-- Electronics	Mega Camera	Wilderness Limited
-- Electronics	Hi-Tec GPS	Outdoor Adventures

-- When you are finished, disconnect MySQL Workbench from the server (exit the program through File/Exit). Upload your completed SQL file and the products.csv file.
