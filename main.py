from flask import Flask, request, jsonify
import sqlite3
import logging
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
def setup_logging():
    """
    Sets up logging for the application. 
    Creates a 'logs' directory if it does not exist, 
    and configures logging to write to 'app.log'.
    """
    # Create a logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Define the log file path
    log_file = os.path.join('logs', 'app.log')

    # Configure logging settings
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s %(levelname)s:%(message)s'
    )
    logging.info('Logging is set up.')

# Call the setup_logging function to configure logging
setup_logging()

# Function to connect to the SQLite database
def get_db_connection():
    """
    Establishes a connection to the SQLite database.

    Returns:
        sqlite3.Connection: A connection object to the database.

    Raises:
        sqlite3.Error: If there is an error connecting to the database.
    """
    try:
        conn = sqlite3.connect('well_production.db')  # Connect to the database file
        conn.row_factory = sqlite3.Row  # Enable row access by column name
        return conn
    except sqlite3.Error as e:
        logging.error("Database connection error: %s", e)
        raise  # Raise the error for further handling

# Define the API endpoint for retrieving annual production data
@app.route('/data', methods=['GET'])
def get_annual_data():
    """
    API endpoint to retrieve annual production data for a specific well.

    Query Parameters:
        well (str): The API WELL NUMBER for which to retrieve data.

    Returns:
        jsonify: A JSON response containing the oil, gas, and brine production values 
                  or an error message if something goes wrong.

    HTTP Status Codes:
        200: Success with data returned.
        400: Bad request if the well number is missing.
        404: Not found if the well number is not found in the database.
        500: Internal server error for database query issues or unexpected errors.
    """
    try:
        well_number = request.args.get('well')  # Get the 'well' parameter from the query string
        if not well_number:
            return jsonify({"error": "Missing well number"}), 400  # Return error if well number is not provided

        # Connect to the database and retrieve the data
        conn = get_db_connection()
        
        # Use double quotes around the column name to handle spaces
        query = 'SELECT "OIL", "GAS", "BRINE" FROM annual_production WHERE "API WELL NUMBER" = ?'
        cursor = conn.execute(query, (well_number,))
        row = cursor.fetchone()  # Fetch a single row from the result
        conn.close()  # Close the database connection

        if row is None:
            return jsonify({"error": "Well number not found"}), 404  # Return error if well number is not found

        # Return the data in JSON format
        return jsonify({
            "oil": row['OIL'],
            "gas": row['GAS'],
            "brine": row['BRINE']
        })

    except sqlite3.Error as e:
        logging.error("Database query error: %s", e)
        return jsonify({"error": "Database query error"}), 500  # Return error for database query issues
    except Exception as e:
        logging.error("Unexpected error: %s", e)
        return jsonify({"error": "An unexpected error occurred"}), 500  # Return error for unexpected issues

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)  # Start the application with debugging enabled
