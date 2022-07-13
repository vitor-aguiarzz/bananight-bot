from itertools import count
import tweepy
import time
import random
import credentials

from os import environ
# API_KEY = environ['API_KEY']
# API_SECRET = environ['API_SECRET']
# ACCESS_TOKEN = environ['ACCESS_TOKEN']
# ACCESS_SECRET = environ['ACCESS_SECRET']

authenticator = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET)
authenticator.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_SECRET)

api = tweepy.API(authenticator)

terms = ["bananight", "Bananight"]
INTERVAL = 60 * 3 # tweet every 3 minutes

f = open('temas.txt', 'r', encoding='utf-8')
temas = f.readlines()
f.close

def get_tema():
    print(temas)
    tamanho = len(temas)
    return temas[random.randint(0, tamanho - 1)].rstrip()


while True:
    # for tweet in tweepy.Cursor(api.search_tweets, q = terms).items(20):
    #     status = api.get_status(tweet.id)
    #     favorited = status.favorited 
    #     if favorited == True:
    #         print("ja foi favoritado")
    #     else:
    #         api.create_favorite(tweet.id)
    #         print("novo tweet")
    
    for tweet in tweepy.Cursor(api.search_tweets, q = "@bananight_bot", count = 10).items(50):
        repliedStatus = api.get_status(tweet.id)
        isReplied = repliedStatus.favorited
        if isReplied == True:
            print(tweet.text)
            break
        else:
            api.create_favorite(tweet.id)
            print(tweet.text)
            print("respondi um novo")
            api.update_status(status = ' Bananight Edição ' + get_tema(), in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
            break
    # api.update_status("Bananight Edição " + get_tema())
