import psycopg2, re

conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'HB@uka2003'
)
cur = conn.cursor()

'''
do
$$
    declare
        student record;
    begin
        for student in select * from phonebook limit 4
            loop
                raise notice 'username = %, number = %', student.username, student.number;
            end loop;
    end
$$;
'''
cur.execute("select * from phonebook limit 4")
result = cur.fetchall()
print(result)