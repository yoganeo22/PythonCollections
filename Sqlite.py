import sqlite3
import pandas as pd

# you could use sqlitestudio to open the db

def createConnection(fileName):
    '''
        Create database connection to sqlite database
        If the file does not exist, it will create the new database
    :param filename: db filename
    :return: None
    '''
    try:
        conn = sqlite3.connect(fileName)
        print("Sqlite3 version: {}".format(sqlite3.version))
        # Sqlite3 version: 2.6.0
    except Error as e:
        print("Err: {}".format(e))
    finally:
        if conn:
            # always close connection after usage.
            conn.close()

def create_table(fileName, table, column1, type1, column2, type2):
    '''
        Create Table if not Exist
    :param fileName: db filename
    :param table: db table
    :param column1: column name
    :param type1: column format
    :param column2: column name
    :param type2: column format
    :return: None
    '''
    try:
        conn = sqlite3.connect(fileName)
        c = conn.cursor()
        c.execute('''
                  CREATE TABLE IF NOT EXISTS ''' + table + ''' 
                  ([''' + column1 + '''] '''+ type1 + ''' PRIMARY KEY, [''' + column2 + '''] ''' + type2 + ''')
                  ''')
        conn.commit()

    except Error as e:
        print("Err: {}".format(e))
    finally:
        if conn:
            # always close connection after usage.
            conn.close()

def insert_data(fileName, table, column1, column2, data):
    '''
        Insert data into table
    :param fileName: db filename
    :param table: db table
    :param table2: db table
    :param data: data to insert
    :return: None
    '''
    try:
        conn = sqlite3.connect(fileName)
        c = conn.cursor()
        c.execute('''
                  INSERT INTO ''' + table + ''' (''' + column1 + ''', ''' + column2 +''')
                    VALUES '''
                    + data + '''
                  ''')
        conn.commit()

    except Error as e:
        print("Err: {}".format(e))
    finally:
        if conn:
            # always close connection after usage.
            conn.close()

def display_data(fileName, table):
    '''
        Display data using Pandas
        Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
            built on top of the Python programming language.
    :param fileName: db filename
    :param table: db table
    :return: None
    '''
    try:
        conn = sqlite3.connect(fileName)
        c = conn.cursor()
        c.execute('''
                  SELECT
                  a.product_name,
                  b.price
                  FROM ''' + table + ''' a
                  LEFT JOIN prices b ON a.product_id = b.product_id
                  ''')
        df = pd.DataFrame(c.fetchall(), columns=['product_name', 'price'])
        print(df)
    except Error as e:
        print("Err: {}".format(e))
    finally:
        if conn:
            # always close connection after usage.
            conn.close()

def drop_table(fileName, table):
    '''
        Drop sqlite table
    :param fileName: db filename
    :param table: db table
    :return: None
    '''
    try:
        conn = sqlite3.connect(fileName)
        c = conn.cursor()
        c.execute('''
                  DROP table ''' + table + '''
                  ''')
    except Error as e:
        print("Err: {}".format(e))
    finally:
        if conn:
            # always close connection after usage.
            conn.close()


if __name__ == "__main__":
    print("Create and connect to Sqlite Database")

    # Create sqlite db with Two Tables as followings:
    #     Table 1:
    #     product_id (Primary)    product_name
    #     1                       Fruits
    #     2                       Vegetables
    #     Table 2:
    #     product_id (Primary)    price
    #     1                       1000
    #     2                       2000

    # dbfile is in the same directory as python file
    createConnection(r"sqlfile.db")

    # drop table
    drop_table(r"sqlfile.db", "Products")
    drop_table(r"sqlfile.db", "Prices")

    # create two tables
    create_table(r"sqlfile.db", "Products", "product_id", "INTEGER", "product_name", "TEXT")
    create_table(r"sqlfile.db", "Prices", "product_id", "INTEGER", "price", "INTEGER")

    # insert data
    data = ''' (1,'Fruits'),
               (2,'Vegetables')
           '''
    insert_data(r"sqlfile.db", "Products", "product_id", "product_name", data)

    data = ''' (1,1000),
               (2,2000)
           '''
    insert_data(r"sqlfile.db", "Prices", "product_id", "price", data)

    # display the results
    display_data(r"sqlfile.db", "Products")


# --- Output --- #
#  product_name  price
# 0       Fruits   1000
# 1   Vegetables   2000