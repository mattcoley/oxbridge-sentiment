import twitter
import pandas as pd
import urllib as ul
import analyze as an
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
    q = get_tweets(query,500)
    if (q['statuses'] == []):
        return pd.DataFrame()
    data = pd.DataFrame(q['statuses'])
    data = data.drop_duplicates('text')
    data['score'] = data['text'].map(lambda x : an.get_score_lang(x))
    data = data[data['score'] != 0.00]
    data['sentiment'] = data['text'].map(an.get_sentiment)
    data['retweet_count'] = data['retweet_count'].map(lambda x: cap(10,x+1))
    return data

def likeability(a):

    d = search(a)
    if d.empty:
        return (0,0,0,"","",0.0)
    number_retweets = d['retweet_count'].sum()
    d['weightedsum'] = (d['score'] * d['retweet_count']) / number_retweets
    total_score = d['weightedsum'].sum()
    d = d.sort(['score'],ascending = False)
    d = d.reset_index()
    print d
    print type(d['text'])
    most_liked = ""
    least_liked = ""
    try:
        most_liked = d['text'][0]
    except IndexError:
        most_liked = ""
    print most_liked

    d = d.sort(['score'])
    d = d.reset_index()
    try:
        least_liked = d['text'][0]
    except IndexError:
        least_liked = ""
    print d
    pos_count = len(d[d['sentiment'] == 'positive'].index)
    neg_count = len(d[d['sentiment'] == 'negative'].index)
    neu_count = len(d[d['sentiment'] == 'neutral'].index)

    print(pos_count, neg_count, most_liked,least_liked)
    return (pos_count,neg_count,neu_count,most_liked,least_liked,total_score)


def cap(a,x):
    if (x >= a):
        return a
    else:
        return x

def points(a):
    d = search(a)
    d = d.groupby(['score']).sum().reset_index()
    d['capped_retweet_count'] = d['retweet_count'].map(lambda x: cap(50,x))
    print d
    return d[['score','capped_retweet_count']].reset_index()


