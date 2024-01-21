-- This script creates the database hbtn_0d_2 and the user user_0d_2 and grants select privilege

-- Creating the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Creating user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
FLUSH PRIVILEGES;

-- Granting permissions to user_0d_2 for the database hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;