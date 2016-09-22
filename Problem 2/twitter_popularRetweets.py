import json
from collections import Counter
from prettytable import PrettyTable

popular_tweets= PrettyTable(["Count","Popular Tweets"])
with open('tweets.json','r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        #print(tweet)
        tweet_text = [tweet['text']]
        #print(terms_all)
        count_all.update(tweet_text)
    #print(count_all.most_common(10))
    x=count_all.most_common(10)
    for item in x:
        popular_tweets.add_row(item)
    popular_tweets.align["Popular Tweets"] ='l'
    popular_tweets.align["Count"]='l'
    popular_tweets._max_width["Popular Tweets"]=50
    print(popular_tweets)

    with open('popularTweets.txt','w',encoding='utf-8')as w:
        w.write(str(popular_tweets))
