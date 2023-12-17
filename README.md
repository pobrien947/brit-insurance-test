# Brit Insurance - Python Test

## Prerequisites
```
Python >= 3.10
Node
npm
```

## Build the python virtual environment
In a project directory run the following to setup the python 
environment for the backend FastAPI application
```
pip install virtualenv
python -m venv brit-venv
source brit-venv/bin/activate
export PYTHONPATH=$PWD
pip install -r requirements.txt
```

## Clone the Application code
```
git clone 
```

## Build the database
The following database set is designed for a MySQL engine.
Any relational engine could be used but some ammendment may be required in schema.sql and dato.sql
```
cd ./database
```
login to the mysql client and enter the following
```
mysql -u[db-user] -p[db-password]
source schema.sql
source data.sql
```

## Set environment variables
The following environment variables are required by the backend application to connect to the databse
```
export DB_HOST=localhost:3306
export DB_USER=[db user]
export DB_PASS=[password]
export DB_NAME=brit_insurance
```

## Set the Backend to run
Enter the following commands to set the backend api app running
The api is set to liston on port 8000 
```
cd ./backend
python main.py
```

## API Endpoints and example requests
With the backend app running the swagger docs can be accessed at
(<b>TODO:</b> Needs more work params not showing up)
```
http://localhost:8000/docs
```

### Login
```
curl -X POST http://localhost:8000/auth/login -d \
    '{"username": "demouser", "password": "demopassword"}' \
    -H 'Content-Type: application/json'
```

### Create New User (Sign Up)
```
curl -X POST http://localhost:8000/auth/signup -d \
    '{"username": "newdemouser", "password": "newdemopassword"}' \
    -H 'Content-Type: application/json'
```

### Get Basket
```
curl -X GET http://localhost:8000/basket/ \
    -H 'Content-Type: application/json' \
    -H 'auth-token: 0c4a2ef7-8f60-4ca3-88be-f2894a441b96' 
```

### Submit basket and get the Summary
```
curl -X POST http://localhost:8000/basket/summary -d \
    '[{"item_name": "Apples", "item_price": 10}, {"item_name": "Book", "item_price": 150}, {"item_name": "Car", "item_price": 15000}]' \
    -H 'Content-Type: application/json' \
    -H 'auth-token: 0c4a2ef7-8f60-4ca3-88be-f2894a441b96' 
```

## Frontend
The frontend is intended to be a React app, however this requires more work.

```
cd ./frontend
npm run start

http://localhost:3000/
```
