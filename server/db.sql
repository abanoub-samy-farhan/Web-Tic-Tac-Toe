-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS TicTacToe;
CREATE USER IF NOT EXISTS 'root'@'localhost' IDENTIFIED BY 'rootroot';
GRANT ALL PRIVILEGES ON `TicTacToe`.* TO 'root'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
