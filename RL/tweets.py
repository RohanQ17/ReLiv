import snscrape.modules.twitter as tweety
import pandas as pd

query = "organ donation"
tweets = []
limit = 50
for tweet in tweety.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.content])

df = pd.DataFrame(tweets,columns= ['date','Tweet'])

print(df)

