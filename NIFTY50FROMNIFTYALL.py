import csv
import mysql.connector
import os.path
import pandas as pd
import easygui
import datetime
from mysql.connector import Error
from mysql.connector import errorcode
import configparser

'''
This Script is for too Copy the Data of NiftyALL i.e the Bhavcopy Data to Nifty50Derived Table 
which contain only Top 50 Nifty Symbol.
'''

class Nifty50FromNiftyAll:
    def copyData(self):

        config_obj = configparser.ConfigParser()
        config_obj.read("Y:\\Python CSV\\1 Main Technical Analysis of National Stock Exchange\\Config\\Config.cfg")

        # DataBase Connection
        print("Hellos from NiftyAll to Nifty50Derived ")
        try:
            connection = mysql.connector.connect(host=config_obj.get("Setting", "host"),
                                                 database=config_obj.get("Setting", "database"),
                                                 user=config_obj.get("Setting", "user"),
                                                 password=config_obj.get("Setting", "password"))
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
            last_day_of_nifty50 ="SELECT timestamp FROM Nifty50Derived WHERE Timestamp IN ( SELECT MAX( Timestamp ) " \
                                 "FROM Nifty50Derived  )  Group by timestamp ORDER BY  timestamp ASC"
            cursor.execute(last_day_of_nifty50)
            last_day_of_nifty50 = cursor.fetchall()


            if(len(last_day_of_nifty50)==0):
                last_day_of_nifty50 = "SELECT timestamp FROM NiftyAll WHERE Timestamp IN ( SELECT MIN( Timestamp ) " \
                                      "FROM NiftyAll  )  Group by timestamp ORDER BY  timestamp ASC"
                cursor.execute(last_day_of_nifty50)
                last_day_of_nifty50 = cursor.fetchall()


            last_day_of_niftyAll="SELECT timestamp FROM NiftyAll WHERE Timestamp IN ( SELECT MAX( Timestamp ) " \
                                 "FROM NiftyAll  )  Group by timestamp ORDER BY  timestamp ASC"
            cursor.execute(last_day_of_niftyAll)
            last_day_of_niftyAll = cursor.fetchall()

            last_day_of_nifty50 = last_day_of_nifty50[0][0]
            last_day_of_niftyAll = last_day_of_niftyAll[0][0]

            print(last_day_of_nifty50)
            print(last_day_of_niftyAll)

            if(last_day_of_niftyAll == last_day_of_nifty50):
                easygui.msgbox("Data Already Present in Nifty50Derived table", title="Process Message")
                pass
            else:
                print("Entered")
                sql_select_query = "Select * from NiftyAll  where Symbol = (Select DISTINCT SYMBOL FROM NIFTY50 " \
                                   "WHERE NIFTY50.SYMBOL = NIFTYALL.SYMBOL)  and Series='EQ' and timestamp  " \
                                   "between '"+str(last_day_of_nifty50)+"' and '" + str(last_day_of_niftyAll)+"'"

                print(sql_select_query)

                cursor.execute(sql_select_query)
                records = cursor.fetchall()

                # Loop to store data
                for i in records:
                    cursor.execute(""" INSERT INTO Nifty50Derived VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                                   (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12]))

                connection.commit()
                easygui.msgbox("Record inserted successfully into Nifty50Derived table", title="Process Message")

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

