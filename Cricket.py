#!/usr/bin/env python

import requests,MySQLdb

from bs4 import BeautifulSoup

import pynotify

from time import sleep
#This will send notifications after every 60 secs
def sendmessage(title, message):

    pynotify.init("Test")

    notice = pynotify.Notification(title, message)

    notice.show()
        
    return
#Url contains link to Cricket Scores Website
url = ""

while True:

    r = requests.get(url)

    while r.status_code is not 200:

            r = requests.get(url)

    soup = BeautifulSoup(r.text,"lxml")

    data = soup.find_All("here the tag which contains the score")
#Here the Score1 variable contains 1st data which got from the tag
    score1 = data[0].text
    print score1    
    
    sendmessage("Data:",score1)

    sleep(60)   
