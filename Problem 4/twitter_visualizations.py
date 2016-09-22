import json
from textblob import TextBlob
from elasticsearch import Elasticsearch
# create instance of elasticsearch
es = Elasticsearch()

count = 0
with open('outfile.json','r') as f:
    #count_all = Counter()
    for line in f:
        dict_data = json.loads(line)
        #x = type(dict_data)

        #pass tweet into TextBlob
        tweet = TextBlob(dict_data["text"])
        # print(tweet)

        # output sentiment polarity
        #print (tweet.sentiment.polarity)

        #determine if sentiment is positive, negative, or neutral
        if tweet.sentiment.polarity < 0:
            sentiment = 'negative'
        elif tweet.sentiment.polarity == 0:
            sentiment = "neutral"
        else:
            sentiment = "positive"

        # output sentiment
        #print (sentiment)
        #es.put_script
        #add text and sentiment info to elasticsearch
        es.index(index="twitter",
                 doc_type="tweets",#
                 body={"author": dict_data["user"]["screen_name"],
                       "date": dict_data["created_at"],
                       "message": dict_data["text"],
                       #"geo":dict_data["geo"],
                       #"coordinates":dict_data["coordinates"],
                       "place":dict_data["place"],
                       "retweet count":dict_data["retweet_count"],
                       "favorite count":dict_data["favorite_count"],
                       #"timestamp":dict_data["timestamp_ms"],
                       "polarity": tweet.sentiment.polarity,
                       "subjectivity": tweet.sentiment.subjectivity,
                       "sentiment": sentiment,
                       "User Name":dict_data["user"]["name"],
                       "User Location":dict_data["user"]["location"],
                       "User Follower Count":dict_data["user"]["followers_count"],
                       "User Friend Count":dict_data["user"]["friends_count"],
                       "User Created Date":dict_data["user"]["created_at"],
                       "hashtags":dict_data["entities"]["hashtags"],
                       "user_mentions":dict_data["entities"]["user_mentions"],
                       "coordinates":dict_data["coordinates"]
                         }

                 )
        print("done indexing tweet")
print("COMPLETE")









        #print(dict_data)
        #line = json.loads(line)
        #terms_all = [term for term in tweet['text']]

