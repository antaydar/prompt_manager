import sqlite3
import pandas as pd

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """Create a table from the create_table_sql statement."""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def main():
    database = "ndeca.db"

    # SQL statements for table creation
 
    sql_create_orders_table = """
    CREATE TABLE IF NOT EXISTS orders (
        unique_id INTEGER PRIMARY KEY,
        order_id TEXT NOT NULL,
        purchase_date TEXT,
        sku TEXT,
        collection TEXT,
        category TEXT,
        quantity INTEGER,
        currency TEXT,
        item_price REAL,
        item_tax REAL,
        shipping_price REAL,
        shipping_tax REAL,
        ship_country TEXT,
        sales_channel TEXT
    );
    """

    sql_create_inventory_table = """
    CREATE TABLE IF NOT EXISTS inventory (
        inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
        sku TEXT,
        collection TEXT,
        category TEXT,
        inventory_count INTEGER,
        date TEXT,
        supply_days INTEGER
    );
    """

    sql_create_advertising_table = """
    CREATE TABLE IF NOT EXISTS advertising_de_april (
        state TEXT,
        campaign_name TEXT,
        collection TEXT,
        category TEXT,
        status TEXT, 
        targeting TEXT,
        budget REAL,
        cost_type TEXT,
        impressions INTEGER,
        clicks INTEGER,
        ctr REAL, 
        spend REAL,
        cpc REAL,
        orders INTEGER,
        sales REAL,
        acos REAL,
        roas REAL
    );
    """

    
    # Create a database connection
    conn = create_connection(database)

    # Create tables
    if conn is not None:
        create_table(conn, sql_create_orders_table)
        create_table(conn, sql_create_inventory_table)
        create_table(conn, sql_create_advertising_table)

        conn.close()
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
