from orator import DatabaseManager


# Comment
conFig = {
    'postgres': {
        'driver': 'postgres',
        'host': 'localhost',
        'database': 'db_name',
        'user': 'db_user',
        'password': 'db_password',
        'prefix': '',
        'port': 5432,
    }
}

db = DatabaseManager(conFig)
