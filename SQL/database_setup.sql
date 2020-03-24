CREATE DATABASE internships;

USE internships;

CREATE TABLE jobs
    (
    id INT unsigned NOT NULL AUTO_INCREMENT,
    position VARCHAR(255),
    company VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    listing_date DATE,
    app_link VARCHAR(255),
    url VARCHAR(255),
    tags VARCHAR(255),
    PRIMARY KEY (id)
    );