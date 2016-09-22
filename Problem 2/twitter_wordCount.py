import json
import re
import operator
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from prettytable import PrettyTable

# with open('outfile.json','r') as f:
#     count_all = Counter()
#     for line in f:
#         tweet = json.loads(line)
#
#         terms_all = [term for term in tweet['text']]
#         count_all.update(terms_all)
#         #print (word_tokenize(text))
#         #do_something_else(tokens)
#     print(count_all.most_common(30))

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

# tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
# print(preprocess(tweet))

stopwords = set(stopwords.words("english")+ [
'.',',','--','\'s','?',')','(',':','\'','\'re','"','-','}','{',"https://t",'This','like','New','htt','You','us','%','To','A','ht','“','We'
u'—','','RT','…','!','?','’','I','https','Make','It','says',"Let's",'told','Happen',';','The','/','&',':/','amp','via'
])

count = 0
fname = 'tweets.json'
common_words= PrettyTable(["Count","Common Words"])
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        #words =word_tokenize(tweet['text'])
        #print(tweet['text'],"tweet text")

        #filtered_sentence = []
        #for w

        terms_all = [term for term in preprocess(tweet['text'])]
        #print(terms_all,"all terms")
        # Update the counter
        filtered_sentence = []
        for w in terms_all:
            if w not in stopwords:
                filtered_sentence.append(w)
        count_all.update(filtered_sentence)  #(terms_all)
        count += 1
        print("tokenizing tweet "+ str(count))
    # Print the first 30 most frequent words
    x=count_all.most_common(25)
    for item in x:
        common_words.add_row(item)
    common_words.align["Common Words"] ='l'
    common_words.align["Count"]='l'
    common_words._max_width["Popular Tweets"]=50
    print(common_words)

    with open('commonWords.txt','w',encoding='utf-8')as w:
        w.write(str(common_words))
