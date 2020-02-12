.read data.sql

-- QUESTIONS --



-------------------------------------------------------------------------
------------------------ Give Interest- ---------------------------------
-------------------------------------------------------------------------

UPDATE accounts SET amount = amount * 1.02;


create table give_interest_result as select * from accounts; -- just for tests

CREATE TABLE temp AS
  SELECT name || "'s Checking account" AS name, amount / 2 as amount FROM accounts UNION
  SELECT name || "'s Savings account"         , amount / 2           FROM accounts;

DELETE FROM accounts;
INSERT INTO accounts SELECT * FROM temp;


create table split_account_results as select * from accounts; -- just for tests

-------------------------------------------------------------------------
-------------------------------- Whoops ---------------------------------
-------------------------------------------------------------------------

DROP TABLE accounts;


CREATE TABLE average_prices AS
  SELECT category AS category, AVG(MSRP) AS average_price FROM products GROUP BY category;

CREATE TABLE lowest_prices AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

CREATE TABLE shopping_list AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

CREATE TABLE total_bandwidth AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
