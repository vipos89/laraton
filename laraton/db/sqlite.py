import sqlite3
import os
from .abstarct_connector import AbstractConnector
from config.database import config


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class Connector(AbstractConnector):

    def connect(self, config: dict):
        self.connection = sqlite3.connect(os.path.join(os.getenv('APP_PATH'), config['dbname']))
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()
        pass

    def execute(self, query, par_={}):
        res = self.cursor.execute(query, par_)
        self.connection.commit()
        return res
