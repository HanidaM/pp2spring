import psycopg2
from config import params

config = psycopg2.connect(**params)
current = config.cursor()

create_table = '''
    CREATE TABLE PhoneBook(
        name VARCHAR(255) ,
        number VARCHAR(255) UNIQUE
    );
'''

current.execute(create_table)

current.close()
config.commit()
config.close()