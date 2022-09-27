# File that contains the Twitter API Info
import twitter_api_info as api_info

import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

details = api_info.TwitterApiInfo()

#API details obtained from file
API_KEY = details.apiKey()
API_SECRET_KEY = details.apiSecretKey()
ACCESS_TOKEN = details.accessToken()
ACCESS_SECRET_TOKEN = details.accessTokenSecret()


# Twitter Authentication
auth=tweepy.OAuthHandler(API_KEY, API_SECRET_KEY )
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)

# API Object
api = tweepy.API(auth)

# Obtain Tweets from a User TimeLine
tweets = api.user_timeline(
    screen_name = '@elonmusk',
    # The number of tweets you want to extract (200 is the max allowed)
    count=200,
    # This is were or not to include re-tweets
    include_rts = False,
    tweet_mode='extended'
)

'''
If you get the "error 453 - You currently have Essential access which includes access to Twitter API v2 endpoints only", it could mean you only have "Essential" access to the API and need to request "Elevated Access" 
'''
print(tweets)
