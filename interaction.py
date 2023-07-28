import tweepy
import collections

# insert your Twitter API credentials here
consumer_key = 'insert ur api'
consumer_secret = 'insert ur api'
access_token = 'insert ur api' 
access_token_secret = 'insert ur api'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_top_interactions(user):
    num_tweets = 1000  # maximum allowed by Twitter API
    cursor = tweepy.Cursor(api.user_timeline, screen_name=user, tweet_mode='extended', count=num_tweets)

    mentioned_users = []

    for status in cursor.items(num_tweets):
        if hasattr(status, "entities"):
            entities = status.entities
            if "user_mentions" in entities:
                for ent in entities["user_mentions"]:
                    if "screen_name" in ent:
                        mentioned_users.append(ent["screen_name"])

    counter = collections.Counter(mentioned_users)
    top_interactions = counter.most_common(10)

    return top_interactions

user = "ZidanRonal"  # replace with the username you want to check
interactions = get_top_interactions(user)

for interaction in interactions:
    print(f"{interaction[0]}: {interaction[1]} mentions")

