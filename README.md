# AMP-Back 
The api where is connected our application to get data and manipulate them. 

# intialisation
## env variables
First, you have to set en variables inside the .env file. You have to add value for these variables:
```
API_V1_STR=""
PROJECT_NAME=""
SQLALCHEMY_DATABASE_URI=""
```
## pip dependencies
There are some package needed to start our app, to retreive these package you just need to execute this command at the root directory :
```
pipenv install
```
# Start the app
To start the app, you can use the script start.sh
or just execute the commande from this script
```
uvicorn app.main:app --reload
```