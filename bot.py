import tweepy
import time
import random

from os import environ
API_KEY = environ['API_KEY']
API_SECRET = environ['API_SECRET']
ACCESS_TOKEN = environ['ACCESS_TOKEN']
ACCESS_SECRET = environ['ACCESS_SECRET']

authenticator = tweepy.OAuthHandler(API_KEY, API_SECRET)
authenticator.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(authenticator)

terms = ["bananight", "Bananight"]
INTERVAL = 60 * 3 # tweet every 3 minutes

f = open('temas.txt', 'r')
temas = f.read().splitlines
f.close

def get_tema():
    return temas[random.randint(0, len(temas) -1)]


while True:
    for tweet in tweepy.Cursor(api.search_tweets, q = terms).items(20):
        status = api.get_status(tweet.id)
        favorited = status.favorited 
        if favorited == True:
            print("ja foi favoritado")
        else:
            api.create_favorite(tweet.id)
            print("novo tweet")
    
    for tweet in tweepy.Cursor(api.search_tweets, q = "@bananight_bot").items(10):
        repliedStatus = api.get_status(tweet.id)
        isReplied = status.favorited
        if favorited == True:
            print("Ja foi respondido")
        else:
            api.create_favorite(tweet.id)
            api.update_status("Bananight Edição " + get_tema(), tweet.id)
    api.update_status("Bananight Edição " + get_tema())
    time.sleep(INTERVAL)
