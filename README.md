# expenses
Setup to try/learn about alembic for db modification and using AWS DBs

# usage
before first use you need to modify the config.py file for your server information

first activate your virtual environment (if using)
`venv\Scripts\Activate.ps1` (Windows) or `source venv\scripts\activate` (Linux)
then
`flask run`

# development steps
1. setup an AWS db instance
    1. a development db called expenses_dev
    1. a production db called expenses_prod
    1. Needed to setup AWS Security to allow connection
1. Configure the MySQL DB
    1. Use MySQL Workbench to do this configuration
1. setup an SQLAlchemy to connect to the AWS DB
    1. define the expenses model
    1. ~MySQL-python package required for the mysql client~
        1. ~This requires MS C++ Build Tools~
    1. Use mysqlclient package instead of MySQL-python
1. setup alembic to create the DDL for the database

