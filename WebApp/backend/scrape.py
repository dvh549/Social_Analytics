import snscrape.modules.twitter as sntwitter
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
from nltk.corpus import stopwords
stopwords = stopwords.words('english')
stopwords.extend(["&amp", "amp"])
import yake
kw_extractor = yake.KeywordExtractor(n=3, top=3, stopwords=stopwords)

def retrieve_tweets_sentiments_and_keywords(no_of_tweets, location):
    query, tweets_list = f'covid within_time:30m lang:en near:"{location}"', []
    # query, tweets_list = f'covid within_time:1d lang:en near:"{location}"', []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()): 
        if i >= no_of_tweets: # number of tweets you want to scrape
            break
        # declare the attributes to be returned
        tweets_list.append([tweet.url, tweet.date, tweet.rawContent, 
                            tweet.renderedContent, tweet.id, tweet.user])

    # create tweets df    
    tweets_df = create_df(tweets_list)

    # calculate sentiments
    calculate_sentiments(tweets_df)
    
    # get top key phrases
    top_keyphrases = get_top_keyphrases(tweets_df)

    return tweets_df, top_keyphrases
    
def create_df(tweets_list):
    tweets_df = pd.DataFrame(tweets_list, columns=['url', 'date', 'rawContent', 'renderedContent', 'id', 'user'])    
    tweets_df["date"] = pd.to_datetime(tweets_df['date'])
    tweets_df["date"] = tweets_df["date"].dt.tz_convert("Etc/GMT+8")
    dates = tweets_df["date"]
    tweets_df.index = dates
    tweets_df.drop("date", axis=1, inplace=True)
    return tweets_df

def calculate_sentiments(tweets_df):
    sentiment_scores = tweets_df['renderedContent'].apply(sid.polarity_scores)
    sentiments = sentiment_scores.apply(lambda x: x["compound"])
    sentiment_label = sentiments.apply(determine_sentiment)
    tweets_df["Sentiment"] = sentiment_label

def determine_sentiment(score):
    if score < 0:
        return "Negative"
    elif score > 0:
        return "Positive"
    else:
        return "Neutral"
    
def get_top_keyphrases(tweets_df):
    tweets = " ".join(tweets_df.renderedContent)
    return [kp[0] for kp in kw_extractor.extract_keywords(tweets)]

if __name__ == "__main__":
    print(retrieve_tweets_sentiments_and_keywords(10, "Singapore"))