-- Bug count: ? (find them all)
-- Topic: GROUP BY, HAVING, aggregate functions, subqueries, CTEs
-- Give after: L09
--
-- Scenario: A sales analytics team runs monthly reports on their store database.
-- Run the setup first, then fix each query.
--
-- Expected results shown as comments above each query.

-- === SETUP ===
DROP TABLE IF EXISTS order_items, orders, customers, products CASCADE;

CREATE TABLE customers (
    id   SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    city VARCHAR(50)
);
CREATE TABLE products (
    id       SERIAL PRIMARY KEY,
    name     VARCHAR(200) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price    NUMERIC(12,2) NOT NULL
);
CREATE TABLE orders (
    id          SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    status      VARCHAR(20) DEFAULT 'pending',
    created_at  TIMESTAMPTZ DEFAULT NOW()
);
CREATE TABLE order_items (
    id         SERIAL PRIMARY KEY,
    order_id   INTEGER REFERENCES orders(id),
    product_id INTEGER REFERENCES products(id),
    quantity   INTEGER NOT NULL
);

INSERT INTO customers VALUES (1,'Sardor','Tashkent'),(2,'Nilufar','Samarkand'),(3,'Aziz','Tashkent'),(4,'Malika','Bukhara');
INSERT INTO products VALUES (1,'Laptop','Electronics',4500000),(2,'Phone','Electronics',3200000),(3,'Keyboard','Accessory',350000),(4,'Mouse','Accessory',180000),(5,'Monitor','Electronics',1800000);
INSERT INTO orders VALUES (1,1,'completed',NOW()),(2,1,'completed',NOW()),(3,2,'completed',NOW()),(4,3,'pending',NOW()),(5,4,'cancelled',NOW());
INSERT INTO order_items VALUES (1,1,1,1),(2,1,3,2),(3,2,2,1),(4,3,1,1),(5,3,5,2),(6,4,4,3),(7,5,2,1);

-- === QUERIES ===

-- Query 1: Count of orders per status
-- Expected: completed → 3, pending → 1, cancelled → 1
SELECT status, COUNT(id) AS order_count  -- BUG: COUNT(id) excludes NULLs but the real issue is elsewhere
FROM orders
GROUP BY order_count;  -- BUG

-- Query 2: Total revenue per customer (completed orders only)
-- JOIN order_items and products to compute quantity * price
-- Expected: Sardor → 8,350,000 | Nilufar → 8,100,000
SELECT
    c.name,
    SUM(oi.quantity * p.price) AS total_revenue
FROM customers c
JOIN orders o     ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p   ON oi.product_id = p.id
WHERE o.status = 'completed'
GROUP BY c.name, c.id
HAVING total_revenue > 0  -- BUG: cannot reference alias in HAVING
ORDER BY total_revenue DESC;

-- Query 3: Categories with more than 1 product
-- Expected: Electronics (3), Accessory (2)
SELECT category, COUNT(*) AS product_count
FROM products
GROUP BY category
WHERE product_count > 1;  -- BUG: WHERE cannot filter aggregates

-- Query 4: Customers who spent more than the average customer spending
-- Expected: shows customers above the average
WITH customer_totals AS (
    SELECT
        c.id,
        c.name,
        SUM(oi.quantity * p.price) AS total_spent
    FROM customers c
    JOIN orders o      ON c.id = o.customer_id
    JOIN order_items oi ON oi.order_id = o.id
    JOIN products p    ON p.id = oi.product_id
    WHERE o.status = 'completed'
    GROUP BY c.id, c.name
)
SELECT name, total_spent
FROM customer_totals
WHERE total_spent > AVG(total_spent)  -- BUG: aggregate not allowed in WHERE outside of subquery
ORDER BY total_spent DESC;

-- Query 5: Products that have never been ordered
-- Expected: (none in this dataset — but query must be structurally correct)
SELECT p.name, p.category
FROM products p
JOIN order_items oi ON p.id = oi.product_id  -- BUG: wrong join type for "never ordered"
WHERE oi.id IS NULL;

