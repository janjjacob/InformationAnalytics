-- SQL examples using world, scratch, and album databases

-- 01 Selecting Rows

USE world;
SELECT 'Hello, World';
SELECT 1 + 2;
SELECT * FROM Country;
SELECT * FROM Country ORDER BY Name;
SELECT Name, LifeExpectancy FROM Country ORDER BY Name;
SELECT Name, LifeExpectancy AS "Life Expectancy" FROM Country ORDER BY Name;
SELECT COUNT(*) FROM Country;
SELECT * FROM Country ORDER BY Name LIMIT 5;


-- 02 Selecting Columns

USE world;
SELECT * FROM Country ORDER BY Code;
SELECT Name, Code, Region, Population FROM Country ORDER BY Code;
SELECT Name AS Country, Code AS ISO, Region, Population AS Pop FROM Country ORDER BY Code;


-- 03 Counting Rows

USE world;
SELECT COUNT(*) FROM Country;
SELECT COUNT(*) FROM Country WHERE Population > 1000000;
SELECT COUNT(*) FROM Country WHERE Population > 100000000;
SELECT COUNT(*) FROM Country WHERE Population > 100000000 AND Continent = 'Europe' ;
SELECT COUNT(*) FROM Country;
SELECT COUNT(LifeExpectancy) FROM Country;


-- 04 Joining queries

USE album;
SELECT * FROM album;
SELECT * FROM track;

SELECT a.artist AS Artist, a.title AS Album, t.track_number AS 'Track Num',
    t.title AS Track, t.duration AS Seconds
  FROM album AS a
  JOIN track AS t ON a.id = t.album_id
  ORDER BY a.artist, a.title, t.track_number;


-- 05 Finding databases, tables, and columns

USE scratch;
SHOW databases;
SHOW tables;
DESCRIBE item;


-- 06 Using operators

USE world;
SELECT Name AS 'Country', ROUND(Population / 1000000) AS 'PopMM' 
  FROM Country 
  WHERE Population > 50000000 AND Continent IN ('Asia', 'Europe')
  ORDER BY Population DESC;

SELECT t.title AS 'Track', t.track_number AS 'Track No', a.title AS 'Album', 
    a.artist AS 'Artist', t.duration AS 'Seconds'
  FROM album AS a
  JOIN track AS t ON t.album_id = a.id
  WHERE t.duration > 120 AND t.track_number > 3
  ORDER BY t.duration DESC;


-- 07 string comparisons

USE world;
SELECT Name FROM Country WHERE Name LIKE '_a%' ORDER BY Name;
SELECT Name FROM Country WHERE STRCMP(Name, 'France') <= 0 ORDER BY Name;


-- 08 regular expressions

USE world;
SELECT Name FROM Country WHERE Name RLIKE 'y$' ORDER BY Name;
SELECT Name FROM Country WHERE Name RLIKE '[xz][ai]' ORDER BY Name;


-- 09 string concatenation

SELECT CONCAT('This ', 'and ', 'that');
SELECT CONCAT('Love', ' ', 'is', ' ', 'all', ' ', 'you', ' ', 'need');
SELECT CONCAT('one', 'two');
SELECT CONCAT('string', 42);
SELECT CONCAT(42, 42);



