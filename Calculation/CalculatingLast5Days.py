import easygui
import configparser
class CalculatingLast5Days:
    config_obj = configparser.ConfigParser()
    config_obj.read("Y:\\Python CSV\\1 Main Technical Analysis of National Stock Exchange\\Config\\Config.cfg")
    def calculatingData(self):
        easygui.msgbox("Hello From Calculation", title="Process Message")
        return