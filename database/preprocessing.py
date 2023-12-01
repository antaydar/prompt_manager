import pandas as pd

def preprocess_csv(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)

    # List of columns to process
    columns_to_process = ['item_price', 'item_tax', 'shipping_price', 'shipping_tax']

    # Replace comma with dot in the specified columns
    for column in columns_to_process:
        df[column] = df[column].astype(str).str.replace(',', '.')

    # Save the processed data to a new CSV file
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_csv = '../data/orders.csv'  
    output_csv = '../data/processed_orders.csv'  
    preprocess_csv(input_csv, output_csv)
