# annual_production_task
annual_production_task


# Flask Well Production API

This Flask application provides an API for retrieving annual production data for wells from an SQLite database. It allows users to query production values for oil, gas, and brine based on the well number.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Examples](#examples)
- [Logging](#logging)
- [Error Handling](#error-handling)
- [License](#license)

## Features

- Retrieve annual production data (oil, gas, and brine) for a specified well.
- Logging to a file for monitoring and debugging.
- Error handling for database connectivity and query issues.

## Technologies

- Flask: A lightweight WSGI web application framework in Python.
- SQLite: A self-contained, serverless SQL database engine.
- Python: The programming language used for building the application.
- Logging: For tracking application events.

## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd <repository_directory>
Install Dependencies:

Ensure you have Python installed, then install Flask:

bash
Copy code
pip install Flask
Create the SQLite Database:

Ensure that you have an SQLite database file named well_production.db in the project directory. This database should contain a table named annual_production with the following structure:

sql
Copy code
CREATE TABLE annual_production (
    "API WELL NUMBER" TEXT PRIMARY KEY,
    "OIL" REAL,
    "GAS" REAL,
    "BRINE" REAL
);
Run the Application:

Start the Flask application using the following command:

bash
Copy code
python app.py
The application will run on http://0.0.0.0:8080.

API Endpoints
GET /data
Retrieve annual production data for a specific well.

Query Parameters:
well (string): The API WELL NUMBER for which to retrieve data.
Example Request:
bash
Copy code
GET http://localhost:8080/data?well=12345
Example Response:
Success (200):

json
Copy code
{
    "oil": 5000,
    "gas": 3000,
    "brine": 1000
}
Error (400): Missing well number

json
Copy code
{
    "error": "Missing well number"
}
Error (404): Well number not found

json
Copy code
{
    "error": "Well number not found"
}
Error (500): Database query error

json
Copy code
{
    "error": "Database query error"
}
Logging
The application logs events to a file named app.log located in the logs directory. Ensure that the directory exists, or the application will create it. Log entries include timestamps and the severity level of each event.

Error Handling
The application includes error handling for the following scenarios:

Database connection issues: Logged as an error with a message.
Missing query parameters: Returns a 400 status code with an error message.
Well number not found: Returns a 404 status code with an error message.
Database query errors: Returns a 500 status code with an error message.
Unexpected errors: Returns a 500 status code with an error message.
License
This project is licensed under the MIT License - see the LICENSE file for details.

markdown
Copy code

### Key Sections:
1. **Features**: Highlights what the API can do.
2. **Technologies**: Lists the technologies used in the project.
3. **Setup Instructions**: Provides step-by-step instructions to run the application.
4. **API Endpoints**: Details the API endpoint, including query parameters and examples for requests and responses.
5. **Logging**: Explains how logging works in the application.
6. **Error Handling**: Describes the error handling mechanisms implemented.
7. **License**: Indicates the licensing terms for the project.

Feel free to adjust any sections or content based on your specific project requirements or
