-- creates the database hbtn_0d_2 and the user user_0d_2
-- user_0d_2 should have the SELECT priviledge
-- password should be set to user_0d_2_pwd
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
USE hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd_@Jsu';
GRANT SELECT ON hbth_0d_2.* TO 'user_0d_2'@'localhost';
