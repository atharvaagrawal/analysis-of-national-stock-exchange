import csv
import mysql.connector
import os.path
import pandas as pd
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import datetime
import easygui
import asyncio
import configparser

'''
Script to insert the Nifty50 Daily data into Database. 
'''

class StoreIntoDatabaseNifity50:

    def executeStore(self):

        config_obj = configparser.ConfigParser()
        config_obj.read("Y:\\Python CSV\\1 Main Technical Analysis of National Stock Exchange\\Config\\Config.cfg")

        path = config_obj.get("Setting","nifty50_file_path")

        download_path = "Download the data on this Location:"+path+" with name as data.csv"
        easygui.msgbox(download_path,title="Process Message")


        todaysday = datetime.today().strftime('%Y-%m-%d')
        if not os.path.exists('data.csv'):
            easygui.msgbox("First Download the file", title="Process Message")
            return


        file = open(path, newline='')
        reader = csv.reader(file)

        header = next(reader)  # the first line is the header

        data = []
        count = 1
        for row in reader:
            if (count == 52):
                break;
            Symbol = row[0]
            Open = float(row[1].replace(',', ''))
            High = float(row[2].replace(',', ''))
            Low = float(row[3].replace(',', ''))
            LastTradedPrice= float(row[4].replace(',', ''))
            ChangeValue= float(row[5].replace(',', ''))
            ChangePercentage= float(row[6].replace(',', ''))
            TradedVolumeLacs= float(row[7].replace(',', ''))
            TradedValueCrs= float(row[8].replace(',', ''))
            Week52High= float(row[9].replace(',', ''))
            Week52Low= float(row[10].replace(',', ''))
            Days365PercentageChange= float(row[11].replace(',', ''))
            Days30PercentageChange= float(row[12].replace(',', ''))

            count += 1
            data.append([todaysday, Symbol, Open, High, Low,LastTradedPrice,ChangeValue,ChangePercentage,
                         TradedVolumeLacs,TradedValueCrs,Week52High,Week52Low,Days365PercentageChange,
                         Days30PercentageChange])
        print("Ok")
        # DataBase Connection
        
        try:
            connection = mysql.connector.connect(host=config_obj.get("Setting", "host"),
                                                 database=config_obj.get("Setting", "database"),
                                                 user=config_obj.get("Setting", "user"),
                                                 password=config_obj.get("Setting", "password"))
            cursor = connection.cursor()
            # to check repeated record
            qry = "Select * from Nifty50"
            pdata = pd.read_sql_query(qry, connection)
            if pdata.empty == True:
                pass
            else:
                pdata['TIMESTAMP'] = pd.to_datetime(pdata.TIMESTAMP)
                todaysday = datetime.today().strftime('%Y-%m-%d')
                ts = pd.to_datetime(todaysday)  # Todays Date
                diff = pdata.tail(1).TIMESTAMP - ts
                print(pdata.tail(1).TIMESTAMP)
                # Converting into int
                daystocheck = int(diff.dt.days)
                print(daystocheck)

                if daystocheck >= 0:
                    easygui.msgbox("This Data is already Present or Older Data . Please download new Data.",
                                   title="Process Message")
                    if (connection.is_connected()):
                        cursor.close()
                        connection.close()
                        file.close()
                    return
                # Loop to store data
            for i in data:
                cursor.execute(""" INSERT INTO Nifty50 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                               (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10],
                                i[11], i[12], i[13]))
            connection.commit()
            easygui.msgbox("Record inserted successfully into Nifty50 table", title="Process Message")
        except mysql.connector.Error as error:
            connection.rollback()  # rollback if any exception occured
            print("Error".format(error))
            msg = "Failed inserting record into Nifty50 table {}"
            easygui.msgbox(msg, title="Process Message")
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                file.close()
                easygui.msgbox("MySQL connection is closed", title="Process Message")
            return

        
