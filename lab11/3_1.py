# Create procedure to insert many new users by list of name and phone. Use loop and if statement in stored procedure. 
# Check correctness of phone in procedure and return all incorrect data.
    
import psycopg2, re

conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    port= 5432,
    user = 'postgres',
    password = 'HB@uka2003'
)
cur = conn.cursor()

input_type = input()
pattern_1 = r"\+{1}\d+$"
pattern_2 = r"\d+$"
if input_type == "Terminal":
    name = input("Add name and number:\n")
    arr = list(map(str, input().split()))
    ok = True 
    if re.match(pattern_1,arr[1]) or re.match(pattern_2,arr[1]):
        pass
    else:
        print("Impossible phone number")
        ok = False
    try:
        insert_into = '''
        INSERT INTO PhoneBook VALUES (%s,%s);
        '''
        if ok:
            cur.execute(insert_into,(f'{arr[0]}',f'{arr[1]}'))
    except:
        print("phone number already written in the book")


cur.execute("select * from phonebook where number not like '+7%' and number not like '8%';")
not_cor_data = cur.fetchall()
print(not_cor_data)



cur.close()
conn.commit()
conn.close()