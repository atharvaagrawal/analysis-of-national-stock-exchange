import csv
import mysql.connector
import os.path
import pandas as pd
import easygui
from datetime import datetime
from mysql.connector import Error
from mysql.connector import errorcode

'''
This Script is for too Copy the Data of NiftyALL i.e the Bhavcopy Data to Nifty50Derived Table 
which contain only Top 50 Nifty Symbol.
'''
class Nifty50FromNiftyAll:
    def copyData(self):
        # DataBase Connection
        print("Hellos")
        try:
            connection = mysql.connector.connect(host='localhost', database='Nifty', user='root', password='[Enter Password]')
            cursor = connection.cursor()
            # to check repeated record
            qry = "Select *  from NiftyAll"
            pdata = pd.read_sql_query(qry, connection)
            
            if pdata.empty == True:
                easygui.msgbox("NiftyAll table is Empty", title="Process Message")
                if (connection.is_connected()):
                    cursor.close()
                    connection.close()
                return
            
            sql_select_Query = "Select *  from NiftyAll  where Symbol = (Select DISTINCT SYMBOL FROM NIFTY50 WHERE NIFTY50.SYMBOL = NIFTYALL.SYMBOL)  and Series='EQ'"
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            print(cursor)
            # Loop to store data
            for i in records:
                cursor.execute(""" INSERT INTO Nifty50Derived VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                               (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12]))

            connection.commit()
            easygui.msgbox("Data Already Present Record inserted successfully into Nifty50Derived table", title="Process Message")
        except mysql.connector.Error as error:
            connection.rollback()  # rollback if any exception occured
            msg="Failed inserting record into Nifty50Derived table {}".format(error)
            easygui.msgbox(msg, title="Process Message")
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                easygui.msgbox("MySQL connection is closed", title="Process Message")
            return

