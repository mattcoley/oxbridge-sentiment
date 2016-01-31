import twitter
import pandas as pd
import urllib as ul
import analyze as an
import matplotlib.pyplot as plt
#Variables that contains the user credentials to access Twitter API
access_token = "4330021037-7JLVKH9XB5djXVwwy0NRb08YsvFek5b1PmTnz5Q"
access_token_secret = "Rosr2YnGrJojHhewYwPAvxucMRqtLEptlsz90bHnmZE93"
consumer_key = "RWQQ1IA5FwQjejfNmeONwF7KV"
consumer_secret = "KhrjgTei67fN584fPZ3ddGTD4sDHc1LmT6egdw3fnD2DmGlTGN"

t = twitter.Twitter(auth=twitter.OAuth(access_token, access_token_secret, consumer_key, consumer_secret))


def get_tweets(query,number):
    q = t.search.tweets(q = query, count=number)
    return q

def search(query):
    q = get_tweets(query,50)
    data = pd.DataFrame(q['statuses'])
    data = data.drop_duplicates('text')
    data['score'] = data['text'].map(lambda x : round (an.get_score(x),1))
    data = data[data['score'] != 0.00]
    data['sentiment'] = data['text'].map(an.get_sentiment)
    data['retweet_count'] = data['retweet_count'].map(lambda x: x+1)
    return data

def likeability(a):
    d = search(a)
    pos = d[d['sentiment'] == 'positive']
    pos_count = pos['retweet_count'].sum();
    neg = d[d['sentiment'] == 'negative']
    neg_count = neg['retweet_count'].sum();
    return (pos_count,neg_count)


def cap(a,x):
    if (x >= a):
        return a
    else:
        return x

def points(a):
    d = search(a)
    d = d.groupby(['score']).sum().reset_index()
    d['capped_retweet_count'] = d['retweet_count'].map(lambda x: cap(50,x))
    return d[['score','capped_retweet_count']]


