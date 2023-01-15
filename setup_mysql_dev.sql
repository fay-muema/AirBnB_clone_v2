--creating database
--granting priviledes

CREATE DATABASE IF NOT EXISTS hbnb_test_db
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
USE hbnb_dev_db;
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
