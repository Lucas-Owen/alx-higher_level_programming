-- Write a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
-- converts all of the following to UTF8:
-- Database hbtn_0c_0
-- Table first_table
-- Field name in first_table
ALTER DATABASE `hbtn_0c_0`
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE `hbtn_0c_0`;
ALTER TABLE `second_table`
MODIFY COLUMN `name` VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;