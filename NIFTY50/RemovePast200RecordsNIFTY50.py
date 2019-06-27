import re
import mysql.connector
import pandas as pd
import easygui
import configparser
from datetime import datetime , date, time, timedelta

'''
Script to delete Past 200 Days Record From Nifty50 Table if Data is more than 200 days then only delete data from DataBase. 
'''

def remove200():
    config_obj = configparser.ConfigParser()
    config_obj.read("Y:\\Python CSV\\1 Main Technical Analysis of National Stock Exchange\\Config\\Config.cfg")

    try:
        connection = mysql.connector.connect(host=config_obj.get("Setting", "host"),
                                             database=config_obj.get("Setting", "database"),
                                             user=config_obj.get("Setting", "user"),
                                             password=config_obj.get("Setting", "password"))

        todaysday=datetime.today().strftime('%Y-%m-%d')
        qry = "Select * from Nifty50"
        cursor = connection.cursor()
        data = pd.read_sql_query(qry,connection)
        if data.empty == True:
            easygui.msgbox("No Data Present", title="Process Message")
            exit(0)

        data['TIMESTAMP'] = pd.to_datetime(data.TIMESTAMP) #Database Date

        ts = pd.to_datetime(todaysday) #Todays Date

        diff = ts - data.head(1).TIMESTAMP # Date Difference
        #Converting into int
        daystocheck = int(diff.dt.days)

        #Getting days after 200 days
        date_after_200 = data.head(1).TIMESTAMP + timedelta(days=200)
        s = str(date_after_200.apply(str)) # Converting to String
        match = re.search(r'\d{4}-\d{2}-\d{2}', s)
        date_after_200 = datetime.strptime(match.group(), '%Y-%m-%d').date()
        date_after_200 = str(date_after_200)

        if daystocheck >= 200:
            msg="Data is more than 200 days:"+str(daystocheck)
            easygui.msgbox(msg, title="Process Message")
            qry = "Delete from Nifty50 where TIMESTAMP <= %s "
            cursor.execute(qry,(date_after_200,))
            connection.commit()
            easygui.msgbox("Record deleted successfully from Nifty50 table", title="Process Message")

        else:
            msg="Only for "+str(daystocheck+1)+" Number of day(s) Data is Present."
            easygui.msgbox(msg, title="Process Message")

    except mysql.connector.Error as error :
        msg="Failed to delete record: {}".format(error)
        easygui.msgbox(msg, title="Process Message")
    finally:
        #closing database connection.
        if(connection.is_connected()):
            connection.close()
            easygui.msgbox("MySQL connection is closed", title="Process Message")
