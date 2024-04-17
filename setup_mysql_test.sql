--prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS `hbnb_test`@`localhost` IDENTIFIED BY `hbnb_test_pwd`;
GRANT All PRIVILEGES ON hbnb_test_db TO `hbnb_dev`@`localhost`;
GRANT SELECT ON performance_schema TO `hbnb_dev`@`localhost`;
FLUSH PRIVILEGES;
