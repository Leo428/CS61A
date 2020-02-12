.read fa19data.sql

CREATE TABLE obedience AS
  SELECT seven, instructor FROM students;

CREATE TABLE smallest_int AS
  SELECT time, smallest FROM students WHERE smallest > 2 ORDER BY smallest ASC LIMIT 20;

CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color from students as a, students as b where a.time < b.time and a.pet = b.pet and a.song = b.song;

