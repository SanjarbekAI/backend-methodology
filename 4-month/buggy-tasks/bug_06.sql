-- Bug count: ? (find them all)
-- Topic: DDL, constraints, indexes, UPDATE/DELETE, EXPLAIN ANALYZE
-- Give after: L09
--
-- Scenario: A developer is setting up a production database schema for
--           a delivery company. The schema has several design mistakes
--           that will cause data integrity problems or poor performance.
--
-- Your task: find and fix every bug. Some bugs crash immediately.
--            Some are silent design errors that will cause problems later.
--            Read the comments carefully.

-- === TABLE DEFINITIONS (contains DDL bugs) ===

DROP TABLE IF EXISTS deliveries, drivers, vehicles CASCADE;

CREATE TABLE vehicles (
    id           SERIAL PRIMARY KEY,
    plate_number VARCHAR(20),          -- BUG: should be UNIQUE NOT NULL
    model        VARCHAR(100) NOT NULL,
    capacity_kg  NUMERIC(8,2)
);

CREATE TABLE drivers (
    id         SERIAL PRIMARY KEY,
    name       VARCHAR(100) NOT NULL,
    license_no VARCHAR(30) NOT NULL,
    phone      VARCHAR(20),
    vehicle_id INTEGER REFERENCES vehicles(id) ON DELETE CASCADE  -- BUG: wrong cascade behavior
                                                                   -- deleting a vehicle should not delete the driver
);

CREATE TABLE deliveries (
    id          SERIAL PRIMARY KEY,
    driver_id   INTEGER REFERENCES drivers(id),
    pickup_city VARCHAR(50),
    dest_city   VARCHAR(50),
    weight_kg   NUMERIC(8,2) CHECK (weight_kg > 0),
    price       NUMERIC(12,2),
    status      VARCHAR(20) DEFAULT 'pending',
    created_at  TIMESTAMPTZ DEFAULT NOW()
);

-- BUG: missing CHECK constraint on deliveries.status
-- It should only allow: 'pending', 'in_transit', 'delivered', 'cancelled'

-- BUG: missing index on deliveries.driver_id (this column is used in every JOIN query)
-- BUG: missing index on deliveries.status (this column is used in every WHERE filter)

-- === DATA SETUP ===
INSERT INTO vehicles (plate_number, model, capacity_kg) VALUES
('01A123BC', 'Ford Transit', 1500),
('01A123BC', 'Mercedes Sprinter', 2000);  -- BUG: duplicate plate — should fail but won't without constraint

INSERT INTO drivers (name, license_no, phone, vehicle_id) VALUES
('Sardor', 'UZB-001', '+998901111111', 1),
('Nilufar', 'UZB-002', '+998902222222', 2);

INSERT INTO deliveries (driver_id, pickup_city, dest_city, weight_kg, price, status) VALUES
(1, 'Tashkent', 'Samarkand', 250, 450000, 'pending'),
(2, 'Bukhara',  'Namangan',  180, 380000, 'in_transit'),
(1, 'Tashkent', 'Fergana',   320, 520000, 'delivered');

-- === DML BUGS ===

-- Bug: Update without WHERE — sets ALL deliveries to 'delivered'
UPDATE deliveries SET status = 'delivered';  -- BUG: missing WHERE clause

-- Bug: Wrong argument order in UPDATE
UPDATE deliveries
SET driver_id = 1
WHERE id = 2;  -- this is actually fine — but the one below is not:

UPDATE deliveries
SET weight_kg = -50           -- BUG: violates CHECK but only if constraint exists
WHERE id = 1;

-- Bug: DELETE that should use soft-delete instead
DELETE FROM drivers WHERE id = 1;
-- BUG: this will fail or cascade — explain why, and change it to a soft-delete approach
-- (add an is_active BOOLEAN DEFAULT TRUE column and set it to FALSE instead)

-- === VERIFY ===
-- After fixing all bugs, these queries should work correctly:
SELECT d.name, v.plate_number, v.model
FROM drivers d
JOIN vehicles v ON d.vehicle_id = v.id;

SELECT dr.name AS driver, de.dest_city, de.status
FROM deliveries de
JOIN drivers dr ON de.driver_id = dr.id
ORDER BY de.created_at DESC;

