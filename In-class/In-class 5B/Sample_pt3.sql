-- Sample SQL Part 3

-- trimming and padding

USE scratch;
SELECT * FROM customer;
SELECT * FROM customer WHERE name LIKE '  Bill Smith  ';
SELECT * FROM customer WHERE name LIKE TRIM('  Bill Smith  ');
SELECT CONCAT(':', RTRIM('  Bill Smith  '), ':');
SELECT CONCAT(':', LTRIM('  Bill Smith  '), ':');

SELECT CONCAT(':', TRIM('x' FROM 'xxxBill Smithxxx'), ':');

SELECT LPAD('Price', 20, '.');
SELECT LPAD('Price', 20, '. ');
SELECT RPAD('Price', 20, '. ');

-- case conversion

USE scratch;
SELECT UPPER(name) FROM customer;
SELECT LOWER(name) FROM customer;
SELECT CONCAT(UPPER(SUBSTRING(name, 1, 1)),LOWER(SUBSTRING(name, 2))) FROM customer;

USE world;
SELECT DISTINCT Region FROM Country ORDER BY Region;

SELECT Continent, COUNT(Name) FROM Country
GROUP BY Continent
ORDER BY Continent;


