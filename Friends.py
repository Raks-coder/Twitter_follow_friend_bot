import tweepy

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)
friends = sorted(api.friends_ids())

friendsFile = open("XYZ_ques1.txt","w")

friendsFile.write("Ids of the users whom I follow are :" +"\n")

ids=[]
count_ids=1

for id in friends:
    ids.append(id)
    friendsFile.write(str(count_ids)+" "+str(id) + "\n")
    count_ids+=1

friendsFile.write("Usernames of the users whom I follow are :" +"\n")

screen_names = [user.screen_name for user in api.lookup_users(user_ids=ids)]

count_names=1
for name in screen_names:
    friendsFile.write(str(count_names)+" "+name +"\n")
    count_names+=1

friendsFile.close()
