import pandas as pd
import sqlite3

def load_and_process_data(excel_file, db_file):
    """
    Load production data from an Excel file, process it, and save the aggregated annual data to a SQLite database.

    Parameters:
    - excel_file (str): The path to the Excel file containing the well production data.
    - db_file (str): The path to the SQLite database file where the data will be saved.

    Returns:
    - None
    """
    try:
        #  Solution of Problem 1 Starts 

        # Load the Excel file into a DataFrame
        df = pd.read_excel(excel_file)
        print("Excel file loaded successfully.")

        # Rename the column for consistency
        df = df.rename(columns={'API WELL  NUMBER': 'API WELL NUMBER'})

        # Group by 'API WELL NUMBER' and sum the OIL, GAS, and BRINE values for each well
        annual_data = df.groupby('API WELL NUMBER').agg({
            'OIL': 'sum',
            'GAS': 'sum',
            'BRINE': 'sum'
        }).reset_index()

        print("Annual data aggregated successfully.")

        #  Solution of Problem 1 Ends 

        #  Solution of Problem 2 Starts 

        # Connect to the SQLite database
        conn = sqlite3.connect(db_file)
        print(f"Connected to the database '{db_file}'.")

        # Save the annual data into a table called 'annual_production'
        # If the table doesn't exist, it will be created automatically
        annual_data.to_sql('annual_production', conn, if_exists='replace', index=False)
        print("Annual production data has been saved into the SQLite database.")

        # Commit the transaction and close the connection
        conn.commit()
        conn.close()
        print("Database connection closed.")

        #  Solution of Problem 2 Ends 

    except FileNotFoundError:
        print(f"Error: The file '{excel_file}' was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The Excel file is empty.")
    except pd.errors.ParserError:
        print("Error: There was a problem parsing the Excel file.")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Replace 'your_file.xls' with the path to your Excel file
load_and_process_data('20210309_2020_1.xls', 'well_production.db')
