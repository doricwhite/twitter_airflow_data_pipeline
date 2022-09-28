# Imports
import twitter_api_info as api_info
import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

# Twitter API Object
details = api_info.TwitterApiInfo()

def run_twitter_etl():
    #API details obtained from file
    API_KEY = details.apiKey()
    API_SECRET_KEY = details.apiSecretKey()
    ACCESS_TOKEN = details.accessToken()
    ACCESS_SECRET_TOKEN = details.accessTokenSecret()


    # Twitter Authentication using tweepy
    auth=tweepy.OAuthHandler(API_KEY, API_SECRET_KEY )
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)

    # API Object
    api = tweepy.API(auth)

    # Obtain Tweets from a User TimeLine
    tweets = api.user_timeline(
        screen_name = '@elonmusk',
        # The number of tweets you want to extract (200 is the max allowed)
        count=200,
        include_rts = False,
        tweet_mode='extended'
    )

    # print(tweets)

    # Transform the data 
    tweet_list = []

    for tweet in tweets:
        text = tweet._json["full_text"]
        
        redefined_tweet = {
            "user": tweet.user.screen_name,
            "text": text,
            "favorite_count": tweet.favorite_count,
            "retweet_count": tweet.retweet_count,
            "created_at": tweet.created_at
        }
        
        # Add restructured tweet to new list
        tweet_list.append(redefined_tweet)

    # Create Dataframe from list with pandas
    df = pd.DataFrame(tweet_list)

    # Create csv file and save to AWS S3 Bucket
    df.to_csv("s3://bucket_name_here/elon_musk_twitter_data.csv")
