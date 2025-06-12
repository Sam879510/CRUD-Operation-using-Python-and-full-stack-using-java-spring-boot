-- SQL script to create database and table
CREATE DATABASE kals_inventory;

USE kals_inventory;

CREATE TABLE beer_inventory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    beer_name VARCHAR(100) NOT NULL,
    promo_item VARCHAR(100) NOT NULL,
    quantity INT NOT NULL DEFAULT 0
);

-- Sample data
INSERT INTO beer_inventory (beer_name, promo_item, quantity) VALUES
('KALS Premium Lager', 'Bottle Opener', 50),
('KALS IPA', 'Keychain', 30),
('KALS Stout', 'Pint Glass', 20),
('KALS Wheat Beer', 'Coaster Set', 40);