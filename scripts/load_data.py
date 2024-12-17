import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file and return its head, column names, and row count.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        tuple: A tuple containing the DataFrame, its head, column names, and row count.
               Returns None if an error occurs.
    """
    
    data = pd.read_csv(file_path)
    data = data.loc[:, ~data.columns.str.contains('^Unnamed')]

    data = data.head()
    columns = data.columns.tolist()
    row_count = data.shape[0] 
    
    return {
        'data': data,
        'column_names': columns,
        'row_count': row_count
    }