#!usr/bin/python3

import os
from sqlalchemy import create_engine

class DBStorage:
    """The engine for storing data in a database"""

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://'
                                      f"{os.get_env('BNB_MYSQL_USER')}:"
                                      f"{os.get_env('HBNB_MYSQL_PWD')}"
                                      f"@{'os.get_env(HBNB_MYSQL_HOST)'}:3306/"
                                      f"{os.get_env(HBNB_MYSQL_DB)}, "
                                      "pool_pre_ping=True")
        if os.get_env('HBNB_ENV') == 'test':
            drop_all(self.__engine)
