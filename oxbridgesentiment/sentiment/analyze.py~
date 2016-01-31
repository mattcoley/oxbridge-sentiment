import urllib2 as ul
import json
import urllib
head = 'https://api.havenondemand.com/1/api/sync/analyzesentiment/v1?'
key = 'apikey=2cc4fcfa-b32a-42d9-9301-7ed9ec880379'


def format_text(s):
    s = s.encode('utf-8')
    s = urllib.quote(s)
    return "%22" + s +"%22"

def get_score(s):
    data = get_text_data(s)
    return data['aggregate']['score']


def get_sentiment(s):
    data = get_text_data(s)
    return data['aggregate']['sentiment']

def get_text_data(s):
    s = format_text(s)
    url = head + 'text=' + s + '&' + key
    print url
    result = ul.urlopen(url)
    data = json.loads(result.read())
    return data



