from numpy.core.fromnumeric import size
import requests
import json
import configparser
import time
from datetime import datetime
import numpy as np
from Tle import Tle
from query import insert_tle


class MyError(Exception):
    def __init___(self,args):
        Exception.__init__(self,"my exception was raised with arguments {0}".format(args))
        self.args = args

uriBase                = "https://www.space-track.org"
requestLogin           = "/ajaxauth/login"
requestCmdAction       = "/basicspacedata/query"
requestDebris   = "/class/tle/OBJECT_TYPE/DEB~~/EPOCH/>now-1/orderby/COMMENT asc/format/3le"

# ACTION REQUIRED FOR YOU:
#=========================
# Provide a config file in the same directory as this file, called SLTrack.ini, with this format (without the # signs)
# [configuration]
# username = XXX
# password = YYY
# output = ZZZ
#
# ... where XXX and YYY are your www.space-track.org credentials (https://www.space-track.org/auth/createAccount for free account)
# ... and ZZZ is your Excel Output file - e.g. starlink-track.xlsx (note: make it an .xlsx file)

# Use configparser package to pull in the ini file (pip install configparser)
print("Requesting data from space-track...")

config = configparser.ConfigParser()
config.read("../include/SLTrack.ini")
configUsr = config.get("configuration","username")
configPwd = config.get("configuration","password")
configOut = config.get("configuration","output")
siteCred = {'identity': configUsr, 'password': configPwd}

with requests.Session() as session:
    # need to log in first. note that we get a 200 to say the web site got the data, not that we are logged in
    resp = session.post(uriBase + requestLogin, data = siteCred)
    if resp.status_code != 200:
        raise MyError(resp, "POST fail on login")

    # this query picks up all Starlink satellites from the catalog. Note - a 401 failure shows you have bad credentials 
    resp = session.get(uriBase + requestCmdAction + requestDebris)
    if resp.status_code != 200:
        print(resp)
        raise MyError(resp, "GET fail on request for Starlink satellites")


    session.close()

database = (resp.text.split("\r\n"))
debrislist = []

for data in range(0, np.size(database)-1, 3):
    name = database[data]
    s = database[data+1]
    t = database[data+2]
    new_tle = Tle(name, s, t)
    if new_tle.name.find('DEB') != -1: debrislist.append(new_tle)
    insert_tle(new_tle)
print("Acquired", (size(database)-1)/3, "tle objects.")
print("From", (size(database)-1)/3, "tle objects,", size(debrislist), "contained DEB prefix.")
print("All tle data were added into the database.")
print("Completed session")