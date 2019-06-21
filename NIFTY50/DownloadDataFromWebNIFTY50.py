# to remove file

import os
import easygui
from selenium import webdriver

class DownloadDataFromWebNIFTY50:

    def downloadNifty50(self):

        try:
            os.remove("data.csv")
        except OSError:
            pass

        # To prevent download dialog
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.folderList', 2) # custom location
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        profile.set_preference('browser.download.dir', 'F:\\Python CSV\\1 Main Technical Analysis of National Stock Exchange')
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')

        driver = webdriver.Firefox(profile)

        driver.get('https://www.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm')

        driver.find_element_by_class_name('download-data-link1').click()
        easygui.msgbox("Download File Completed Successfully", title="Process Message")
        return


