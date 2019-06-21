import re
import mysql.connector
import pandas as pd
import easygui

from mysql.connector import Error
from mysql.connector import errorcode
from matplotlib import pyplot as plt
from datetime import datetime , date, time, timedelta

def remove200():
    connection = mysql.connector.connect(host='localhost', database='Nifty', user='Atharva', password='Atharva@007')

    try:
        todaysday=datetime.today().strftime('%Y-%m-%d')
        qry = "Select * from Nifty50"
        cursor = connection.cursor()
        data = pd.read_sql_query(qry,connection)
        if data.empty == True:
            easygui.msgbox("No Data Present", title="Process Message")
            exit(0)

        data['Today'] = pd.to_datetime(data.Today) #Database Date

        ts = pd.to_datetime(todaysday) #Todays Date

        diff = ts - data.head(1).Today # Date Difference
        #Converting into int
        daystocheck = int(diff.dt.days)

        #Getting days after 200 days
        date_after_200 = data.head(1).Today + timedelta(days=200)
        s = str(date_after_200.apply(str)) # Converting to String
        match = re.search(r'\d{4}-\d{2}-\d{2}', s)
        date_after_200 = datetime.strptime(match.group(), '%Y-%m-%d').date()
        date_after_200 = str(date_after_200)

        if daystocheck >= 200:
            msg="Data is more than 200 days:"+str(daystocheck)
            easygui.msgbox(msg, title="Process Message")
            d = input("Enter y to delete data else n:")
            if d is 'y':
                qry = "Delete from csvtest where Today = %s "
                cursor.execute(qry,(date_after_200,))
                connection.commit()
                easygui.msgbox("Record deleted successfully from csvtest table", title="Process Message")
            else:
                exit(0)
        else:
            msg="Only for "+str(daystocheck)+" Number of day(s) Data is Present."
            easygui.msgbox(msg, title="Process Message")

    except mysql.connector.Error as error :
        msg="Failed to delete record: {}".format(error)
        easygui.msgbox(msg, title="Process Message")
    finally:
        #closing database connection.
        if(connection.is_connected()):
            connection.close()
            easygui.msgbox("MySQL connection is closed", title="Process Message")

remove200()