-- More SQL examples using world, scratch, and album databases

-- Using operators

USE world;
SELECT Name AS 'Country', ROUND(Population / 1000000) AS 'Pop (Million)' 
  FROM Country 
  WHERE Population > 40000000 AND Continent IN ('Asia', 'Europe')
  ORDER BY Name;

USE album;
SELECT t.title AS 'Track', t.track_number AS 'Track No', a.title AS 'Album', 
    a.artist AS 'Artist', t.duration AS 'Seconds'
  FROM album AS a
  JOIN track AS t ON t.album_id = a.id
  WHERE t.duration > 110 AND t.track_number > 2
  ORDER BY t.track_number;


-- string comparisons

USE world;
SELECT Name FROM Country WHERE Name LIKE 'a_g%' ORDER BY Name;
SELECT Name FROM Country WHERE STRCMP(Name, 'Barundi') <= 0 ORDER BY Name;


-- regular expressions

USE world;
SELECT Name FROM Country WHERE Name RLIKE '^g' ORDER BY Name;
SELECT Name FROM Country WHERE Name RLIKE '[xz][a-c]' ORDER BY Name;




