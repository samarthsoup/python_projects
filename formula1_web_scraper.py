import tweepy

auth = tweepy.OAuthHandler("YOUR_API_KEY", "YOUR_API_SECRET_KEY")
auth.set_access_token("YOUR_ACCESS_TOKEN", "YOUR_ACCESS_TOKEN_SECRET")

api = tweepy.API(auth)

tweets = api.user_timeline(screen_name='F1', count=10)  

for tweet in tweets:
    print(f"{tweet.created_at} - {tweet.text}\n")
