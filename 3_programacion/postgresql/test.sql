CREATE DATABASE your_database;

USE your_database;

CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50),
  email VARCHAR(50),
  password VARCHAR(50)
);

INSERT INTO users (name, email, password) VALUES
  ('Alice', 'alice@example.com', 'password123'),
  ('Bob', 'bob@example.com', 'password456'); 
