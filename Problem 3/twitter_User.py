import tweepy
from tweepy import OAuthHandler
from prettytable import PrettyTable
import time

consumer_key = "1edf1EkmplIy7bSUR5j6ODzGu"
consumer_secret = "QDGNRSHkzES2Qrexpln5Uhj4viJ3UyJw9T0lmoC8UgG2zJaDJY"
access_token = "3856128089-RgsqT2MPPeCtSaPKXMzJMX1Y603FpDipGSZhOGf"
access_token_secret = "fdFDkN6fn68a7DUFYGB3auP8r3PVQPHAYrZiWdVYOmdwK"

if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
    auth.set_access_token(access_token, access_token_secret)

    screen_name ='USAforTrump2016'  #'USAforTrump2016'  #"MakeAmericaGre4", "TrumpVsHilary"

    user = api.get_user(screen_name)
    print('Screen Name -',user.screen_name)
    print('Description -',user.description)
    print('Followers -',user.followers_count)
    print('Status Count -',user.statuses_count)
    print('User URL -',user.url)

    # Extracting list of all friends and followers
    friends = api.friends_ids(screen_name)
    #print('Friends',friends)
    #print(len(friends))

    followers = []
    for page in tweepy.Cursor(api.followers_ids, screen_name='USAforTrump2016').pages():
        followers.extend(page)
        time.sleep(70)
    #print(len(followers),'- followers')


    friend_id = friends[1:21]
    #print(friend_id,'friend_id')
    friend_name = map(lambda x: api.get_user(x).screen_name,friend_id)
    #print(friend_name,'friend_name')

    follower_id = followers[1:21]
    #print(follower_id,'follower_id')
    follower_name = map(lambda x:api.get_user(x).screen_name,follower_id)
    #print(follower_name,'follower_name')

    # Creating a Pretty Table for top 20 Friends and Followers
    friend_pretty = PrettyTable(["id","name"])
    for item in (friend_id)[1:21]:
        friend_pretty.add_row([item,api.get_user(item).screen_name])
    print(friend_pretty)

    follower_pretty = PrettyTable(["id","name"])
    for item in (follower_id)[1:21]:
        follower_pretty.add_row([item,api.get_user(item).screen_name])
    print(follower_pretty)

    # For finding Mutual Friends
    mutual_id = set(friends).intersection(set(followers))
    #print(len(mutual_id))
    mutualFriends_pretty = PrettyTable(["id","name"])
    for item in list(mutual_id)[1:40]:
        mutualFriends_pretty.add_row([item,api.get_user(item).screen_name])
    print(mutualFriends_pretty,'mutual friends')

    # Write the Tables to a file
    #time.sleep(70)
    with open('friend.txt','w')as w:
        w.write(str(friend_pretty))

    with open('follower.txt','w')as w:
        w.write(str(follower_pretty))

    with open('mutualFriends.txt','w')as w:
        w.write(str(mutualFriends_pretty))
