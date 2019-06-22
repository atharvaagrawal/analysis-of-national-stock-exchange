import asyncio
import csv
import mysql.connector
import os.path
import pandas as pd
import easygui
from datetime import datetime
from mysql.connector import Error
from mysql.connector import errorcode
import configparser
'''
This Script is for Storing the Bhavcopy data into Database.
'''
class StoreIntoDatabaseNiftyAll:
    def executeStoreNiftyAll(self):

        config_obj = configparser.ConfigParser()
        config_obj.read("F:\\Python CSV\\1 Main Technical Analysis of National Stock Exchange\\Config\\Config.cfg")

        path = config_obj.get("Setting", "nifty_all_file_path")

        download_path="Download the data on this Location: "+path+" with name as NiftyAll.csv "

        easygui.msgbox(download_path,title="Process Message")

        if not os.path.exists(path):
            easygui.msgbox("First Download the file", title="Process Message")
            return


        file = open(path, newline='')
        reader = csv.reader(file)

        header = next(reader)  # the first line is the header

        data = []
        count = 1
        for row in reader:
            Symbol = row[0]
            Series = row[1]
            Open = float(row[2].replace(',', ''))
            High = float(row[3].replace(',', ''))
            Low = float(row[4].replace(',', ''))
            Close = float(row[5].replace(',', ''))
            Last = float(row[6].replace(',', ''))
            PrevClose = float(row[7].replace(',', ''))
            TOTTRDQTY = float(row[8].replace(',', ''))
            TOTTRDVAL = float(row[9].replace(',', ''))
            TIMESTAMP = datetime.strptime(row[10], '%d-%b-%Y').strftime('%Y-%m-%d')
            TOTALTRADES  = float(row[11].replace(',', ''))
            ISIN = row[12]

            count += 1
            data.append([Symbol,Series, Open, High, Low,Close,Last,PrevClose,TOTTRDQTY,TOTTRDVAL,TIMESTAMP,TOTALTRADES,ISIN])
        print("Ok")
        # DataBase Connection
        try:
            connection = mysql.connector.connect(host=config_obj.get("Setting", "host"),
                                                 database=config_obj.get("Setting", "database"),
                                                 user=config_obj.get("Setting", "user"),
                                                 password=config_obj.get("Setting", "password"))
            cursor = connection.cursor()
            # to check repeated record
            qry = "Select * from NiftyAll"
            pdata = pd.read_sql_query(qry, connection)

            if pdata.empty == True:
                pass
            else:
                pdata['TIMESTAMP'] = pd.to_datetime(pdata.TIMESTAMP)
                todaysday = datetime.today().strftime('%Y-%m-%d')
                ts = pd.to_datetime(todaysday) #Todays Date
                diff =  pdata.tail(1).TIMESTAMP - ts
                print(pdata.tail(1).TIMESTAMP)
                # Converting into int
                daystocheck = int(diff.dt.days)
                print(daystocheck)

                if daystocheck >= 0:
                    easygui.msgbox("This Data is already Present or Older Data. Please download new Data.", title="Process Message")
                    if (connection.is_connected()):
                        cursor.close()
                        connection.close()
                        file.close()
                    return
                # Loop to store data
            for i in data:
                cursor.execute(""" INSERT INTO NiftyAll VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                               (i[0], i[1], i[2], i[3], i[4] , i[5], i[6], i[7], i[8], i[9]  , i[10],i[11],i[12] ) )
            connection.commit()
            easygui.msgbox("Record inserted successfully into NiftyAll table", title="Process Message")
        except mysql.connector.Error as error:
            connection.rollback()  # rollback if any exception occured
            msg="Data Already Present Failed inserting record into NiftyAll table {}".format(error)
            easygui.msgbox(msg, title="Process Message")
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                file.close()
                easygui.msgbox("MySQL connection is closed", title="Process Message")


