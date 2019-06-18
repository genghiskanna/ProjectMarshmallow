import tweepy
import indicoio
from statistics import mean
from preprocessor import clean
indicoio.config.api_key = '31298927fc2333c0f7659aa8bd790664'

consumer_key = 'UUB0VZCyLVjt9BqXhugUjVGxa'
consumer_secret = 'AEtKQO4Ax3hYhRo6ON4C28xfaiiDCkCoOoCiOkkCdGOvBBxzqD'
access_token = '760459013469327362-63GuahBCNJeMLgRrmtXZjWZYjntPy61'
access_token_secret = 'DnxigtVWHwjdDZMo8UnXvWC4ICFVQhuB6iwvMew2DidGF'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def calculate_sentiment(product_name, product_feature, tweet_limit):
    results = api.search(q=product_name, count=tweet_limit, lang="en")
    processed = []
    for result in results:
        print result.text
        processed.append(result.text)

    sentiments = []
    for tweets in processed:
        try:
            sentiments.append(float(indicoio.sentiment(str(clean(tweets.decode('utf-8'))))))
        except Exception as e:
            print "Tweet Exception occurred " + str(e)
    return sum(sentiments)


