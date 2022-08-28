# Twitter Web Scraper with Twitter API and Tweepy Python

This scraper is coded using python to scrape through 200 recent tweets regarding the brand Tesla. 
It uses the library Tweepy to extract the necessary data and then stores these information into a CSV file.

## Instructions
1. Before running the codes, please ensure that you have the required packages installed.  
- pip install tweepy
- pip install pandas
- pip install time
- pip install psutil

2. After installation of packages, modify the parameter input of.   
- twitter_login function: with a valid email address, username and password that will able to access and log into Twitter
- twitter_search function: with the search URL, and the number of tweets to scrape.  

3. Lastly change the file path in tweets.to_csv('C:/Users/user/desktop/tweets.csv') to the directory that you would like the csv file to be stored in.






