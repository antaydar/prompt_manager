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
    sql_create_categories_table = """ 
    CREATE TABLE IF NOT EXISTS categories (
        category TEXT NOT NULL,
        category_id INTEGER PRIMARY KEY
    );
    """

    sql_create_collections_table = """
    CREATE TABLE IF NOT EXISTS collections (
        collection TEXT NOT NULL,
        collection_id INTEGER PRIMARY KEY,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories (category_id)
    );
    """


    sql_create_products_table = """
    CREATE TABLE IF NOT EXISTS products (
        sku TEXT PRIMARY KEY,
        collection_id INTEGER,
        category_id INTEGER,
        FOREIGN KEY (collection_id) REFERENCES collections (collection_id),
        FOREIGN KEY (category_id) REFERENCES categories (category_id)
    );
    """


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
        collection_id INTEGER,
        category_id INTEGER,
        inventory_count INTEGER,
        month TEXT,
        FOREIGN KEY (sku) REFERENCES products (sku),
        FOREIGN KEY (collection_id) REFERENCES collections (collection_id),
        FOREIGN KEY (category_id) REFERENCES categories (category_id)
    );
    """

    sql_create_advertising_de_april_table = """
    CREATE TABLE IF NOT EXISTS advertising_de_april (
        state TEXT,
        campaign_name TEXT,
        collection_id INTEGER,
        category_id INTEGER,
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
        roas REAL,
        FOREIGN KEY (collection_id) REFERENCES collections (collection_id),
        FOREIGN KEY (category_id) REFERENCES categories (category_id)
    );
    """
    
    # Create a database connection
    conn = create_connection(database)

    # Create tables
    if conn is not None:
        create_table(conn, sql_create_categories_table)
        create_table(conn, sql_create_collections_table)
        create_table(conn, sql_create_products_table)
        create_table(conn, sql_create_orders_table)
        create_table(conn, sql_create_inventory_table)
        create_table(conn, sql_create_advertising_de_april_table)

        conn.close()
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
