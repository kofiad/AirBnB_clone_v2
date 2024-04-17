CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;
CREATE USER IF NOT EXISTS `hbnb_dev`@`localhost` IDENTIFIED BY `hbnb_dev_pwd`;
GRANT All PRIVILEGES ON `hbnb_dev_db` TO `hbnb_dev`@`localhost` IDENTIFIED BY `hbnb_dev_pwd`;
GRANT SELECT PRIVILEGES ON `performance_schema ` TO `hbnb_dev`@`localhost` IDENTIFIED BY `hbnb_dev_pwd`;
FLUSH PRIVILEGES;
