from abc import abstractmethod
import os
import typing

from app import BASE_DIRECTORY


class SqlUriBase():
    @abstractmethod
    def getSqlUri(void) -> str:
        pass

class SqlLiteUri(SqlUriBase):
    def __init__(self,base_directory=None):
        from . import BASE_DIRECTORY
        self.base_directory = base_directory if base_directory is not None else BASE_DIRECTORY

    def getSqlUri(self) -> str:
        return f'sqlite:///{self.base_directory}/app.db'

class MySqlUri(SqlUriBase):
    def __init__(self):
        self.user = os.environ.get('SQL_USER','APP')
        self.server = os.environ.get('SQL_SERVER','192.168.1.1')
        self.key = os.environ.get('SQL_KEY','ajflkj2389Fjkj48')
        self.db = os.environ.get('SQL_DB','expenses-dev')
    def getSqlUri(self) -> str:
        return f'mysql+mysqldb://{self.user}:{self.key}@{self.server}/{self.db}'

sqlite_uri = SqlLiteUri()
mysql_uri = MySqlUri()

class ConfigBase:
    NAME='Base'
    DEBUG=False
    TESTING=False
    SQLALCHEMY_DATABASE_URI=sqlite_uri.getSqlUri()

class ConfigTesting(ConfigBase):
    NAME='Testing'

class ConfigDevelopment(ConfigBase):
    NAME='Development'
    DEBUG=True
    TESTING=True
    SQLALCHEMY_DATABASE_URI=mysql_uri.getSqlUri()

class ConfigProduction(ConfigDevelopment):
    NAME="Production"
    DEBUG=False
    TESTING=False

environments = [
    ConfigTesting(), ConfigDevelopment(), ConfigProduction()
]

config_by_name = { cfg.NAME : cfg for cfg in environments }