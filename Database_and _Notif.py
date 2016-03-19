#!/usr/bin/env py0thon

import requests,MySQLdb

from bs4 import BeautifulSoup

import pynotify

from time import sleep

#your url here
url = ""

#This will send notifications after every 60 secs
def sendmessage(title, message):

#Message title here
    pynotify.init("")

    notice = pynotify.Notification(title, message)

    notice.show()
        
    return

while True:

    r = requests.get(url)

    while r.status_code is not 200:

            r = requests.get(url)

    soup = BeautifulSoup(r.text,"lxml")

    data = soup.find_all("tr")
                #Data to be displayed here as notif
    score1 = data[0].text
    score2 = data[1].text
    score3 = data[2].text
    score4 = data[3].text
    score5 = data[4].text
    score6 = data[6].text
    name=data[0].text
    print score1
    print score2
    print score3
    print score4
    print score5  

    for dat in data:
        print data
    #code for data base connection mysql
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="")        # name of the data base
                     
    cur = db.cursor()

    # Use all the SQL you like
    cur.ex`ecute(insert into Drugs(Drug_name,Medicine_name,D_Quantity,Price,Manufacturer) values(%s,%s,%s,%s,%s),(score1,score2,score3,score4,score5))
       
    db.commit();
    db.close()
     #  print all the first cell of all the rows
    row=cur.fetchall()
    for rows in row:
        print rows

    sendmessage("title",score1+"\n"+score2+"\n"+score3+"\n"+score4+"\n"+score5);

    sleep(60)  


