import tweepy
import time
import credentials

authenticator = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET)
authenticator.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_SECRET)

api = tweepy.API(authenticator)
cont = 0

while (cont < 16
):
    for tweet in tweepy.Cursor(api.search_tweets, q = "bananight").items(20):
        status = api.get_status(tweet.id)
        retweeted = status.retweeted 
        if retweeted == True:
            print("ja foi retweetado")
        else:
            print("novo tweet")
    cont +=1
    print("15---", str(cont))
    time.sleep(900)
