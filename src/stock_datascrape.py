__author__ = "Justine"
__date__ = "$Mar 7, 2015 9:57:17 PM$"

#program that extracts stock price and percent change for each dow jones company
#saves all results into a dated folder and labelled company files
#fully equipt with a scheduler starting at 5PM each day until terminated

import sys, urllib2, os
import re, json, time, datetime
from os.path import join as j
from apscheduler.schedulers.blocking import BlockingScheduler



reload(sys)
sys.setdefaultencoding("utf-8")

try:
    today = datetime.date.today()#find todays date
    betterToday = today.isoformat()#make it pretty
    os.mkdir(betterToday)#use today as the folder name
except:
    print "no file writes for you! (already done today)"
    pass


dow_jones_list = ["mmm","axp","aapl","ba","cat","cvx","csco","ko","dis","dd","xom","ge","gs","hd","ibm","intc","jnj","jpm","mcd","mrk","msft","nke","pfe","pg","trv","utx","unh","vz","v","wmt"]

    
def findName():
    i = 0
    while i < len(dow_jones_list):
        url = "http://finance.yahoo.com/q;_ylt=Ar8JnTphTkbeh2wEkYQthyYnv7gF?uhb=uhb2&fr=uh3_finance_vert_gs&type=2button&s="+ dow_jones_list[i]
        web_file = urllib2.urlopen(url)
        html_text = web_file.read()
        #step one company name
        regex1 = '<h2>(.+?)('+dow_jones_list[i].upper()+')</h2>'
        pattern1 = re.compile(regex1)
        name = re.findall(pattern1,html_text)
        filename = dow_jones_list[i] + '.txt'
        pathToFile = j(betterToday, filename)
        file = open(pathToFile, 'a')
        file.write('Name: ')
        file.write(json.dumps(name))
        file.write('\n')
        file.close()
        #print name #uncomment for testing
        i+=1
        
def findPrice():
    i = 0
    while i < len(dow_jones_list):
        url = "http://finance.yahoo.com/q;_ylt=Ar8JnTphTkbeh2wEkYQthyYnv7gF?uhb=uhb2&fr=uh3_finance_vert_gs&type=2button&s="+ dow_jones_list[i]
        web_file = urllib2.urlopen(url)
        html_text = web_file.read()
        #step 2 company price
        regex2 = '<span id="yfs_l84_'+ dow_jones_list[i] +'">(.+?)</span>'
        pattern2 = re.compile(regex2)
        price = re.findall(pattern2,html_text)
        filename = dow_jones_list[i] + '.txt'
        pathToFile = j(betterToday, filename)
        file = open(pathToFile, 'a')
        file.write('Price: ')
        file.write(json.dumps(price))
        file.write('\n')
        file.close()
        #print price #uncomment for testing
        i+=1


def findPercent():
    i = 0
    while i < len(dow_jones_list):
        url = "http://finance.yahoo.com/q;_ylt=Ar8JnTphTkbeh2wEkYQthyYnv7gF?uhb=uhb2&fr=uh3_finance_vert_gs&type=2button&s="+ dow_jones_list[i]
        web_file = urllib2.urlopen(url)
        html_text = web_file.read()
        #step 3 percent increase or decrease
        regex3 = '<span id="yfs_p43_'+dow_jones_list[i]+'">(.+?)</span>'
        pattern3 = re.compile(regex3)
        percent = re.findall(pattern3,html_text)
        filename = dow_jones_list[i] + '.txt'
        pathToFile = j(betterToday, filename)
        file = open(pathToFile, 'a')
        file.write('Percent change: ')
        file.write(json.dumps(percent))
        file.write('\n')
        file.close()
        #print percent #uncomment for testing
        i+=1


def main():#main function returns all needed topics
    try:
        findName()
        findPrice()
        findPercent()
    except:
        print 'error saving data' #error checking
        print betterToday
        pass
    
sched = BlockingScheduler()
@sched.scheduled_job('cron', day_of_week= 'mon-sun', hour = 17) #runs every day at 5PM military time     
def scheduled_job():
    main()


if __name__ == "__main__":
    sched.start()
#user must terminate program

    
    
  