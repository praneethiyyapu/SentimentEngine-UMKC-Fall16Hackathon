import tweepy
import csv #Import csv
import re
auth = tweepy.auth.OAuthHandler('23cTqXHXdkUWACSff0N0XqP7K', 'xYaeYBtnBuC4AwhOOITgx5rF1aueYL1sDRPNZ6e6o2cDuHuolU')
auth.set_access_token('138033110-3dpqx2pEqvyDGhDGd8UrGe9Ac35hpvXmEAaEATyy', '5eKRsxHj6KZPcyXZm1HiyFeqEvPDQ5yUNC9ipxeYLwUi2')

api = tweepy.API(auth,wait_on_rate_limit=True)
# Open/Create a file to append data
text_file = open("result.txt", "w ")
#Use csv Writer

for tweet in tweepy.Cursor(api.search, 
                    q="#CalExit", 
                    since="2016-11-08", 
                    until="2016-11-10", 
                    lang="en").items():
    #Write a row to the csv file/ I use encode utf-8
    text_file.write(re.sub('\W+'," ", tweet.text.encode('utf-8') ))
    print tweet.created_at, tweet.text.encode('utf-8')
text_file.close()
