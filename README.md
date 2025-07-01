### Pre-requisites: 
- Python 3.10+
- poetry
- docker
- docker-compose
- postgres instance in the docker

### How to run:
- ```poetry shell``` to activate the virtual environment
- ```poetry install``` or ```poetry install --no-root``` to install the dependencies
- Create a .env file
- Specify the below fields in the `.env` file. Sample values are provided
  - DB_HOST=localhost
  - DB_PORT=5433
  - DB_USERNAME=db-username
  - DB_PASSWORD=db-password
  - DB_NAME=db-name
#### N.B.: These values will be used in the docker-compose.yml file to create a postgres db instance. Thus, provide good values.

[//]: # (#### N.B.: )
- Run the db: ```docker-compose -up --build -d```
- Run the app: ```uvicorn infrastructure.main:app --reload```

