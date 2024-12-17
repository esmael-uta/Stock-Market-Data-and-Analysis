

import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file and return its head, column names, and row count.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        tuple: A tuple containing:
            - data_head (DataFrame): First 5 rows of the data.
            - columns (list): List of column names.
            - row_count (int): Total number of rows in the data.
    """
    try:
        # Load the data
        data = pd.read_csv(file_path)
        
        # Extract required information
        data_head = data.head()
        columns = data.columns.tolist()
        row_count = data.shape[0]
        
        return data_head, columns, row_count

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        