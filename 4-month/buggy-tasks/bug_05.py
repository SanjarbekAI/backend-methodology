# Bug count: ? (find them all)
# Topic: psycopg2 transactions, error handling, rollback, RETURNING
# Give after: L09
#
# Scenario: An order placement system that must atomically:
#   1. Check stock
#   2. Insert the order
#   3. Reduce product stock
#   4. Commit — or rollback everything on failure
#
# Expected output (success case):
#   Stock before: 10
#   Order #<id> placed. New stock: 8
#
# Expected output (insufficient stock):
#   Error: not enough stock (requested 50, available 10)
#   Stock unchanged: 10
#
# Expected output (invalid product):
#   Error: product 9999 not found
#   Stock unchanged: 10

import psycopg2
import psycopg2.extras
import os
from dotenv import load_dotenv

load_dotenv()

def get_conn():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

def setup(conn):
    with conn.cursor() as cur:
        cur.execute("DROP TABLE IF EXISTS demo_orders, demo_products CASCADE")
        cur.execute("""
            CREATE TABLE demo_products (
                id    SERIAL PRIMARY KEY,
                name  VARCHAR(100) NOT NULL,
                stock INTEGER NOT NULL CHECK (stock >= 0)
            )
        """)
        cur.execute("""
            CREATE TABLE demo_orders (
                id         SERIAL PRIMARY KEY,
                product_id INTEGER REFERENCES demo_products(id),
                quantity   INTEGER NOT NULL
            )
        """)
        cur.execute("INSERT INTO demo_products (name, stock) VALUES ('Laptop', 10) RETURNING id")
        product_id = cur.fetchone()[0]
    conn.commit()
    return product_id

def place_order(conn, product_id: int, quantity: int):
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            # Step 1: check stock
            cur.execute("SELECT stock FROM demo_products WHERE id = %s", (product_id))  # BUG
            row = cur.fetchone()

            if row is None:
                raise ValueError(f"product {product_id} not found")

            if row["stock"] < quantity:
                raise ValueError(
                    f"not enough stock (requested {quantity}, available {row['stock']})"
                )

            # Step 2: insert order
            cur.execute(
                "INSERT INTO demo_orders (product_id, quantity) VALUES (%s, %s) RETURNING id",
                (product_id, quantity)
            )
            order_id = cur.fetchone()["id"]

            # Step 3: reduce stock
            cur.execute(
                "UPDATE demo_products SET stock = stock - %s WHERE id = %s RETURNING stock",
                (product_id, quantity)  # BUG — arguments are in the wrong order
            )
            new_stock = cur.fetchone()["stock"]

        conn.commit()  # BUG — commit is outside the with block but inside try — is this correct? think carefully
        return order_id, new_stock

    except Exception as e:
        conn.rollback()
        raise


conn = get_conn()
product_id = setup(conn)

# Test 1: successful order
print(f"Stock before: 10")
try:
    order_id, new_stock = place_order(conn, product_id, 2)
    print(f"Order #{order_id} placed. New stock: {new_stock}")
except ValueError as e:
    print(f"Error: {e}")
    with conn.cursor() as cur:
        cur.execute("SELECT stock FROM demo_products WHERE id = %s", (product_id,))
        print(f"Stock unchanged: {cur.fetchone()[0]}")

# Test 2: insufficient stock
try:
    place_order(conn, product_id, 50)
except ValueError as e:
    print(f"Error: {e}")
    with conn.cursor() as cur:
        cur.execute("SELECT stock FROM demo_products WHERE id = %s", (product_id,))
        print(f"Stock unchanged: {cur.fetchone()[0]}")

# Test 3: invalid product
try:
    place_order(conn, 9999, 1)
except ValueError as e:
    print(f"Error: {e}")
    with conn.cursor() as cur:
        cur.execute("SELECT stock FROM demo_products WHERE id = %s", (product_id,))
        print(f"Stock unchanged: {cur.fetchone()[0]}")

conn.close()

