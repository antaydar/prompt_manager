import pandas as pd
import sqlite3

def import_csv_to_sqlite(db_file, csv_file, table_name):
    # Create a database connection
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Import the data into the SQLite table
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    database = 'ndeca.db'  

    # Define your CSV files and corresponding table names
    csv_files_and_tables = {
        '../data/advertising.csv': 'advertising_de_april',
        '../data/categories.csv': 'categories',
        '../data/collections.csv': 'collections',
        '../data/inventory.csv': 'inventory',
        '../data/processed_orders.csv': 'orders',
        '../data/products.csv': 'products'
    }

    # Import each CSV file into the corresponding SQL table
    for csv_file, table_name in csv_files_and_tables.items():
        import_csv_to_sqlite(database, csv_file, table_name)
