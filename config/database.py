import os
config = {
    'default': 'sqlite',
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': os.getenv('DB_NAME', 'laraton'),
        'user': os.getenv('DB_NAME', 'root'),
        'password': os.getenv('DB_NAME', 'root'),
        'prefix': ''
    },
    "sqlite": {
        'driver': 'sqlite',
        "dbname": os.getenv('DB_NAME', 'test.db')
    }
}
