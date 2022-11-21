import string
import random
import psycopg2

def insertUser():
    n = 12
    res = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k=n))

    query = """insert into UserTable(user_fullname,username, password, phone_number,address,email)
    values(""" + f"'{res}'" + """,""" + f"'{res}'" + """,'jATVnvd@59','01812456967','Road-346,House-4,Flat-B2,Gulshan-2','sar@gmail.com');
    """

    # print(query)

    try:
        connection = psycopg2.connect(user="postgres",
                                password="postgres",
                                host="192.168.50.200",
                                port="5432",
                                database="test_trigger_db")
        
        # for i in range(1, 1000000):
        #     cursor = connection.cursor()
        #     cursor.execute(query)
        #     connection.commit()
        #     print(i)
        #     cursor.close()


        cursor = connection.cursor()
        # print ( connection.get_dsn_parameters())  

        cursor.execute(query)

        connection.commit()
        cursor.close()
        # count = cursor.rowcount
        # print(count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")



if __name__ == '__main__':
    insertUser()



