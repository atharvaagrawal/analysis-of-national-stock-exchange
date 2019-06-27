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

# To Store Daily Bunch of record Based on Bhavcopy FileName in Numeric Order
# Ex: I have Bhav Copy Files from 1 May to 15 May as 1.csv , 2.csv, ... ,15.csv So then I can Insert the
# Data of All this File at once using this Python Script

class StoreBunchofDataIntoNiftyAll:
    def executeStoreNiftyAll(self, config_obj):
        config_obj = configparser.ConfigParser()
        config_obj.read("Y:\\Python CSV\\1 Main Technical Analysis of National Stock Exchange\\Config\\Config.cfg")


        try:
            connection = mysql.connector.connect(host=config_obj.get("Setting", "host"),
                                                 database=config_obj.get("Setting", "database"),
                                                 user=config_obj.get("Setting", "user"),
                                                 password=config_obj.get("Setting", "password"))
            cursor = connection.cursor()
            count = 1
            for i in range(2,12):

                path = config_obj.get("Setting", "store_bunch__nifty_all_path")+str(i)+".csv"

                if not os.path.exists(path):
                    easygui.msgbox("First Download the file", title="Process Message")
                    return

                file = open(path, newline='')
                reader = csv.reader(file)

                header = next(reader)  # the first line is the header

                data = []

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

                    data.append([Symbol,Series, Open, High, Low,Close,Last,PrevClose,TOTTRDQTY,TOTTRDVAL,TIMESTAMP,TOTALTRADES,ISIN])
                print("Ok")
                # DataBase Connection
                # to check repeated record
                qry = "select * from NiftyAll ORDER BY TIMESTAMP ASC"
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
                            break
                        return

                    # Loop to store data
                for i in data:
                    cursor.execute(""" INSERT INTO NiftyAll VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                                   (i[0], i[1], i[2], i[3], i[4] , i[5], i[6], i[7], i[8], i[9]  , i[10],i[11],i[12] ) )
                connection.commit()
                #easygui.msgbox("Record inserted successfully into NiftyAll table "+str(pdata.tail(1).TIMESTAMP), title="Process Message")
                print(count)
                count += 1
        except mysql.connector.Error as error:
            connection.rollback()  # rollback if any exception occured
            msg="Failed inserting record into NiftyAll table {}".format(error)
            easygui.msgbox(msg, title="Process Message")
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                file.close()
                easygui.msgbox("MySQL connection is closed", title="Process Message")
            return
