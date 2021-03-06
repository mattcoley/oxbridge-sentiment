import urllib2 as ul
import json
import urllib
head = 'https://api.havenondemand.com/1/api/sync/analyzesentiment/v1?'
key = 'apikey=2cc4fcfa-b32a-42d9-9301-7ed9ec880379'
head_lang_det = "https://api.havenondemand.com/1/api/sync/identifylanguage/v1?"

def format_text(s):
    s = s.encode('utf-8')
    s = urllib.quote(s)
    return "%22" + s +"%22"

def get_score(s):
    data = get_text_data(s)
    return data['aggregate']['score']

def get_score_lang(s):
    data = get_text_data_lang(s)
    return data['aggregate']['score']

def get_sentiment(s):
    data = get_text_data(s)
    return data['aggregate']['sentiment']

def get_text_data(s):
    s = format_text(s)
    url = head + 'text=' + s + '&' + key
    result = ul.urlopen(url)
    data = json.loads(result.read())
    return data

def get_text_data_lang(s):
    s = format_text(s)

    url_lang_det = head_lang_det + 'text='+ s + '&' + 'additional_metadata=false' + '&' + key
    result_lang_det = ul.urlopen(url_lang_det)
    data_lang_det = json.loads(result_lang_det.read())

    languages = ['eng','fre','spa','ger','ita','chi','por','dut','spa','rus','cze','tur','ENG','FRE','SPA','GER','ITA','CHI','POR', 'DUT','SPA','RUS','CZE','TUR']
    current_language = data_lang_det['language_iso639_2b']

    language = '';
    if current_language in languages:
        language = '&language=' + current_language

    url = head + 'text=' + s + language + '&' + key
    result = ul.urlopen(url)
    data = json.loads(result.read())

    return data


