import twitter

#Variables that contains the user credentials to access Twitter API 
access_token = "4330021037-7JLVKH9XB5djXVwwy0NRb08YsvFek5b1PmTnz5Q"
access_token_secret = "Rosr2YnGrJojHhewYwPAvxucMRqtLEptlsz90bHnmZE93"
consumer_key = "RWQQ1IA5FwQjejfNmeONwF7KV"
consumer_secret = "KhrjgTei67fN584fPZ3ddGTD4sDHc1LmT6egdw3fnD2DmGlTGN"

t = twitter.Twitter(auth=twitter.OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

query = t.search.tweets(q = '#cambridge', count=1000)
for stat in query['statuses']:
    print stat
