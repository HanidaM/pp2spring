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
delete_raw = '''
    DELETE FROM PhoneBook WHERE name = %s;
'''
current.execute(delete_raw,('Eer',))
current.close()
config.commit()
config.close()