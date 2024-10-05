import requests

def test_api_endpoint(well_number):
    base_url = 'http://localhost:8080/data'

    # Test case 1: Missing well number
    response = requests.get(base_url)
    assert response.status_code == 400
    print("Test Case 1: Missing well number - Passed")

    # Test case 2: Invalid well number
    response = requests.get(base_url, params={'well': 'INVALID'})
    assert response.status_code == 404
    print("Test Case 2: Invalid well number - Passed")

    # Test case 3: Valid well number (using the parameter passed to the function)
    response = requests.get(base_url, params={'well': well_number})
    if response.status_code == 200:
        data = response.json()
        print("Test Case 3: Valid well number - Passed")
        print("Data:", data)
    else:
        print("Test Case 3: Valid well number - Failed, Status Code:", response.status_code)

test_api_endpoint(34059242540000)



# import pandas as pd
# import sqlite3

# # Replace 'your_file.xls' with the path to your Excel file
# df = pd.read_excel('20210309_2020_1.xls')

# df = df.rename(columns={'API WELL  NUMBER': 'API WELL NUMBER'})
# # Group by API WELL NUMBER and sum the OIL, GAS, BRINE values for each well (across all quarters)
# annual_data = df.groupby('API WELL NUMBER').agg({
#     'OIL': 'sum',
#     'GAS': 'sum',
#     'BRINE': 'sum'
# }).reset_index()

# # print(annual_data)
# # print(df.columns)

# # Connect to a local SQLite database (it will create the DB file if it doesn't exist)
# conn = sqlite3.connect('well_production.db')

# # Save the annual data into a table called 'annual_production'
# # If the table doesn't exist, it will be created automatically
# annual_data.to_sql('annual_production', conn, if_exists='replace', index=False)

# # Commit the transaction and close the connection
# conn.commit()
# conn.close()

# print("Annual production data has been successfully saved into the SQLite database.")



