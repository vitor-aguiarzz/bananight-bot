from itertools import count
import tweepy
import time
import random
import credentials

from os import environ
API_KEY = environ['API_KEY']
API_SECRET = environ['API_SECRET']
ACCESS_TOKEN = environ['ACCESS_TOKEN']
ACCESS_SECRET = environ['ACCESS_SECRET']

authenticator = tweepy.OAuthHandler(API_KEY, API_SECRET)
authenticator.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(authenticator)

terms = ["bananight", "Bananight"]
edicao = ["Gold Edition ", "Edição Especial ", "Tema ", "Edição ", "Edição Dourada ", "Especial "]

f = open('temas.txt', 'r', encoding='utf-8')
temas = f.readlines()
f.close

def get_termo():
    return edicao[random.randint(0, len(edicao) - 1)]

def get_tema():
    tamanho = len(temas)
    return temas[random.randint(0, tamanho - 1)].rstrip()


for tweet in tweepy.Cursor(api.search_tweets, q = terms).items(20):
    status = api.get_status(tweet.id)
    retweeted = status.retweeted 
    if retweeted == True:
        print("ja foi retweetado")
    else:
        if status.favorited:
            print("ja foi curtido")
        else:
            api.create_favorite(tweet.id)
        api.retweet(tweet.id)
        print("novo tweet")
    

api.update_status(status = 'Bananight ' + get_termo() + get_tema())

