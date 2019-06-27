import re
import mysql.connector
import pandas as pd
import easygui
import configparser
from datetime import datetime , date, time, timedelta

'''
Script to Check Days That Date is not present of NiftyAll Table. 
'''
class CheckForRemainingDayNiftyAll:
    def remainingDayData(self):
        config_obj = configparser.ConfigParser()
        config_obj.read("Y:\\Python CSV\\1 Main Technical Analysis of National Stock Exchange\\Config\\Config.cfg")

        try:
            connection = mysql.connector.connect(host=config_obj.get("Setting", "host"),
                                                 database=config_obj.get("Setting", "database"),
                                                 user=config_obj.get("Setting", "user"),
                                                 password=config_obj.get("Setting", "password"))

            todaysday = datetime.today().strftime('%Y-%m-%d')
            qry = "select * from NiftyAll ORDER BY TIMESTAMP ASC"
            data = pd.read_sql_query(qry, connection)

            if data.empty == True:
                easygui.msgbox("No Data Present", title="Process Message")
                return

            data['TIMESTAMP'] = pd.to_datetime(data.TIMESTAMP)  # Database Date

            end = pd.to_datetime(todaysday)  # Todays Date
            start = data.tail(1).TIMESTAMP   # Last Record Date
            delta = end - start
            s = ''
            dates = ''
            d = int(delta.dt.days) + 1

            for i in range(1,d):
                s =  str((start + timedelta(days=i)).dt.date)
                match = re.search(r'\d{4}-\d{2}-\d{2}', s)
                dates = dates + str(match.group())+"\n"

            easygui.msgbox(dates, title="Remaining Days")


        except mysql.connector.Error as error :
            msg="Failed to delete record: {}".format(error)
            easygui.msgbox(msg, title="Process Message")
        finally:
            #closing database connection.
            if(connection.is_connected()):
                connection.close()
                easygui.msgbox("MySQL connection is closed", title="Process Message")
            return

