import tweepy
import json
from tweepy import OAuthHandler

class Fetcher:
  consumer_key = "U28Q6OwIKyC2sMjggvspP7nfL"
  consumer_secret = "xf6iWfTsGz6VVUUwF5KhgOF1VSgHJpIntKjH3LbKHjypAXFIdg"
  access_token = "292479868-18a2fAylGE2DzDG8h9bH0PZ6u9y4CPZAsNE9GRLm"
  access_secret = "6dYHsPiYbvYzWzfr3X5cuvEGnQ14XHzwcfEfPQPl6YEEw"

  auth = OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_secret)

  api = tweepy.API(auth)

  def fetch(hashtag, count):
    tweets = []
    for tweet in tweepy.Cursor(Fetcher.api.search, q=hashtag).items(count):
      tweets.append(tweet._json['text'])
    return tweets

  def display(hashtag, count):
    for tweet in tweepy.Cursor(Fetcher.api.search, q=hashtag).items(count):
      print(tweet._json['text'].encode('utf-8'))