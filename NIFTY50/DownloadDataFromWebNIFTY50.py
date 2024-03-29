import os
import easygui
from selenium import webdriver
import configparser

'''
Script to download daily Nifty50 Data From Web
'''

class DownloadDataFromWebNIFTY50:

    def downloadNifty50(self):
        config_obj = configparser.ConfigParser()
        config_obj.read("Y:\\Python CSV\\1 Main Technical Analysis of National Stock Exchange\\Config\\Config.cfg")

        # to remove file
        try:
            os.remove(config_obj.get("Setting","web_download_nifty50")+"\\data.csv")
        except OSError:
            pass

        # To prevent download dialog
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.folderList', 2) # custom location
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        profile.set_preference('browser.download.dir', config_obj.get("Setting","web_download_nifty50"))
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')

        driver = webdriver.Firefox(profile)

        driver.get('https://www.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm')

        driver.find_element_by_class_name('download-data-link1').click()
        easygui.msgbox("Download File Completed Successfully", title="Process Message")
        return


