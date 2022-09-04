from .query_builder import QueryBuilder
from config.database import config


class Model:
    __table_name__ = None
    connection = None
    primary_key = 'id'
    fillable = []

    def __init__(self, *args, **kwargs):
        super(Model, self).__init__(*args, **kwargs)


    @classmethod
    def get_table_name(cls):
        if cls.__table_name__ is not None:
            return cls.__table_name__
        else:
            return cls.__name__.lower() + 's'

    @classmethod
    def where(cls, *args):
        qb = QueryBuilder(cls)
        qb.where(list(args))
        return qb

    @classmethod
    def or_where(cls, *args):
        qb = QueryBuilder(cls)
        qb.or_where(list(args))
        return qb

    @classmethod
    def find(cls, id):
        qb = QueryBuilder(cls)
        res = qb.find(id)
        del qb
        return res

    def save(self):
        if hasattr(self, self.primary_key) and getattr(self, self.primary_key) is not None:
            pass
            # update
        else:
            pass
            # insert


