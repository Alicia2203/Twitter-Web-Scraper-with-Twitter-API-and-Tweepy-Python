#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 23:34:57 2022

@author: alicia
"""
import tweepy
import pandas as pd # For saving the response data in CSV format
import time 
import psutil

consumer_key = "rfUoC2hizynpQnansDPqWPwc3"
consumer_secret = "YTPBSLCEziH4GTagZ6NUuffrt4NfSN3dZivxodNhgu9zJkZBoM" 
access_key = "2761702328-lIjz6FcrP7fVwzSwiyjno5vb95jrdcktlF7tb32"
access_secret = "eoLjIuwECwi8aGWArTkToISqxeTygXFfqY82VkSlRzJe4" 


def twitter_setup():
    # Authentication and access using keys
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    # Calling API
    api = tweepy.API(auth, wait_on_rate_limit=True)
    
    try:
        api.verify_credentials()
        print("Successful Authentication")
    except:
        print("Failed authentication")
    return api

# An extractor object to hold the api data by calling in twitter_setup()function
extractor = twitter_setup()

# create a function that Extract tweets based on keywords
def keywords_tweets(api, keyword, number_of_tweets):
    new_keyword = keyword + " -filter:retweets"
    tweets = []
    for status in tweepy.Cursor(api.search_tweets, q=new_keyword, 
                                lang="en", tweet_mode='extended', 
                                result_type='mixed').items(number_of_tweets):
          tweets.append(status)
    return tweets

# Grab Currrent Time Before Running the Code
start = time.time()

# Scrape tweets based on keywords
keyword_alltweets = keywords_tweets(extractor, "Tesla -nikola", 200)

# Grab Currrent Time After Running the Code
end = time.time()

#Subtract Start Time from The End Time
total_time = end - start
print("\n Time taken to Scrape Tweets: " + str(total_time))

print('\n cpu_percent', psutil.cpu_percent() )
print("\n" + str(psutil.virtual_memory()))
print('\n memory % used:', str(psutil.virtual_memory()[2]) + "\n")

# create a pandas DataFrame by looping through each element and add it to the DataFrame
data = pd.DataFrame(data=[tweet.full_text for tweet in keyword_alltweets], 
                    columns=['Tweets'])
data['Tweets_ID'] = [tweet.id for tweet in keyword_alltweets]
data['Date'] = [tweet.created_at for tweet in keyword_alltweets]
data['Source'] = [tweet.source for tweet in keyword_alltweets]
data['Likes_no'] = [tweet.favorite_count for tweet in keyword_alltweets]
data['Retweets_no'] = [tweet.retweet_count for tweet in keyword_alltweets]
data['Location'] = [tweet.user.location for tweet in keyword_alltweets]
data['UID'] = [tweet.user.id for tweet in keyword_alltweets]
data['Username'] = [tweet.user.screen_name for tweet in keyword_alltweets]
data['DisplayName'] = [tweet.user.name for tweet in keyword_alltweets]
data['Verified'] = [tweet.user.verified for tweet in keyword_alltweets]

data['ProfileLink'] = [tweet.user.screen_name for tweet in keyword_alltweets]
data['Tweet_URL'] = [tweet.id_str for tweet in keyword_alltweets]
for i in range(len(keyword_alltweets)):
    data['Tweet_URL'][i]="https://twitter.com/"+data['ProfileLink'][i] +"/status/"+data['Tweet_URL'][i]
    data['ProfileLink'][i] = "https://twitter.com/" + data['ProfileLink'][i]
  
# import to csv file
data.to_csv('C:/Users/user/desktop/tweets.csv')



































