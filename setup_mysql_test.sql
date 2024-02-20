-- prepares a MySQL server for the project (test)
-- create database hbnb_test_db for testing purpose
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create new user hbnb_test (in localhost)
CREATE USER IF NOT EXISTS 'hbnb_test' @'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- grant hbnb_test all privileges on hbnb_test_db database
GRANT SELECT ON performance_schema.* TO 'hbnb_test' @'localhost';

-- grant hbnb_test SELECT privilege on performance_schema database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
