![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![GitLab](https://img.shields.io/badge/gitlab-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white)

***

### Introducing

This is an application that inserts/select/updates/deletes data in the database (PostgreSQL) using sqlalchemy and flask
rest framework.
***
### Instalation

    Clone with SSH: git@github.com:ValeriyFromUA/Students_DB_with_Flask_and_postgres_SQL.git
    Clone with HTTP: https://github.com/ValeriyFromUA/Students_Db.git

Main used libraries in Pipfile nad Pipfile.lock that stored in `compose/` with Dockerfiles

***

### Usage

Chose config in ```configuration.py``` and add it in ```app_run.py```

```
# example
APP = create_app(DevelopmentConfig)
```

then Run ```create_db_with_data.py``` to create DB and ```app_run.py``` to start server
<hr />

***

### Usage with Docker

Run a docker-compose file

```docker-compose up```

Run the file that creates the database

```create_db_with_data.py```

#### Flasgger

     http://localhost:5000/apidocs/

***

### Details for use

#### Returning students list or student by id when using optional argument

     http://localhost:5000/api/v1/students?student_id=5

#### Returning list of courses

     http://localhost:5000/api/v1/courses

#### Returning groups list or group with a maximum of "X" members when using optional argument

     http://localhost:5000/api/v1/groups?students_count=15

***

## Technology

    - Python 3.10
    - Flask
    - SQLAlchemy
    - PostgreSQL
    - Docker
    - Pytest
    - Swagger

## Project author:

#### https://www.linkedin.com/in/valeriy-vasilenko/

#### https://github.com/ValeriyFromUA

***
