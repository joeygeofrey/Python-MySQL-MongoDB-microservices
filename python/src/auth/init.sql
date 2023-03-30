CREATE USER 'auth_admin'@'localhost' IDENTIFIED BY 'Adminpass123';

CREATE DATABASE auth;

GRANT ALL PRIVILEGES ON auth.* TO 'auth_user'@'localhost';

USE auth;

CREATE TABLE user (
    id INT NOT AUTO_INCRIMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO user (email, password) VALUES ('joey@geofrey.com', 'Pass123')