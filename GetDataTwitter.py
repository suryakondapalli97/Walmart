# importing required packages
import tweepy
import pandas as pd
import config

from pandas.io import sql
import MySQLdb

# create a class called KeywordStream and then a function to print out of status JSON record.--->Testing purpose
class KeywordStream(tweepy.Stream):
    
    def on_status(self, status):
    print(status)

    #Starting a stream through Twitter’s API using Consumer key and tokens
    stream = KeywordStream(
    config.consumer_key, config.consumer_secret,
    config.access_token, config.access_token_secret
    )

    #We can then use Tweepy’s stream.filter to specify a keyword that we want to stream. For us its Justin Bieber
    stream.filter(track=['Justin Bieber'])

    #We may get many variables from the above filter but want all related to music
    tweet_text = []
    songname = []
    date_time = []
    id_str = []
    verified = []
    followers_count = []
    retweet_count = []
    statuses_count = []

class KeywordStream(tweepy.Stream):
    def on_status(self, status):
      if status.truncated == False:
        tweet_text.append(status.text)
      else:
        tweet_text.append(status.extended_tweet["full_text"])  
      songname.append(status.user.song_name)
      date_time.append(status.created_at)
      id_str.append(status.id_str)
      verified.append(status.user.verified)
      followers_count.append(status.user.followers_count)
      retweet_count.append(status.user.retweet_count)
      statuses_count.append(status.user.statuses_count)

    song = pd.DataFrame({‘Songname’: songname, ‘ID’: id_str, ‘Tweet’: tweet_text})
    twitter_analytics = pd.DataFrame({'Verified Status': verified, 'Follower Count': followers_count, 'Retweet Count': retweet_count, 'Statuses Count': statuses_count})
    obtained_date = pd.DataFrame({'DateTime Created': date_time})

    obtained_date[‘DateTime Created’] = pd.to_datetime(obtained_date[‘DateTime Created’])
    obtained_date[‘day’] = obtained_date[‘DateTime Created’].dt.day
    obtained_date[‘month’] = obtained_date[‘DateTime Created’].dt.month
    obtained_date[‘year’] = obtained_date[‘DateTime Created’].dt.year
    obtained_date[‘day_of_week’] = obtained_date[‘DateTime Created’].dt.day_name()

    song.to_csv(Justin_Songs.csv’, index=False)
    twitter_analytics.to_csv(Songs_Analtics.csv’, index=False)
    obtained_date.to_csv(‘twitteruserpublisheddate.csv’, index=False)

    con = MySQLdb.connect(host='-------------',
                        database='------------',
                        user='-------------',
                        password='----------')

    sql.write_frame(song, con=con, name='Justin_Songs', 
                    if_exists='replace', flavor='mysql')

    sql.write_frame(twitter_analytics, con=con, name='Songs_Analtics', 
                    if_exists='replace', flavor='mysql')

    

