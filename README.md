# annual_production_task
annual_production_task

2. Add up the quarterly data to calculate the annual data for  oil, gas, and brine for each well based on API WELL NUMBER. For example, API WELL NUMBER 34059242540000 has a quarter 1 production of 103, quarter 2 production of 166, quarter 3 production of 50, and quarter 4 production of 62, therefore it would have an annual oil production of 381 because 103 + 166 + 50 + 62 = 381.

3. Using python, load the calculated annual data into a local sqlite database.

## The solution of these two problems are in the file named as "annual_data.py". You can just run the file by "python annual_data.py"

4. Make an api using flask on port 8080 to allow for getting the annual data from the database using a GET request.

For example if the input url is:

http://localhost:8080/data?well=34059242540000 

then the api should return

{
	"oil": 381
	"gas": 108074
	"brine": 939
}


5. The app should be launch-able by running:

python main.py

## The solution of this is in the file named as  "main.py". You can start the flask server by running "python main.py".
## Once the flask app is up and running, you can use postman to test the API by using this example url

http://localhost:8080/data?well=34059242540000 
then the api returns
{
	"oil": 381
	"gas": 108074
	"brine": 939
}

## You can also test the api by running the "test.py" file in a differnent terminal by using "python test.py", you should get
Test Case 1: Missing well number - Passed
Test Case 2: Invalid well number - Passed
Test Case 3: Valid well number - Passed
Data: {'brine': 939, 'gas': 108074, 'oil': 381}
## these prints in the terminal
## Keep in mind that the flask app should by running the whole time

N.B: Exception handeling and error logging in an add-on to this task
