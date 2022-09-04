from config.database import config
from typing import Union


class QueryBuilder:
    __query_type__ = 'select'
    __columns__ = []
    __conditions = []
    __rendered = set()
    __query_args__ = {}

    def __init__(self, model):
        self.model = model
        connection_name = model.connection if model.connection is not None else config['default']
        driver = config[connection_name]['driver']
        mod = __import__(f'laraton.db.{driver}', fromlist=['Connector'])
        connector_class = getattr(mod, 'Connector')
        self.driver_connection = connector_class(config[connection_name])
        pass

    def find(self, id):
        sql = f"select * from  {self.model.get_table_name()} where {self.model.primary_key} = :id"
        res = self.driver_connection.execute(sql, {'id': id})
        return self.convert_to_obj(self.model, res.fetchone())

    def all(self):
        res = self.driver_connection.execute(f"select * from  {self.model.get_table_name()}")
        lst = []
        if res is not None:
            for row in res.fetchall():
                lst.append(self.convert_to_obj(self.model, row))
        return lst

    def select(self, columns: Union[str, list]):
        self.__query_type__ = 'select'
        if isinstance(columns, str):
            self.__columns__.append(columns)
        else:
            self.__columns__ = columns
        return self

    def where(self, args):
        if isinstance(args[0], list):
            for condition in args:
                self.__add_condition_string('where', condition)
        else:
            self.__add_condition_string('where', args)
        return self

    def or_where(self, *args):
        if isinstance(args, tuple) and (isinstance(args[0], tuple) or isinstance(args[0], list)):
            args = args[0]

        if isinstance(args[0], list):
            for condition in args:
                self.__add_condition_string('or', condition)
        else:
            self.__add_condition_string('or', args)

        return self

    def get(self):
        sql = self.__generate_query()
        res = self.driver_connection.execute(sql, self.__query_args__)
        lst = []
        if res is not None:
            for row in res.fetchall():
                lst.append(self.convert_to_obj(self.model, row))
        return lst

    def first(self):
        sql = self.__generate_query() + ' limit 1'
        res = self.driver_connection.execute(sql, self.__query_args__)

        return self.convert_to_obj(self.model, res.fetchone())


    def __add_condition_string(self, operator: str, condition_lst: list):
        init = operator
        if operator.lower() == 'where':
            if len(self.__conditions) > 0:
                operator = 'and where'
        elif operator.lower() == 'or':
            if len(self.__conditions) == 0:
                operator = 'where'

        if len(condition_lst) == 2:
            arg_name = 'Arg' + str(len(self.__query_args__) + 1)
            if f'{init} {condition_lst[0]} =:{condition_lst[1]}' not in self.__rendered:
                self.__conditions.append(f'{operator} {condition_lst[0]} =:{arg_name}')
                self.__query_args__[arg_name] = condition_lst[1]
                self.__rendered.add(f'{init} {condition_lst[0]} =:{condition_lst[1]}')
        elif len(condition_lst) == 3:
            if f'{init} {condition_lst[0]} {condition_lst[1]}:{condition_lst[2]}' not in self.__rendered:
                arg_name = 'Arg' + str(len(self.__query_args__) + 1)
                self.__conditions.append(f'{operator} {condition_lst[0]} {condition_lst[1]}:{arg_name}')
                self.__query_args__[arg_name] = condition_lst[2]
                self.__rendered.add(f'{init} {condition_lst[0]} {condition_lst[1]}:{condition_lst[2]}')

    def __generate_query(self):
        fields = '*' if len(self.__columns__) == 0 else ','.join(self.__columns__)
        table_name = self.model.get_table_name()
        conditions = ' '.join(self.__conditions)
        self.__conditions = []
        return f"select {fields} from {table_name} {conditions}"


    def convert_to_obj(self, model_class, res):
        if res is not None:
            model = model_class()
            for key in res:
                setattr(model, key, res[key])
            return model
        return None
