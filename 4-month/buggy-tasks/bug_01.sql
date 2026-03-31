-- Bug count: ? (find them all)
-- Topic: SELECT, WHERE, ORDER BY, LIMIT, LIKE, NULL handling
-- Give after: L05
--
-- Scenario: A product manager queries an electronics store database.
-- Run this entire file in psql to set up and test.
--
-- Expected results are shown as comments above each query.

-- === SETUP ===
DROP TABLE IF EXISTS products;
CREATE TABLE products (
    id        SERIAL PRIMARY KEY,
    name      VARCHAR(200) NOT NULL,
    category  VARCHAR(50)  NOT NULL,
    brand     VARCHAR(100),
    price     NUMERIC(12,2) NOT NULL,
    stock     INTEGER DEFAULT 0,
    rating    NUMERIC(3,2)
);

INSERT INTO products (name, category, brand, price, stock, rating) VALUES
('Laptop HP 15',     'Laptop',    'HP',      4500000, 8,  4.2),
('iPhone 15',        'Phone',     'Apple',   8200000, 3,  4.8),
('Samsung Galaxy',   'Phone',     'Samsung', 3800000, 12, 4.1),
('iPad Pro',         'Tablet',    'Apple',   5900000, 5,  4.6),
('USB Hub',          'Accessory', NULL,       85000,  50, 3.9),
('Wireless Mouse',   'Accessory', 'Logitech', 95000, 30, NULL),
('MacBook Pro',      'Laptop',    'Apple',  11800000, 2,  4.9),
('AirPods Pro',      'Accessory', 'Apple',   1450000, 15, 4.7);

-- === QUERIES (each has at least one bug) ===

-- Query 1: Show name and price for all Laptops, cheapest first
-- Expected: Laptop HP 15 (4,500,000), MacBook Pro (11,800,000)
SELECT name, price
FROM products
WHERE category = 'laptop'  -- BUG
ORDER BY price ASC;

-- Query 2: Show all products where brand is unknown (not set)
-- Expected: USB Hub
SELECT name, brand
FROM products
WHERE brand = NULL;  -- BUG

-- Query 3: Show top 3 most expensive products
-- Expected: MacBook Pro, iPhone 15, iPad Pro
SELECT name, price
FROM products
ORDER BY price  -- BUG
LIMIT 3;

-- Query 4: Find all Apple products with rating above 4.5
-- Expected: iPhone 15, iPad Pro, MacBook Pro, AirPods Pro
SELECT name, brand, rating
FROM products
WHERE brand = 'Apple' AND rating > 4.5
ORDER BY rating;  -- BUG — should be DESC to show highest rated first

-- Query 5: Show product name and a stock_status label using CASE WHEN
-- Expected: stock=0 → 'Out of Stock', 1-5 → 'Low', 6+ → 'Available'
SELECT
    name,
    stock,
    CASE
        WHEN stock = 0 THEN 'Out of Stock'
        WHEN stock < 5 THEN 'Low'   -- BUG: boundary — stock=5 should be 'Low' not 'Available'
        ELSE 'Available'
    END AS stock_status
FROM products
ORDER BY stock;

-- Query 6: Search for products whose name contains 'pro' (case-insensitive)
-- Expected: iPad Pro, MacBook Pro, AirPods Pro
SELECT name, category, price
FROM products
WHERE name LIKE '%pro%';  -- BUG

