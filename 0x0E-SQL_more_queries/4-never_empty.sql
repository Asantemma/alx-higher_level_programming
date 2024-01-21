-- A script that creates the table id_not_null on your MySQL server.
-- Table has id default value of 1

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);