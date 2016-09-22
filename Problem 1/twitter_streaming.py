
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import json

#Variables that contains the user credentials to access Twitter API
consumer_key = "1edf1EkmplIy7bSUR5j6ODzGu"
consumer_secret = "QDGNRSHkzES2Qrexpln5Uhj4viJ3UyJw9T0lmoC8UgG2zJaDJY"
access_token = "3856128089-RgsqT2MPPeCtSaPKXMzJMX1Y603FpDipGSZhOGf"
access_token_secret = "fdFDkN6fn68a7DUFYGB3auP8r3PVQPHAYrZiWdVYOmdwK"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        try:
            all_data = json.loads(data)
            tweet = all_data["text"]
            print(tweet)
            print(data)
            saveFile = open('tweets.json','a')
            saveFile.write(data)
            #saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException as e:
            print(('failed ondata',str(e)))
            time.sleep(5)

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'Trump2016', 'Hillary2016'
    stream.filter(track=['Trump2016', 'Hillary2016','#imwithher','#makeamericagreatagain','election2016','Donald Trump','Hillary Clinton','presidentialelections2016','donald trump','hillary clinton'])#imwithher ##makeamericagreatagain
    # g = st["text"]
    # print(g)

# Run this python file on command line to store data in .txt or .json file: ' python twitter_streaming.py > twitter_data.json '
