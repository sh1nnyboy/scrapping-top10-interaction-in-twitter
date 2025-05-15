import tweepy
import collections
import sys

# Twitter API credentials
# Replace these placeholders with your actual API credentials
consumer_key = 'insert your API key'
consumer_secret = 'insert your API secret'
access_token = 'insert your access token'
access_token_secret = 'insert your access token secret'

# Set up authentication with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_top_interactions(user):
    """
    Fetch and analyze the most recent tweets from a user to find the top mentioned accounts.
    
    Args:
        user (str): The Twitter username to analyze.
        
    Returns:
        list: A list of tuples containing (username, mention count) for the top 10 most mentioned users.
    """
    try:
        num_tweets = 1000  # Maximum number of tweets to analyze (Twitter API limit)
        cursor = tweepy.Cursor(api.user_timeline, screen_name=user, tweet_mode='extended', count=num_tweets)

        mentioned_users = []

        for status in cursor.items(num_tweets):
            if hasattr(status, "entities"):
                entities = status.entities
                if "user_mentions" in entities:
                    for ent in entities["user_mentions"]:
                        if "screen_name" in ent:
                            mentioned_users.append(ent["screen_name"])

        # Count occurrences of each mentioned user
        counter = collections.Counter(mentioned_users)
        # Get the top 10 most mentioned users
        top_interactions = counter.most_common(10)

        return top_interactions
    
    except tweepy.TweepyException as e:
        print(f"Error: {e}")
        return []

def main():
    # Get Twitter handle from user input
    user = input("Enter the Twitter handle to analyze (without @): ")
    
    # Remove @ symbol if user included it
    user = user.replace("@", "").strip()
    
    if not user:
        print("Error: Please enter a valid Twitter handle.")
        return
    
    print(f"\nAnalyzing @{user}'s recent tweets. This may take a moment...\n")
    
    interactions = get_top_interactions(user)
    
    if interactions:
        print(f"Top 10 accounts mentioned by @{user}:")
        for interaction in interactions:
            print(f"{interaction[0]}: {interaction[1]} mentions")
    else:
        print(f"No mentions found or unable to analyze @{user}'s tweets.")

if __name__ == "__main__":
    main()