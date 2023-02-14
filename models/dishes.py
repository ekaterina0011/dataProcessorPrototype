import psycopg2


def fib(dictionary):
# connection establishment
    conn = psycopg2.connect(
    database="postgres",
    user='postgres',
    password='postgres',
    host='localhost',
    port='5432'
    )

    conn.autocommit = True
    cursor = conn.cursor()

    #columns = dictionary.keys()
    #for i in dictionary.values():
    sql2 = f'''insert into task1.food(dish,description,ingredient,measurement) 
    VALUES('{dictionary['dish']}','{dictionary['description']}','{dictionary['ingredient']}'
    ,'{dictionary['measurement']}');'''

    cursor.execute(sql2)

    sql3 = '''select * from task1.food;'''
    cursor.execute(sql3)
    for i in cursor.fetchall():
        print(i)

    conn.commit()
    conn.close()