-- Bug count: ? (find them all)
-- Topic: INNER JOIN, LEFT JOIN, self JOIN, multi-table JOIN
-- Give after: L05
--
-- Scenario: An HR system for a small company.
-- Run the setup first, then fix and run each query.
--
-- Expected results are shown as comments above each query.

-- === SETUP ===
DROP TABLE IF EXISTS order_items, orders, customers, departments, employees CASCADE;

CREATE TABLE departments (
    id   SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE employees (
    id            SERIAL PRIMARY KEY,
    name          VARCHAR(100) NOT NULL,
    department_id INTEGER REFERENCES departments(id),
    manager_id    INTEGER REFERENCES employees(id),
    salary        NUMERIC(12,2) NOT NULL
);

CREATE TABLE customers (
    id    SERIAL PRIMARY KEY,
    name  VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL
);

CREATE TABLE orders (
    id          SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    amount      NUMERIC(12,2) NOT NULL,
    status      VARCHAR(20) DEFAULT 'pending'
);

INSERT INTO departments (name) VALUES ('Engineering'), ('Marketing'), ('Sales');
INSERT INTO employees (name, department_id, manager_id, salary) VALUES
('Kamol',   1, NULL,  25000000),
('Aziz',    1, 1,     15000000),
('Gulnora', 2, 1,     12000000),
('Jasur',   1, 2,      8000000),
('Malika',  3, 3,      9500000),
('Bobur',   3, 3,      7800000);

INSERT INTO customers (name, email) VALUES
('Sardor', 'sardor@mail.com'),
('Nilufar', 'nilufar@mail.com'),
('Zarina', 'zarina@mail.com');

INSERT INTO orders (customer_id, amount, status) VALUES
(1, 850000, 'completed'),
(1, 450000, 'pending'),
(2, 1200000, 'completed'),
(NULL, 300000, 'pending');   -- orphan order with no customer

-- === QUERIES ===

-- Query 1: Show every employee with their department name
-- Expected: all 6 employees with their department
SELECT e.name, d.name AS department
FROM employees e
JOIN departments d ON e.id = d.department_id;  -- BUG: wrong join direction

-- Query 2: Show all customers AND their orders (include customers with no orders)
-- Expected: Sardor (2 orders), Nilufar (1 order), Zarina (0 orders → NULLs)
SELECT c.name, o.id AS order_id, o.amount, o.status
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.id  -- BUG: tables are swapped for this requirement
ORDER BY c.name;

-- Query 3: Find customers who have NEVER placed an order
-- Expected: Zarina
SELECT c.name, c.email
FROM customers c
INNER JOIN orders o ON c.id = o.customer_id  -- BUG: wrong join type
WHERE o.id IS NULL;

-- Query 4: Show each employee with their manager's name
-- Expected: Kamol → (no manager), Aziz → Kamol, Gulnora → Kamol, etc.
SELECT
    e.name     AS employee,
    m.name     AS manager
FROM employees e
JOIN employees m ON e.id = m.manager_id  -- BUG: join condition is backwards
ORDER BY manager NULLS LAST;

-- Query 5: Show all orders with customer name — include the orphan order (no customer)
-- Expected: 4 rows, the NULL-customer order shows NULL for customer name
SELECT c.name AS customer, o.amount, o.status
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id;  -- BUG: wrong table on left side for this requirement

