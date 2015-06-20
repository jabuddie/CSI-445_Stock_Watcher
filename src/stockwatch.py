__author__ = "Justine"

#program to extract tweets for each dow jones company
#saves all data into files labelled by company in a folder for the date run
#with a scheduler and timer to run 4 times a day starting at 5PM

import time, datetime, os
import twitter, sys, json
from os.path import join as j
from apscheduler.schedulers.blocking import BlockingScheduler

reload(sys)
sys.setdefaultencoding("utf-8")#set automatic encoding to utf-8 


#twitter credentials and authorization
myApi=twitter.Api(consumer_key = c_key, \
                  consumer_secret = c_secret, \
                  access_token_key = token_key, \
                  access_token_secret = token_secret)
                  
try:
    today = datetime.date.today()#find todays date
    betterToday = today.isoformat()#make it pretty
    os.mkdir(betterToday)#use today as the folder name
except:
    print "no file writes for you! (already done today)"
    pass


def save_text(tweet,label):
    #print '***************************' #uncomment for testing
    #print 'User Name: ', tweet['user']['screen_name'] #uncomment for testing
    #try:
	    #print 'Tweet Text: ', tweet['text']#for testing/visualization
    #except:
		#pass
    try:
            print 'writing to file...'
            string = tweet['user']['screen_name'] #designs filename to be the username
            filename = string + '_' + label + '.txt'
            pathToFile = j(betterToday, filename)
            file = open(pathToFile, 'a')
            file.write(json.dumps(tweet['text'])) #write one tweet into usernames file
            file.close()
    except:
                print 'unable to write to file'#error
                pass
            
            
               
def save_raw(tweet):#file to save all raw tweet useful data 
    raw = 'todays_raw_info.txt'
    pathToRaw = j(betterToday, raw)
    file = open(pathToRaw, 'a')
    #id write
    file.write(json.dumps('TweetID: '))
    file.write(json.dumps(tweet['id'], indent=1))
    #time write
    file.write(json.dumps('Time created: '))
    file.write(json.dumps(tweet['created_at'], indent=1))
    #user write
    file.write(json.dumps('User: '))
    file.write(json.dumps(tweet['user']['screen_name'], indent=1))
    #retweet t/f
    file.write(json.dumps('Retweet status: '))
    file.write(json.dumps(tweet['retweeted'], indent=1))
    #retweet write
    try:
        file.write(json.dumps('Retweet count: '))
        file.write(json.dumps(tweet['retweet_count'], indent=1))
    except:
        pass
    #favorite t/f
    file.write(json.dumps('Favorite status: '))
    file.write(json.dumps(tweet['favorited'], indent=1))
    #favorite count write
    try:
        file.write(json.dumps('Favorite count: '))
        file.write(json.dumps(tweet['favorite_count'], indent=1))
    except:
        pass
    #text write
    file.write(json.dumps("Tweet text:"))
    file.write(json.dumps(tweet['text'], indent=1))
    file.close()

               
def query_run(q,name):    
    for it in range(0,1): #gets 6 tweets each call
        raw_tweets = myApi.GetSearch(q, lang = 'en', result_type = 'recent', count = 6) #search tweets relating to query and location
    for raw_tweet in raw_tweets:
        tweet = json.loads(str(raw_tweet))#load tweet information in javascript object notation
        save_raw(tweet)
        save_text(tweet,name)#print tweet and document in file

         


def main():#calls to all thirty dow jones
    query_run('"$MMM stock" OR "3M stock" OR "3M"', 'MMM')
    query_run('"$AXP stock" OR "American Express stock" OR "American Express"', 'AXP')
    #query_run('"$T stock" OR "AT&T stock" OR "AT&T"', 'T')#goner
    query_run('"$BA stock" OR "Boeing stock" OR "Boeing"', 'BA')
    query_run('"$CAT stock" OR "Caterpillar stock" OR "Caterpillar Inc"', 'CAT')
    query_run('"$CVX stock" OR "Chevron stock" OR "Chevron Corp"', 'CVX')
    query_run('"$CSCO stock" OR "Cisco stock" OR "Cisco"', 'CSCO')
    query_run('"$KO stock" OR "Coca-Cola stock" OR "Coca-Cola"', 'KO')
    query_run('"$DIS stock" OR "Disney stock" OR "Disney"', 'DIS')
    query_run('"$DD stock" OR "E l du Port de Nemours and Co stock" OR "E. I. du Pont de Nemours and Company"', 'DD')
    query_run('"$XOM stock" OR "Exon stock" OR "Exon"', 'XOM')
    query_run('"$GE stock" OR "General Electric stock" OR "General Electric"', 'GE')
    query_run('"$GS stock" OR "Goldman Sachs stock" OR "Goldman Sachs"', 'GS')
    query_run('"HD $stock" OR "Home Depot stock" OR "Home Depot"', 'HD')
    query_run('"$IBM stock" OR "IBM stock" OR "IBM"', 'IBM')
    query_run('"$INTC stock" OR "Intel stock" OR "Intel"', 'INTC')
    query_run('"$JNJ stock" OR "Johnson & Johnson stock" OR "Johnson & Johnson"', 'JNJ')
    query_run('"$JPM stock" OR "JPMorgan Chase stock" OR "JP Morgan"', 'JPM')
    query_run('"$MCD stock" OR "McDonalds stock" OR "McDonalds"', 'MCD')
    query_run('"$MRK stock" OR "Merck stock" OR "Merck"', 'MRK')
    query_run('"$MSFT stock" OR "Microsoft stock" OR "Microsoft"', 'MSFT')
    query_run('"$NKE stock" OR "Nike stock" OR "NIKE"', 'NKE')
    query_run('"$PFE stock" OR "Pfizer stock" OR "Pfizer"', 'PFE')
    query_run('"$PG stock" OR "Proctor and Gamble stock" OR "P&G"', 'PG')
    query_run('"$TRV stock" OR "Travelers Companies Inc stock" OR "Travelers Companies Inc"', 'TRV')
    query_run('"$UTX stock" OR "United Technologies stock" OR "United Technologies"', 'UTX')
    query_run('"$UNH stock" OR "United Health stock" OR "United Health"', 'UNH')
    query_run('"$VZ stock" OR "Verizon stock" OR "Verizon"', 'VZ')
    query_run('"$V stock" OR "VISA stock" OR "Visa"', 'V')
    query_run('"$WMT stock" OR "Walmart stock" OR "Walmart"', 'WMT')
    query_run('"$AAPL stock" OR "Apple stock" OR "Apple Inc" OR "IPhone" OR "MACbook"', 'AAPL')#saw AAPL joined DOW 3-19 
    
    
     
sched = BlockingScheduler()
@sched.scheduled_job('cron', day_of_week= 'mon-sun', hour = 17) #runs every day at 5PM military time     
def scheduled_job():
    try:
        quarter_hour = 0
        while quarter_hour != 4: #timer runs program every 15 minutes for 1 hour 
            main()
            time.sleep(60*15)#time goes by seconds, we want to wait 15 minutes
            quarter_hour += 1
    except:
        print 'failure to run on:'
        print betterToday
        
    

if __name__ == '__main__':
   sched.start()#begin scheduled jobs
   
   #user must terminate program
    


