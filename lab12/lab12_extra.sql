.read lab12.sql

CREATE TABLE smallest_int_having AS
  SELECT time, smallest FROM students GROUP BY smallest HAVING COUNT(smallest) = 1;

CREATE TABLE fa19favpets AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


CREATE TABLE fa19dog AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


CREATE TABLE obedienceimages AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
