"""
This module is responsible for connecting to the database
"""
from typing import List

import psycopg2

from app.config.database import database_config
from sqlalchemy.orm import sessionmaker
import sqlalchemy
import databases


class Database:
    """
    Class responsible for connecting to the database
    """

    def __init__(self):
        self.connection = None
        self.database = databases.Database(database_config.url)
        self.metadata = sqlalchemy.MetaData()
        self.engine = sqlalchemy.create_engine(database_config.url)
        self.SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=self.engine)

    @property
    def get_connection(self) -> psycopg2.extensions.connection:
        """
        get_connection: returns the connection to the database
        """
        return self.connection
    
    def open_connection(self) -> None:
        self.connection = psycopg2.connect(
            host=database_config.host,
            user=database_config.user,
            password=database_config.password,
            database=database_config.database,
            port=database_config.port,
        )

    def close_connection(self) -> None:
        self.connection.close()

    @property
    def get_cursor(self) -> psycopg2.extensions.cursor:
        return self.connection.cursor()

    def query(self, query) -> List[tuple]:
        """
        query: executes a query in the database
        params: query: str

        return List[tuple]
        """
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        data = cursor.fetchall()
        cursor.close()
        return data
    
database = Database()
