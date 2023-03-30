import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import datetime
import pymysql
import uuid
from dotenv import load_dotenv
import os
import xgboost as xgb
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import re, string, math
import emoji
import demoji
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud, STOPWORDS
import seaborn as sns
from PIL import Image
import contractions
import nltk
from nltk.text import Text
from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import gensim
from gensim.utils import simple_preprocess
import gensim.corpora as corpora
from gensim.test.utils import datapath
from gensim.models import CoherenceModel
import pyLDAvis.gensim_models as gensimvis
import pickle 
import pyLDAvis
import pprint
import random
stopwords = set(STOPWORDS)
stopwords.add("amp")
sid = SentimentIntensityAnalyzer()
# stopwords = stopwords.words('english')
stopwords.update(["&amp", "amp"])

app = Flask(__name__)
CORS(app)

def connectDB():
    load_dotenv()
    return pymysql.connect(
        host=os.getenv("HOST"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DATABASE")
    )
def binary_map(x):
    return x.map({'Yes': 1, "No": 0})

def determine_sentiment(score):
    if score < 0:
        return "Negative"
    elif score > 0:
        return "Positive"
    else:
        return "Neutral"

# Clean emojis from text
def strip_emoji(text):
    return demoji.replace(text, '')

# Remove punctuations, links, mentions and \r\n new line characters
def strip_all_entities(text): 
    text = text.replace('\r', '').replace('\n', ' ').replace('\n', ' ').lower() # remove \n and \r and lowercase
    text = re.sub(r"(?:\@|https?\://)\S+", "", text) # remove links and mentions
    text = re.sub(r'[^\x00-\x7f]',r'', text) # remove non utf8/ascii characters such as '\x9a\x91\x97\x9a\x97'
    banned_list= string.punctuation + 'Ã'+'±'+'ã'+'¼'+'â'+'»'+'§'
    table = str.maketrans('', '', banned_list)
    text = text.translate(table)
    return text

# Clean hashtags at the end of the sentence, and keep those in the middle of the sentence by removing just the # symbol
def clean_hashtags(tweet):
    new_tweet = " ".join(word.strip() for word in re.split('#(?!(?:hashtag)\b)[\w-]+(?=(?:\s+#[\w-]+)*\s*$)', tweet)) # remove last hashtags
    new_tweet2 = " ".join(word.strip() for word in re.split('#|_', new_tweet)) # remove hashtags symbol from words in the middle of the sentence
    return new_tweet2

# Filter special characters such as & and $ present in some words
def filter_chars(a):
    sent = []
    for word in a.split(' '):
        if ('$' in word) | ('&' in word):
            sent.append('')
        else:
            sent.append(word)
    return ' '.join(sent)

def remove_mult_spaces(text): # remove multiple spaces
    return re.sub("\s\s+" , " ", text)

def clean_tweet(tweet, column):
    ## remove contractions
    tweet[column] = tweet[column].apply(lambda x: [contractions.fix(word) for word in x.split()])

    ## convert back into string so that tokenization can be done
    tweet[column] = [' '.join(map(str, l)) for l in tweet[column]]

    ## tokenize
    tweet[column] = tweet[column].apply(word_tokenize)

    ## convert tokens to lowercase
    tweet[column] = tweet[column].apply(lambda x: [word.lower() for word in x])

    ## remove punctuations and numerics
    tweet[column] = tweet[column].apply(lambda x: [word for word in x if re.search('^[a-z]+$',word)])

    ## remove stopwords
    stop_list = stopwords.words('english')
    tweet[column] = tweet[column].apply(lambda x: [word for word in x if word not in stop_list])
    
    tweet[column] = tweet[column].apply(lambda x: lemmatize_words(x))
    return tweet
                        
def lemmatize_words(text):
    return " ".join([lemmatizer.lemmatize(word) for word in text])

def processWordCloudDic(d):
    result=[]
    for key, val in d.items():
        
        try:
            temp = { "text": key, "size": int(val) }
            # temp =[key,int(val)]
        except:
            print("error")
            temp = { "name": key, "value": 0 }
            # temp =[key,0]

        result.append(temp)
    return result 

def make_bigrams(bigram_mod,texts):
    return [bigram_mod[doc] for doc in texts]

def make_trigrams(trigram_mod,bigram_mod,texts):
    return [trigram_mod[bigram_mod[doc]] for doc in texts]

def sent_to_words(sentences):
    for sentence in sentences:
        yield(simple_preprocess(str(sentence), deacc=True))

def preProcessingCluteringCorrelation():
    d = { "ID":[],"Name":[],"Age":[],"Occupation":[],"Gender":[],"Same_office_home_location":[],"kids":[],"RM_save_money":[],"RM_quality_time":[],"RM_better_sleep":[],"calmer_stressed":[],"RM_professional_growth":[],"RM_lazy":[],"RM_productive":[],"digital_connect_sufficient":[],"RM_better_work_life_balance":[],"RM_improved_skillset":[],"RM_job_opportunities":[], "Target":[]}
    conn = connectDB()
    cur = conn.cursor()
    cur.execute("select ID,Name,Age,Occupation,Gender,Same_office_home_location,kids,RM_save_money,RM_quality_time,RM_better_sleep,calmer_stressed,RM_professional_growth,RM_lazy,RM_productive,digital_connect_sufficient,RM_better_work_life_balance,RM_improved_skillset,RM_job_opportunities, Target from wfh_wfo;")
    output = cur.fetchall()
    conn.close()
    # print(output)
    for i in output:
        
        d["ID"].append(i[0])
        d["Name"] .append(i[1])
        d["Age"] .append( i[2])
        d["Occupation"] .append( i[3])
        d["Gender"] .append( i[4])
        d["Same_office_home_location"] .append( i[5])
        d["kids"] .append( i[6])
        d["RM_save_money"] .append( i[7])
        d["RM_quality_time"] .append( i[8])
        d["RM_better_sleep"] .append( i[9])
        d["calmer_stressed"] .append( i[10])
        d["RM_professional_growth"] .append( i[11])
        d["RM_lazy"] .append( i[12])
        d["RM_productive"] .append( i[13])
        d["digital_connect_sufficient"] .append( i[14])
        d["RM_better_work_life_balance"] .append( i[15])
        d["RM_improved_skillset"] .append( i[16])
        d["RM_job_opportunities"] .append( i[17])
        d["Target"] .append( i[18])
    # print("===================")
    
    # print(error)
    # print("===================")
    # for key,val in d.items():
    #     print(key+":", val, len(val))
    data = pd.DataFrame(data=d)
    # print(data)
    data2 = data.copy()
    data2['Age_group'] = pd.cut(x=data2['Age'], bins=[20, 29, 39, 49, 59], labels=["20s", "30s", "40s", "50s"])
    age_group_dummies = pd.get_dummies(data2.Age_group)
    data2 = pd.concat([data2, age_group_dummies], axis=1)
    data2.drop(["Age", "Age_group"], axis=1, inplace=True)
    gender = pd.get_dummies(data['Gender'], drop_first=True)
    calm_stress = pd.get_dummies(data['calmer_stressed'], drop_first=True)
    data2 = pd.concat([data2, gender, calm_stress], axis=1)
    data2.drop(['Gender', 'calmer_stressed'], axis=1, inplace=True)
    occupation_dummies = pd.get_dummies(data2.Occupation)
    data2 = pd.concat([data2, occupation_dummies], axis=1)
    data2.drop("Occupation", axis=1, inplace=True)
    categorical =  ['Same_office_home_location', 'kids', 'RM_save_money', 'RM_quality_time', 'RM_better_sleep', 'digital_connect_sufficient','RM_job_opportunities']
    data2[categorical] = data2[categorical].apply(binary_map)
    data2 = data2.dropna(subset=['Same_office_home_location','RM_job_opportunities'])
    data2['Same_office_home_location'] = data2['Same_office_home_location'].astype(int)
    data2['RM_job_opportunities'] = data2['RM_job_opportunities'].astype(int)
    wfh_yes = data2[data2.Target == 1].copy()
    wfh_no = data2[data2.Target == 0].copy()
    wfh_yes.drop(["ID", "Name", "Target"], axis=1, inplace=True)
    wfh_no.drop(["ID", "Name", "Target"], axis=1, inplace=True)
    km = KMeans(n_clusters = 2, random_state = 100)
    km.fit(wfh_yes)
    wfh_yes["cluster"] = km.labels_
    cluster_dummies = pd.get_dummies(wfh_yes.cluster, prefix="Cluster")
    wfh_yes = pd.concat([wfh_yes, cluster_dummies], axis=1)
    wfh_yes.drop("cluster", axis=1, inplace=True)
    km = KMeans(n_clusters = 2, random_state = 100)
    km.fit(wfh_no)
    wfh_no["cluster"] = km.labels_
    cluster_dummies = pd.get_dummies(wfh_no.cluster, prefix="Cluster")
    wfh_no = pd.concat([wfh_no, cluster_dummies], axis=1)
    wfh_no.drop("cluster", axis=1, inplace=True)
    print("here")
    corr_wfh_yes = wfh_yes.corr()
    corr_wfh_no = wfh_no.corr()
    clust_means_wfh_yes = pd.DataFrame(km.cluster_centers_, columns=wfh_yes.columns[:-2])
    clust_means_wfh_no = pd.DataFrame(km.cluster_centers_, columns=wfh_no.columns[:-2])
    
    # for i 
    # result = {}
    corr_wfh_yes_col_header = corr_wfh_yes.columns.tolist()
    corr_wfh_yes_values = corr_wfh_yes.values.tolist()
    corr_wfh_yes_cleaned =[]
    for ind, val in enumerate(corr_wfh_yes_values):
        temp = {"name": corr_wfh_yes_col_header[ind], "data":[
            {"x":corr_wfh_yes_col_header[0],"y":round(float(val[0]),2)},
            {"x":corr_wfh_yes_col_header[1],"y":round(float(val[1]),2)},
            {"x":corr_wfh_yes_col_header[2],"y":round(float(val[2]),2)},
            {"x":corr_wfh_yes_col_header[3],"y":round(float(val[3]),2)},
            {"x":corr_wfh_yes_col_header[4],"y":round(float(val[4]),2)},
            {"x":corr_wfh_yes_col_header[5],"y":round(float(val[5]),2)},
            {"x":corr_wfh_yes_col_header[6],"y":round(float(val[6]),2)},
            {"x":corr_wfh_yes_col_header[7],"y":round(float(val[7]),2)},
            {"x":corr_wfh_yes_col_header[8],"y":round(float(val[8]),2)},
            {"x":corr_wfh_yes_col_header[9],"y":round(float(val[9]),2)},
            {"x":corr_wfh_yes_col_header[10],"y":round(float(val[10]),2)},
            {"x":corr_wfh_yes_col_header[11],"y":round(float(val[11]),2)},
            {"x":corr_wfh_yes_col_header[12],"y":round(float(val[12]),2)},
            {"x":corr_wfh_yes_col_header[13],"y":round(float(val[13]),2)},
            {"x":corr_wfh_yes_col_header[14],"y":round(float(val[14]),2)},
            {"x":corr_wfh_yes_col_header[15],"y":round(float(val[15]),2)},
            {"x":corr_wfh_yes_col_header[16],"y":round(float(val[16]),2)},
            {"x":corr_wfh_yes_col_header[17],"y":round(float(val[17]),2)},
            {"x":corr_wfh_yes_col_header[18],"y":round(float(val[18]),2)},
            {"x":corr_wfh_yes_col_header[19],"y":round(float(val[19]),2)},
            {"x":corr_wfh_yes_col_header[20],"y":round(float(val[20]),2)},
            {"x":corr_wfh_yes_col_header[21],"y":round(float(val[21]),2)},
            {"x":corr_wfh_yes_col_header[22],"y":round(float(val[22]),2)},
            {"x":corr_wfh_yes_col_header[23],"y":round(float(val[23]),2)},
            {"x":corr_wfh_yes_col_header[24],"y":round(float(val[24]),2)},
            {"x":corr_wfh_yes_col_header[25],"y":round(float(val[25]),2)},
            {"x":corr_wfh_yes_col_header[26],"y":round(float(val[26]),2)}
            ]}
        corr_wfh_yes_cleaned.append(temp)
    corr_wfh_no=corr_wfh_no.replace(np.nan,0)
    corr_wfh_no_col_header = corr_wfh_no.columns.tolist()
    corr_wfh_no_values = corr_wfh_no.values.tolist()
    print(type(corr_wfh_no))
    corr_wfh_no_cleaned =[]
    for ind, val in enumerate(corr_wfh_no_values):
        temp = {"name": corr_wfh_no_col_header[ind], "data":[
            {"x":corr_wfh_no_col_header[0],"y":round(float(val[0]),2)},
            {"x":corr_wfh_no_col_header[1],"y":round(float(val[1]),2)},
            {"x":corr_wfh_no_col_header[2],"y":round(float(val[2]),2)},
            {"x":corr_wfh_no_col_header[3],"y":round(float(val[3]),2)},
            {"x":corr_wfh_no_col_header[4],"y":round(float(val[4]),2)},
            {"x":corr_wfh_no_col_header[5],"y":round(float(val[5]),2)},
            {"x":corr_wfh_no_col_header[6],"y":round(float(val[6]),2)},
            {"x":corr_wfh_no_col_header[7],"y":round(float(val[7]),2)},
            {"x":corr_wfh_no_col_header[8],"y":round(float(val[8]),2)},
            {"x":corr_wfh_no_col_header[9],"y":round(float(val[9]),2)},
            {"x":corr_wfh_no_col_header[10],"y":round(float(val[10]),2)},
            {"x":corr_wfh_no_col_header[11],"y":round(float(val[11]),2)},
            {"x":corr_wfh_no_col_header[12],"y":round(float(val[12]),2)},
            {"x":corr_wfh_no_col_header[13],"y":round(float(val[13]),2)},
            {"x":corr_wfh_no_col_header[14],"y":round(float(val[14]),2)},
            {"x":corr_wfh_no_col_header[15],"y":round(float(val[15]),2)},
            {"x":corr_wfh_no_col_header[16],"y":round(float(val[16]),2)},
            {"x":corr_wfh_no_col_header[17],"y":round(float(val[17]),2)},
            {"x":corr_wfh_no_col_header[18],"y":round(float(val[18]),2)},
            {"x":corr_wfh_no_col_header[19],"y":round(float(val[19]),2)},
            {"x":corr_wfh_no_col_header[20],"y":round(float(val[20]),2)},
            {"x":corr_wfh_no_col_header[21],"y":round(float(val[21]),2)},
            {"x":corr_wfh_no_col_header[22],"y":round(float(val[22]),2)},
            {"x":corr_wfh_no_col_header[23],"y":round(float(val[23]),2)},
            {"x":corr_wfh_no_col_header[24],"y":round(float(val[24]),2)},
            {"x":corr_wfh_no_col_header[25],"y":round(float(val[25]),2)},
            {"x":corr_wfh_no_col_header[26],"y":round(float(val[26]),2)}
            ]}
        corr_wfh_no_cleaned.append(temp)
        
        # print(temp)
        # break
    
    clust_means_wfh_yes_col_header = clust_means_wfh_yes.columns.tolist()
    clust_means_wfh_yes_values = clust_means_wfh_yes.values.tolist()
    clust_means_wfh_yes_cleaned =[]
    clusters=["Clusters 0", "Clusters 1"]
    # print(clust_means_wfh_yes_col_header)
    # print(len(clust_means_wfh_yes_col_header))
    for ind, val in enumerate(clust_means_wfh_yes_values):
        temp = {"name": clusters[ind], "data":[
            {"x":clust_means_wfh_yes_col_header[0],"y":round(float(val[0]),2)},
            {"x":clust_means_wfh_yes_col_header[1],"y":round(float(val[1]),2)},
            {"x":clust_means_wfh_yes_col_header[2],"y":round(float(val[2]),2)},
            {"x":clust_means_wfh_yes_col_header[3],"y":round(float(val[3]),2)},
            {"x":clust_means_wfh_yes_col_header[4],"y":round(float(val[4]),2)},
            {"x":clust_means_wfh_yes_col_header[5],"y":round(float(val[5]),2)},
            {"x":clust_means_wfh_yes_col_header[6],"y":round(float(val[6]),2)},
            {"x":clust_means_wfh_yes_col_header[7],"y":round(float(val[7]),2)},
            {"x":clust_means_wfh_yes_col_header[8],"y":round(float(val[8]),2)},
            {"x":clust_means_wfh_yes_col_header[9],"y":round(float(val[9]),2)},
            {"x":clust_means_wfh_yes_col_header[10],"y":round(float(val[10]),2)},
            {"x":clust_means_wfh_yes_col_header[11],"y":round(float(val[11]),2)},
            {"x":clust_means_wfh_yes_col_header[12],"y":round(float(val[12]),2)},
            {"x":clust_means_wfh_yes_col_header[13],"y":round(float(val[13]),2)},
            {"x":clust_means_wfh_yes_col_header[14],"y":round(float(val[14]),2)},
            {"x":clust_means_wfh_yes_col_header[15],"y":round(float(val[15]),2)},
            {"x":clust_means_wfh_yes_col_header[16],"y":round(float(val[16]),2)},
            {"x":clust_means_wfh_yes_col_header[17],"y":round(float(val[17]),2)},
            {"x":clust_means_wfh_yes_col_header[18],"y":round(float(val[18]),2)},
            {"x":clust_means_wfh_yes_col_header[19],"y":round(float(val[19]),2)},
            {"x":clust_means_wfh_yes_col_header[20],"y":round(float(val[20]),2)},
            {"x":clust_means_wfh_yes_col_header[21],"y":round(float(val[21]),2)},
            {"x":clust_means_wfh_yes_col_header[22],"y":round(float(val[22]),2)},
            {"x":clust_means_wfh_yes_col_header[23],"y":round(float(val[23]),2)},
            {"x":clust_means_wfh_yes_col_header[24],"y":round(float(val[24]),2)},
            ]}
        clust_means_wfh_yes_cleaned.append(temp)
    clust_means_wfh_no_col_header = clust_means_wfh_no.columns.tolist()
    clust_means_wfh_no_values = clust_means_wfh_no.values.tolist()
    clust_means_wfh_no_cleaned =[]
    # print(clust_means_wfh_yes_col_header)
    # print(len(clust_means_wfh_no_col_header))
    for ind, val in enumerate(clust_means_wfh_no_values):
        temp = {"name": clusters[ind], "data":[
            {"x":clust_means_wfh_no_col_header[0],"y":round(float(val[0]),2)},
            {"x":clust_means_wfh_no_col_header[1],"y":round(float(val[1]),2)},
            {"x":clust_means_wfh_no_col_header[2],"y":round(float(val[2]),2)},
            {"x":clust_means_wfh_no_col_header[3],"y":round(float(val[3]),2)},
            {"x":clust_means_wfh_no_col_header[4],"y":round(float(val[4]),2)},
            {"x":clust_means_wfh_no_col_header[5],"y":round(float(val[5]),2)},
            {"x":clust_means_wfh_no_col_header[6],"y":round(float(val[6]),2)},
            {"x":clust_means_wfh_no_col_header[7],"y":round(float(val[7]),2)},
            {"x":clust_means_wfh_no_col_header[8],"y":round(float(val[8]),2)},
            {"x":clust_means_wfh_no_col_header[9],"y":round(float(val[9]),2)},
            {"x":clust_means_wfh_no_col_header[10],"y":round(float(val[10]),2)},
            {"x":clust_means_wfh_no_col_header[11],"y":round(float(val[11]),2)},
            {"x":clust_means_wfh_no_col_header[12],"y":round(float(val[12]),2)},
            {"x":clust_means_wfh_no_col_header[13],"y":round(float(val[13]),2)},
            {"x":clust_means_wfh_no_col_header[14],"y":round(float(val[14]),2)},
            {"x":clust_means_wfh_no_col_header[15],"y":round(float(val[15]),2)},
            {"x":clust_means_wfh_no_col_header[16],"y":round(float(val[16]),2)},
            {"x":clust_means_wfh_no_col_header[17],"y":round(float(val[17]),2)},
            {"x":clust_means_wfh_no_col_header[18],"y":round(float(val[18]),2)},
            {"x":clust_means_wfh_no_col_header[19],"y":round(float(val[19]),2)},
            {"x":clust_means_wfh_no_col_header[20],"y":round(float(val[20]),2)},
            {"x":clust_means_wfh_no_col_header[21],"y":round(float(val[21]),2)},
            {"x":clust_means_wfh_no_col_header[22],"y":round(float(val[22]),2)},
            {"x":clust_means_wfh_no_col_header[23],"y":round(float(val[23]),2)},
            {"x":clust_means_wfh_no_col_header[24],"y":round(float(val[24]),2)},
            ]}
        clust_means_wfh_no_cleaned.append(temp)
    # print(corr_wfh_no_cleaned)
    return {"corr_yes":corr_wfh_yes_cleaned,"corr_no":corr_wfh_no_cleaned,"clust_yes":clust_means_wfh_yes_cleaned,"clust_no":clust_means_wfh_no_cleaned}
    # return {"corr_no":corr_wfh_no_cleaned}

def preprocessStartSenti(val):
    d= {"url":[],"date":[],"rawContent":[],"renderedContent":[],"id":[],"user":[],"replyCount":[],"retweetCount":[],"likeCount":[],"quoteCount":[],"converstationID":[],"lang":[],"source":[],"sourceUrl":[],"sourceLabel":[],"links":[],"media":[],"retweetedTweet":[], "quotedTweet":[],"inReplyToTweetId":[],"inReplyToUser":[],"mentionedUsers":[],"coordinates":[],"place":[],"hashtags":[],"cashtags":[],"card":[],"viewCount":[],"vibe":[]}
    conn = connectDB()
    cur = conn.cursor()
    if val =="start":
       cur.execute("SELECT url, date,rawContent,renderedContent, id, user, replyCount, retweetCount, likeCount, quoteCount, converstationID,lang, source, sourceUrl, sourceLabel, links, media, retweetedTweet, quotedTweet, inReplyToTweetId, inReplyToUser,mentionedUsers, coordinates, place,hashtags,cashtags, card, viewCount, vibe FROM sg_tweets  WHERE (date BETWEEN '2020-01-01 00:00:00' AND '2020-03-31 23:59:59') ;")
    elif val =="cb":
       cur.execute("SELECT url, date,rawContent,renderedContent, id, user, replyCount, retweetCount, likeCount, quoteCount, converstationID,lang, source, sourceUrl, sourceLabel, links, media, retweetedTweet, quotedTweet, inReplyToTweetId, inReplyToUser,mentionedUsers, coordinates, place,hashtags,cashtags, card, viewCount, vibe FROM sg_tweets  WHERE (date BETWEEN '2020-04-01 00:00:00' AND '2022-05-31 23:59:59') ;")
    elif val =="phases":
       cur.execute("SELECT url, date,rawContent,renderedContent, id, user, replyCount, retweetCount, likeCount, quoteCount, converstationID,lang, source, sourceUrl, sourceLabel, links, media, retweetedTweet, quotedTweet, inReplyToTweetId, inReplyToUser,mentionedUsers, coordinates, place,hashtags,cashtags, card, viewCount, vibe FROM sg_tweets  WHERE (date BETWEEN '2020-06-01 00:00:00' AND '2021-11-30 23:59:59') ;")
    elif val =="acutePhase":
       cur.execute("SELECT url, date,rawContent,renderedContent, id, user, replyCount, retweetCount, likeCount, quoteCount, converstationID,lang, source, sourceUrl, sourceLabel, links, media, retweetedTweet, quotedTweet, inReplyToTweetId, inReplyToUser,mentionedUsers, coordinates, place,hashtags,cashtags, card, viewCount, vibe FROM sg_tweets  WHERE (date BETWEEN '2021-12-01 00:00:00' AND '2023-01-31 23:59:59') ;")
    elif val =="green":
       cur.execute("SELECT url, date,rawContent,renderedContent, id, user, replyCount, retweetCount, likeCount, quoteCount, converstationID,lang, source, sourceUrl, sourceLabel, links, media, retweetedTweet, quotedTweet, inReplyToTweetId, inReplyToUser,mentionedUsers, coordinates, place,hashtags,cashtags, card, viewCount, vibe FROM sg_tweets  WHERE (date BETWEEN '2023-02-01 00:00:00' AND '2023-12-31 23:59:59') ;")
    
    output = cur.fetchall()
    conn.close()
    for i in output:
        d["url"].append(i[0])
        d["date"].append(i[1])
        d["rawContent"].append(i[2])
        d["renderedContent"].append(i[3])
        d["id"].append(i[4])
        d["user"].append(i[5])
        d["replyCount"].append(i[6])
        d["retweetCount"].append(i[7])
        d["likeCount"].append(i[8])
        d["quoteCount"].append(i[9])
        d["converstationID"].append(i[10])
        d["lang"].append(i[11])
        d["source"].append(i[12])
        d["sourceUrl"].append(i[13])
        d["sourceLabel"].append(i[14])
        d["links"].append(i[15])
        d["media"].append(i[16])
        d["retweetedTweet"].append(i[17])
        d["quotedTweet"].append(i[18])
        d["inReplyToTweetId"].append(i[19])
        d["inReplyToUser"].append(i[20])
        d["mentionedUsers"].append(i[21])
        d["coordinates"].append(i[22])
        d["place"].append(i[23])
        d["hashtags"].append(i[24])
        d["cashtags"].append(i[25])
        d["card"].append(i[26])
        d["viewCount"].append(i[27])
        d["vibe"].append(i[28])
    start =  pd.DataFrame(data=d)
    start["date"] = pd.to_datetime(start['date'])
    start["date"] = start["date"].dt.tz_localize("Etc/GMT+8")
    dates = start["date"]
    start.index = dates
    start.drop("date", axis=1, inplace=True)
    start["renderedContent"] = start['renderedContent'].apply(lambda tweet:str(tweet))
    sentiment_scores = start['renderedContent'].apply(sid.polarity_scores)
    sentiments = sentiment_scores.apply(lambda x: x["compound"])
    sentiment_label = sentiments.apply(determine_sentiment)
    start["Sentiment"] = sentiment_label
    negative = start[start["Sentiment"] == "Negative"]
    neutral = start[start["Sentiment"] == "Neutral"]
    positive = start[start["Sentiment"] == "Positive"]
    mask = np.array(Image.open("twitter.png"))
    #negative
    text = " ".join(tweet for tweet in negative.renderedContent)
    text = remove_mult_spaces(filter_chars(clean_hashtags(strip_all_entities(strip_emoji(text)))))
    negative_wordcloud = WordCloud(stopwords=stopwords, max_font_size=50, max_words=100, background_color="white",mask =mask,  colormap='rainbow').generate(text)
    # negative_wordcloud_d = negative_wordcloud.process_text(text)
    # negative_cleaned_wordcloud = processWordCloudDic(negative_wordcloud_d)
    #neutral
    text = " ".join(tweet for tweet in neutral.renderedContent)
    text = remove_mult_spaces(filter_chars(clean_hashtags(strip_all_entities(strip_emoji(text)))))
    neutral_wordcloud = WordCloud(stopwords=stopwords, max_font_size=50, max_words=100, background_color="white", mask =mask,  colormap='rainbow').generate(text)
    # neutral_wordcloud_d = negative_wordcloud.process_text(text)
    # neutral_cleaned_wordcloud = processWordCloudDic(neutral_wordcloud_d)

    #positive
    text = " ".join(tweet for tweet in positive.rawContent)
    text = remove_mult_spaces(filter_chars(clean_hashtags(strip_all_entities(strip_emoji(text)))))
    positive_wordcloud = WordCloud(stopwords=stopwords, max_font_size=50, max_words=100, background_color="white",mask =mask,  colormap='rainbow').generate(text)
    # positive_wordcloud_d = positive_wordcloud.process_text(text)
    # positive_cleaned_wordcloud = processWordCloudDic(positive_wordcloud_d)
    # return {"wordCloud": {"positive":positive_cleaned_wordcloud,"neutral":neutral_cleaned_wordcloud,"negative":negative_cleaned_wordcloud  }}
    if val=="start":
        negative_wordcloud.to_file("../frontend/socialanalytics/src/assets/negative_wordcloud_start.png")
        neutral_wordcloud.to_file("../frontend/socialanalytics/src/assets/neutral_wordcloud_start.png")
        positive_wordcloud.to_file("../frontend/socialanalytics/src/assets/positive_wordcloud_start.png")
    elif val=="cb":
        negative_wordcloud.to_file("../frontend/socialanalytics/src/assets/negative_wordcloud_cb.png")
        neutral_wordcloud.to_file("../frontend/socialanalytics/src/assets/neutral_wordcloud_cb.png")
        positive_wordcloud.to_file("../frontend/socialanalytics/src/assets/positive_wordcloud_cb.png")
    elif val=="phases":
        negative_wordcloud.to_file("../frontend/socialanalytics/src/assets/negative_wordcloud_phases.png")
        neutral_wordcloud.to_file("../frontend/socialanalytics/src/assets/neutral_wordcloud_phases.png")
        positive_wordcloud.to_file("../frontend/socialanalytics/src/assets/positive_wordcloud_phases.png")
    elif val=="acutePhase":
        negative_wordcloud.to_file("../frontend/socialanalytics/src/assets/negative_wordcloud_acutePhases.png")
        neutral_wordcloud.to_file("../frontend/socialanalytics/src/assets/neutral_wordcloud_acutePhases.png")
        positive_wordcloud.to_file("../frontend/socialanalytics/src/assets/positive_wordcloud_acutePhases.png")
    elif val=="green":
        negative_wordcloud.to_file("../frontend/socialanalytics/src/assets/negative_wordcloud_green.png")
        neutral_wordcloud.to_file("../frontend/socialanalytics/src/assets/neutral_wordcloud_green.png")
        positive_wordcloud.to_file("../frontend/socialanalytics/src/assets/positive_wordcloud_green.png")

    resampled_negative = negative.resample("W-MON").count()["Sentiment"]
    resampled_neutral = neutral.resample("W-MON").count()["Sentiment"]
    resampled_positive = positive.resample("W-MON").count()["Sentiment"]
    # positive_line = resampled_positive.values()
    # neutral_line = resampled_neutral.values()
    # negative_line = resampled_negative.values()
    # dateaxis = resampled_negative.index.to_numpy()
    positive_line = []
    neutral_line = []
    negative_line = [] 
    dateaxis = []
    for ind, val in resampled_positive.items():
        dateaxis.append(ind.strftime("%Y-%m-%d"))
        positive_line.append(val)
        print(int(val))
    for ind, val in resampled_neutral.items():
        neutral_line.append(val)
    for ind, val in resampled_negative.items():
        negative_line.append(val)
    print(dateaxis)
    # print(type(resampled_negative))
    print(neutral_line)
    print(negative_line)

    return {"bar_start": [ round(len(negative)/len(start)*100),round(len(neutral)/len(start)*100),round(len(positive)/len(start)*100)], "line_start":{"data":{"positive":positive_line,"neutral":neutral_line, "negative":negative_line }},"dateaxis":dateaxis}

def preprocessStartSentiUS(val):
    d= {"url":[],"date":[],"rawContent":[],"renderedContent":[],"id":[],"user":[],"replyCount":[],"retweetCount":[],"likeCount":[],"quoteCount":[],"converstationID":[],"lang":[],"source":[],"sourceUrl":[],"sourceLabel":[],"links":[],"media":[],"retweetedTweet":[], "quotedTweet":[],"inReplyToTweetId":[],"inReplyToUser":[],"mentionedUsers":[],"coordinates":[],"place":[],"hashtags":[],"cashtags":[],"card":[],"viewCount":[],"vibe":[]}
    conn = connectDB()
    cur = conn.cursor()
    if val =="start":
       cur.execute("SELECT url, date,rawContent,renderedContent, id, user, replyCount, retweetCount, likeCount, quoteCount, converstationID,lang, source, sourceUrl, sourceLabel, links, media, retweetedTweet, quotedTweet, inReplyToTweetId, inReplyToUser,mentionedUsers, coordinates, place,hashtags,cashtags, card, viewCount, vibe FROM us_tweets  WHERE (date BETWEEN '2020-01-01 00:00:00' AND '2020-03-22 23:59:59') ;")
    elif val =="cb":
       cur.execute("SELECT url, date,rawContent,renderedContent, id, user, replyCount, retweetCount, likeCount, quoteCount, converstationID,lang, source, sourceUrl, sourceLabel, links, media, retweetedTweet, quotedTweet, inReplyToTweetId, inReplyToUser,mentionedUsers, coordinates, place,hashtags,cashtags, card, viewCount, vibe FROM us_tweets  WHERE (date BETWEEN '2020-03-22 00:00:00' AND '2022-04-30 23:59:59') ;")
    elif val =="phases":
       cur.execute("SELECT url, date,rawContent,renderedContent, id, user, replyCount, retweetCount, likeCount, quoteCount, converstationID,lang, source, sourceUrl, sourceLabel, links, media, retweetedTweet, quotedTweet, inReplyToTweetId, inReplyToUser,mentionedUsers, coordinates, place,hashtags,cashtags, card, viewCount, vibe FROM us_tweets  WHERE (date BETWEEN '2020-01-01 00:00:00' AND '2020-12-31 23:59:59') ;")
    elif val =="acutePhase":
       cur.execute("SELECT url, date,rawContent,renderedContent, id, user, replyCount, retweetCount, likeCount, quoteCount, converstationID,lang, source, sourceUrl, sourceLabel, links, media, retweetedTweet, quotedTweet, inReplyToTweetId, inReplyToUser,mentionedUsers, coordinates, place,hashtags,cashtags, card, viewCount, vibe FROM us_tweets  WHERE (date BETWEEN '2021-01-01 00:00:00' AND '2021-12-31 23:59:59') ;")
    elif val =="green":
       cur.execute("SELECT url, date,rawContent,renderedContent, id, user, replyCount, retweetCount, likeCount, quoteCount, converstationID,lang, source, sourceUrl, sourceLabel, links, media, retweetedTweet, quotedTweet, inReplyToTweetId, inReplyToUser,mentionedUsers, coordinates, place,hashtags,cashtags, card, viewCount, vibe FROM us_tweets  WHERE (date BETWEEN '2022-01-01 00:00:00' AND '2022-12-31 23:59:59') ;")
    
    output = cur.fetchall()
    conn.close()
    for i in output:
        d["url"].append(i[0])
        d["date"].append(i[1])
        d["rawContent"].append(i[2])
        d["renderedContent"].append(i[3])
        d["id"].append(i[4])
        d["user"].append(i[5])
        d["replyCount"].append(i[6])
        d["retweetCount"].append(i[7])
        d["likeCount"].append(i[8])
        d["quoteCount"].append(i[9])
        d["converstationID"].append(i[10])
        d["lang"].append(i[11])
        d["source"].append(i[12])
        d["sourceUrl"].append(i[13])
        d["sourceLabel"].append(i[14])
        d["links"].append(i[15])
        d["media"].append(i[16])
        d["retweetedTweet"].append(i[17])
        d["quotedTweet"].append(i[18])
        d["inReplyToTweetId"].append(i[19])
        d["inReplyToUser"].append(i[20])
        d["mentionedUsers"].append(i[21])
        d["coordinates"].append(i[22])
        d["place"].append(i[23])
        d["hashtags"].append(i[24])
        d["cashtags"].append(i[25])
        d["card"].append(i[26])
        d["viewCount"].append(i[27])
        d["vibe"].append(i[28])
    start =  pd.DataFrame(data=d)
    start["date"] = pd.to_datetime(start['date'])
    start["date"] = start["date"].dt.tz_localize("Etc/GMT+8")
    dates = start["date"]
    start.index = dates
    start.drop("date", axis=1, inplace=True)
    start["renderedContent"] = start['renderedContent'].apply(lambda tweet:str(tweet))
    sentiment_scores = start['renderedContent'].apply(sid.polarity_scores)
    sentiments = sentiment_scores.apply(lambda x: x["compound"])
    sentiment_label = sentiments.apply(determine_sentiment)
    start["Sentiment"] = sentiment_label
    negative = start[start["Sentiment"] == "Negative"]
    neutral = start[start["Sentiment"] == "Neutral"]
    positive = start[start["Sentiment"] == "Positive"]
    mask = np.array(Image.open("twitter.png"))
    #negative
    text = " ".join(tweet for tweet in negative.renderedContent)
    text = remove_mult_spaces(filter_chars(clean_hashtags(strip_all_entities(strip_emoji(text)))))
    negative_wordcloud = WordCloud(stopwords=stopwords, max_font_size=50, max_words=100, background_color="white",mask =mask,  colormap='rainbow').generate(text)
    # negative_wordcloud_d = negative_wordcloud.process_text(text)
    # negative_cleaned_wordcloud = processWordCloudDic(negative_wordcloud_d)
    #neutral
    text = " ".join(tweet for tweet in neutral.renderedContent)
    text = remove_mult_spaces(filter_chars(clean_hashtags(strip_all_entities(strip_emoji(text)))))
    neutral_wordcloud = WordCloud(stopwords=stopwords, max_font_size=50, max_words=100, background_color="white", mask =mask,  colormap='rainbow').generate(text)
    # neutral_wordcloud_d = negative_wordcloud.process_text(text)
    # neutral_cleaned_wordcloud = processWordCloudDic(neutral_wordcloud_d)

    #positive
    text = " ".join(tweet for tweet in positive.rawContent)
    text = remove_mult_spaces(filter_chars(clean_hashtags(strip_all_entities(strip_emoji(text)))))
    positive_wordcloud = WordCloud(stopwords=stopwords, max_font_size=50, max_words=100, background_color="white",mask =mask,  colormap='rainbow').generate(text)
    # positive_wordcloud_d = positive_wordcloud.process_text(text)
    # positive_cleaned_wordcloud = processWordCloudDic(positive_wordcloud_d)
    # return {"wordCloud": {"positive":positive_cleaned_wordcloud,"neutral":neutral_cleaned_wordcloud,"negative":negative_cleaned_wordcloud  }}
    if val=="start":
        negative_wordcloud.to_file("../frontend/socialanalytics/src/assets/negative_wordcloud_start.png")
        neutral_wordcloud.to_file("../frontend/socialanalytics/src/assets/neutral_wordcloud_start.png")
        positive_wordcloud.to_file("../frontend/socialanalytics/src/assets/positive_wordcloud_start.png")
    elif val=="cb":
        negative_wordcloud.to_file("../frontend/socialanalytics/src/assets/negative_wordcloud_cb.png")
        neutral_wordcloud.to_file("../frontend/socialanalytics/src/assets/neutral_wordcloud_cb.png")
        positive_wordcloud.to_file("../frontend/socialanalytics/src/assets/positive_wordcloud_cb.png")
    elif val=="phases":
        negative_wordcloud.to_file("../frontend/socialanalytics/src/assets/negative_wordcloud_phases.png")
        neutral_wordcloud.to_file("../frontend/socialanalytics/src/assets/neutral_wordcloud_phases.png")
        positive_wordcloud.to_file("../frontend/socialanalytics/src/assets/positive_wordcloud_phases.png")
    elif val=="acutePhase":
        negative_wordcloud.to_file("../frontend/socialanalytics/src/assets/negative_wordcloud_acutePhases.png")
        neutral_wordcloud.to_file("../frontend/socialanalytics/src/assets/neutral_wordcloud_acutePhases.png")
        positive_wordcloud.to_file("../frontend/socialanalytics/src/assets/positive_wordcloud_acutePhases.png")
    elif val=="green":
        negative_wordcloud.to_file("../frontend/socialanalytics/src/assets/negative_wordcloud_green.png")
        neutral_wordcloud.to_file("../frontend/socialanalytics/src/assets/neutral_wordcloud_green.png")
        positive_wordcloud.to_file("../frontend/socialanalytics/src/assets/positive_wordcloud_green.png")

    resampled_negative = negative.resample("W-MON").count()["Sentiment"]
    resampled_neutral = neutral.resample("W-MON").count()["Sentiment"]
    resampled_positive = positive.resample("W-MON").count()["Sentiment"]
    # positive_line = resampled_positive.values()
    # neutral_line = resampled_neutral.values()
    # negative_line = resampled_negative.values()
    # dateaxis = resampled_negative.index.to_numpy()
    positive_line = []
    neutral_line = []
    negative_line = [] 
    dateaxis = []
    for ind, val in resampled_positive.items():
        dateaxis.append(ind.strftime("%Y-%m-%d"))
        positive_line.append(val)
        print(int(val))
    for ind, val in resampled_neutral.items():
        neutral_line.append(val)
    for ind, val in resampled_negative.items():
        negative_line.append(val)
    print(dateaxis)
    # print(type(resampled_negative))
    print(neutral_line)
    print(negative_line)

    return {"bar_start": [ round(len(negative)/len(start)*100),round(len(neutral)/len(start)*100),round(len(positive)/len(start)*100)], "line_start":{"data":{"positive":positive_line,"neutral":neutral_line, "negative":negative_line }},"dateaxis":dateaxis}

def preprocessTopicSg(val):
    d= {"url":[],"date":[],"rawContent":[],"renderedContent":[],"id":[],"user":[],"replyCount":[],"retweetCount":[],"likeCount":[],"quoteCount":[],"converstationID":[],"lang":[],"source":[],"sourceUrl":[],"sourceLabel":[],"links":[],"media":[],"retweetedTweet":[], "quotedTweet":[],"inReplyToTweetId":[],"inReplyToUser":[],"mentionedUsers":[],"coordinates":[],"place":[],"hashtags":[],"cashtags":[],"card":[],"viewCount":[],"vibe":[]}
    conn = connectDB()
    cur = conn.cursor()
    if val =="start":
        cur.execute("SELECT url, date,rawContent,renderedContent, id, user, replyCount, retweetCount, likeCount, quoteCount, converstationID,lang, source, sourceUrl, sourceLabel, links, media, retweetedTweet, quotedTweet, inReplyToTweetId, inReplyToUser,mentionedUsers, coordinates, place,hashtags,cashtags, card, viewCount, vibe FROM sg_tweets  WHERE (date BETWEEN '2020-01-01 00:00:00' AND '2020-03-31 23:59:59') ;")
        
        # lda_model_saved_file = datapath("models/topic/sg_start_lda_vis_tuned")
        lda_model = gensim.models.ldamodel.LdaModel.load("models/LDA models/LDA models/SG/sg_start_lda_model_18")
        num_topics= 18
    elif val =="cb":
        cur.execute("SELECT url, date,rawContent,renderedContent, id, user, replyCount, retweetCount, likeCount, quoteCount, converstationID,lang, source, sourceUrl, sourceLabel, links, media, retweetedTweet, quotedTweet, inReplyToTweetId, inReplyToUser,mentionedUsers, coordinates, place,hashtags,cashtags, card, viewCount, vibe FROM sg_tweets  WHERE (date BETWEEN '2020-04-01 00:00:00' AND '2022-05-31 23:59:59') ;")
        # lda_model_saved_file = datapath("../models/topic/sg_circuit_lda_vis_model")
        lda_model = gensim.models.ldamodel.LdaModel.load("models/LDA models/LDA models/SG/sg_circuit_lda_model_17")

        num_topics= 17

    elif val =="phases":
        cur.execute("SELECT url, date,rawContent,renderedContent, id, user, replyCount, retweetCount, likeCount, quoteCount, converstationID,lang, source, sourceUrl, sourceLabel, links, media, retweetedTweet, quotedTweet, inReplyToTweetId, inReplyToUser,mentionedUsers, coordinates, place,hashtags,cashtags, card, viewCount, vibe FROM sg_tweets  WHERE (date BETWEEN '2020-06-01 00:00:00' AND '2021-11-30 23:59:59') ;")
        # lda_model_saved_file = datapath("../models/topic/sg_phases_lda_vis_model")
        lda_model = gensim.models.ldamodel.LdaModel.load("models/LDA models/LDA models/SG/sg_phases_lda_model_11")
        num_topics= 11

    elif val =="acutePhase":
        cur.execute("SELECT url, date,rawContent,renderedContent, id, user, replyCount, retweetCount, likeCount, quoteCount, converstationID,lang, source, sourceUrl, sourceLabel, links, media, retweetedTweet, quotedTweet, inReplyToTweetId, inReplyToUser,mentionedUsers, coordinates, place,hashtags,cashtags, card, viewCount, vibe FROM sg_tweets  WHERE (date BETWEEN '2021-12-01 00:00:00' AND '2023-01-31 23:59:59') ;")
        lda_model = gensim.models.ldamodel.LdaModel.load("models/LDA models/LDA models/SG/sg_acute_lda_model_18")

        num_topics= 18

    elif val =="green":
        cur.execute("SELECT url, date,rawContent,renderedContent, id, user, replyCount, retweetCount, likeCount, quoteCount, converstationID,lang, source, sourceUrl, sourceLabel, links, media, retweetedTweet, quotedTweet, inReplyToTweetId, inReplyToUser,mentionedUsers, coordinates, place,hashtags,cashtags, card, viewCount, vibe FROM sg_tweets  WHERE (date BETWEEN '2023-02-01 00:00:00' AND '2023-12-31 23:59:59') ;")
        # lda_model_saved_file = datapath("../models/topic/sg_green_lda_vis_model")
        lda_model = gensim.models.ldamodel.LdaModel.load("models/LDA models/LDA models/SG/sg_green_lda_model_6")
        num_topics= 18


    output = cur.fetchall()
    conn.close()
    print("here")
    for i in output:
        d["url"].append(i[0])
        d["date"].append(i[1])
        d["rawContent"].append(i[2])
        d["renderedContent"].append(i[3])
        d["id"].append(i[4])
        d["user"].append(i[5])
        d["replyCount"].append(i[6])
        d["retweetCount"].append(i[7])
        d["likeCount"].append(i[8])
        d["quoteCount"].append(i[9])
        d["converstationID"].append(i[10])
        d["lang"].append(i[11])
        d["source"].append(i[12])
        d["sourceUrl"].append(i[13])
        d["sourceLabel"].append(i[14])
        d["links"].append(i[15])
        d["media"].append(i[16])
        d["retweetedTweet"].append(i[17])
        d["quotedTweet"].append(i[18])
        d["inReplyToTweetId"].append(i[19])
        d["inReplyToUser"].append(i[20])
        d["mentionedUsers"].append(i[21])
        d["coordinates"].append(i[22])
        d["place"].append(i[23])
        d["hashtags"].append(i[24])
        d["cashtags"].append(i[25])
        d["card"].append(i[26])
        d["viewCount"].append(i[27])
        d["vibe"].append(i[28])
    combined_df =  pd.DataFrame(data=d)

    combined_df['rawContent'].fillna('', inplace=True)
    combined_df['renderedContent'].fillna('', inplace=True)

    combined_df['rawContent'] = combined_df['rawContent'].str.replace('https', '')
    combined_df['rawContent'] = combined_df['rawContent'].str.replace('http', '')

    combined_df['renderedContent'] = combined_df['renderedContent'].str.replace('https', '')
    combined_df['renderedContent'] = combined_df['renderedContent'].str.replace('http', '')

    combined_df['rawContent'] = combined_df['rawContent'].str.replace('amp', '')
    combined_df['renderedContent'] = combined_df['renderedContent'].str.replace('amp', '')

    combined_df['rawContent'] = combined_df['rawContent'].str.replace('covid', '')
    combined_df['rawContent'] = combined_df['rawContent'].str.replace('coronavirus', '')

    combined_df['renderedContent'] = combined_df['renderedContent'].str.replace('covid', '')
    combined_df['renderedContent'] = combined_df['renderedContent'].str.replace('coronavirus', '')
    print("here")

    data = combined_df['renderedContent'].values.tolist()
    data_words = list(sent_to_words(data))
    # Build the bigram and trigram models
    bigram = gensim.models.Phrases(data_words, min_count=5, threshold=100) # higher threshold fewer phrases.
    trigram = gensim.models.Phrases(bigram[data_words], threshold=100)  

    # Faster way to get a sentence clubbed as a trigram/bigram
    bigram_mod = gensim.models.phrases.Phraser(bigram)
    trigram_mod = gensim.models.phrases.Phraser(trigram)

    data_words_bigrams = make_bigrams(bigram_mod,data_words)
    data_words_trigrams = make_trigrams(trigram_mod,bigram_mod,data_words)
    # Create Dictionary
    id2word = corpora.Dictionary(data_words_trigrams)

    # Create Corpus
    texts = data_words_trigrams
    print("here")
    # Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in texts]
    # score = CoherenceModel(model=lda_model, texts=data_words_trigrams, dictionary=id2word, coherence='c_v')
    # score= score.get_coherence()
    # pyLDAvis.enable_notebook()
    # vis_data = gensimvis.prepare(lda_model, corpus, id2word)
    combined_df["renderedContent"] = combined_df['renderedContent'].apply(lambda tweet:str(tweet))
    sentiment_scores = combined_df['renderedContent'].apply(sid.polarity_scores)
    # Get the topics in the LDA model
    all_topics = lda_model.print_topics()
    print(len(all_topics))
    # Print the topics
    # pprint.pprint(topics)

    print("here2")
    topics=  []
    # print(len(corpus[2165]))
    for i in range(len(corpus)):
        # print(i)
        try:
            top_topics = (lda_model.get_document_topics(corpus[i],minimum_probability=0.0))
            topic_vec = [top_topics[i][1] for i in range(num_topics)]
            topics.append(topic_vec.index(max(topic_vec))+1)
            
        except:
            # print(corpus[i])
            # print("error")
            topics.append(int(random.randint(0, num_topics-1)+1))
            continue
    print("here")
    combined_df["Topic"] = topics
    sentiments = sentiment_scores.apply(lambda x: x["compound"])
    sentiment_label = sentiments.apply(determine_sentiment)
    combined_df["Sentiment"] = sentiment_label
    print("here2")

    topics = range(1, num_topics+1)
    
    columns = ["Negative", "Positive", "Neutral"]
    data = []

    for i in range(num_topics):
        # print(i)
        curr_topic = combined_df[combined_df["Topic"] == i+1]
        negative, positive, neutral = len(curr_topic[curr_topic["Sentiment"] == "Negative"]), len(curr_topic[curr_topic["Sentiment"] == "Positive"]), len(curr_topic[curr_topic["Sentiment"] == "Neutral"]) 
        data.append([negative, positive, neutral])

    print(all_topics)
    print("here")
    topic_result = []
    for i in all_topics:
        relevant_words_arr = i[1]
        relevant_words_arr = relevant_words_arr.replace("\'",'')
        relevant_words_arr = relevant_words_arr.replace("\"",'')
        relevant_words_arr = relevant_words_arr.replace(" ",'')
        split_arr = relevant_words_arr.split("+")
        temp_arr=[]
        for j in split_arr:
            temp_arr.append(j.split("*")[1])
        temp = {"topic_no":i[0], "topic_words":",".join(temp_arr)}
        
        topic_result.append(temp)
    negative = []
    positive = []
    neutral = []
    for i in data:
        negative.append(i[0])
        positive.append(i[1])
        neutral.append(i[2])
    data = [{"name":"negative","data":negative},{"name":"positive","data":positive}, {"name":"neutral","data":neutral}]
    xaxis = [i+1 for i in range(num_topics)]

    return {"topics":topic_result,"bar_chart":data,"xaxis":xaxis }
 

def preprocessTopicUS(val):
    d= {"url":[],"date":[],"rawContent":[],"renderedContent":[],"id":[],"user":[],"replyCount":[],"retweetCount":[],"likeCount":[],"quoteCount":[],"converstationID":[],"lang":[],"source":[],"sourceUrl":[],"sourceLabel":[],"links":[],"media":[],"retweetedTweet":[], "quotedTweet":[],"inReplyToTweetId":[],"inReplyToUser":[],"mentionedUsers":[],"coordinates":[],"place":[],"hashtags":[],"cashtags":[],"card":[],"viewCount":[],"vibe":[]}
    conn = connectDB()
    cur = conn.cursor()
    if val =="start":
        cur.execute("SELECT url, date,rawContent,renderedContent, id, user, replyCount, retweetCount, likeCount, quoteCount, converstationID,lang, source, sourceUrl, sourceLabel, links, media, retweetedTweet, quotedTweet, inReplyToTweetId, inReplyToUser,mentionedUsers, coordinates, place,hashtags,cashtags, card, viewCount, vibe FROM us_tweets  WHERE (date BETWEEN '2020-01-01 00:00:00' AND '2020-03-22 23:59:59') ;")
        
        # lda_model_saved_file = datapath("models/topic/sg_start_lda_vis_tuned")
        lda_model = gensim.models.ldamodel.LdaModel.load("models/LDA models/LDA models/US/us_start_lda_model_15")
        num_topics= 15
    elif val =="cb":
        cur.execute("SELECT url, date,rawContent,renderedContent, id, user, replyCount, retweetCount, likeCount, quoteCount, converstationID,lang, source, sourceUrl, sourceLabel, links, media, retweetedTweet, quotedTweet, inReplyToTweetId, inReplyToUser,mentionedUsers, coordinates, place,hashtags,cashtags, card, viewCount, vibe FROM us_tweets  WHERE (date BETWEEN '2020-04-01 00:00:00' AND '2022-05-31 23:59:59') ;")
        # lda_model_saved_file = datapath("../models/topic/sg_circuit_lda_vis_model")
        lda_model = gensim.models.ldamodel.LdaModel.load("models/LDA models/LDA models/US/us_circuit_lda_model_11")

        num_topics= 11

    elif val =="phases":
        cur.execute("SELECT url, date,rawContent,renderedContent, id, user, replyCount, retweetCount, likeCount, quoteCount, converstationID,lang, source, sourceUrl, sourceLabel, links, media, retweetedTweet, quotedTweet, inReplyToTweetId, inReplyToUser,mentionedUsers, coordinates, place,hashtags,cashtags, card, viewCount, vibe FROM us_tweets  WHERE (date BETWEEN '2020-01-01 00:00:00' AND '2020-12-30 23:59:59') ;")
        # lda_model_saved_file = datapath("../models/topic/sg_phases_lda_vis_model")
        lda_model = gensim.models.ldamodel.LdaModel.load("models/LDA models/LDA models/US/us_2020_lda_model_7")
        num_topics= 7

    elif val =="acutePhase":
        cur.execute("SELECT url, date,rawContent,renderedContent, id, user, replyCount, retweetCount, likeCount, quoteCount, converstationID,lang, source, sourceUrl, sourceLabel, links, media, retweetedTweet, quotedTweet, inReplyToTweetId, inReplyToUser,mentionedUsers, coordinates, place,hashtags,cashtags, card, viewCount, vibe FROM us_tweets  WHERE (date BETWEEN '2021-01-01 00:00:00' AND '2022-12-31 23:59:59') ;")
        lda_model = gensim.models.ldamodel.LdaModel.load("models/LDA models/LDA models/US/us_2021_lda_model_11")
        num_topics= 11

    elif val =="green":
        cur.execute("SELECT url, date,rawContent,renderedContent, id, user, replyCount, retweetCount, likeCount, quoteCount, converstationID,lang, source, sourceUrl, sourceLabel, links, media, retweetedTweet, quotedTweet, inReplyToTweetId, inReplyToUser,mentionedUsers, coordinates, place,hashtags,cashtags, card, viewCount, vibe FROM us_tweets  WHERE (date BETWEEN '2022-01-01 00:00:00' AND '2023-12-31 23:59:59') ;")
        # lda_model_saved_file = datapath("../models/topic/sg_green_lda_vis_model")
        lda_model = gensim.models.ldamodel.LdaModel.load("models/LDA models/LDA models/US/us_2022_lda_model_19")
        num_topics= 19


    output = cur.fetchall()
    conn.close()
    print("here")
    for i in output:
        d["url"].append(i[0])
        d["date"].append(i[1])
        d["rawContent"].append(i[2])
        d["renderedContent"].append(i[3])
        d["id"].append(i[4])
        d["user"].append(i[5])
        d["replyCount"].append(i[6])
        d["retweetCount"].append(i[7])
        d["likeCount"].append(i[8])
        d["quoteCount"].append(i[9])
        d["converstationID"].append(i[10])
        d["lang"].append(i[11])
        d["source"].append(i[12])
        d["sourceUrl"].append(i[13])
        d["sourceLabel"].append(i[14])
        d["links"].append(i[15])
        d["media"].append(i[16])
        d["retweetedTweet"].append(i[17])
        d["quotedTweet"].append(i[18])
        d["inReplyToTweetId"].append(i[19])
        d["inReplyToUser"].append(i[20])
        d["mentionedUsers"].append(i[21])
        d["coordinates"].append(i[22])
        d["place"].append(i[23])
        d["hashtags"].append(i[24])
        d["cashtags"].append(i[25])
        d["card"].append(i[26])
        d["viewCount"].append(i[27])
        d["vibe"].append(i[28])
    combined_df =  pd.DataFrame(data=d)

    combined_df['rawContent'].fillna('', inplace=True)
    combined_df['renderedContent'].fillna('', inplace=True)

    combined_df['rawContent'] = combined_df['rawContent'].str.replace('https', '')
    combined_df['rawContent'] = combined_df['rawContent'].str.replace('http', '')

    combined_df['renderedContent'] = combined_df['renderedContent'].str.replace('https', '')
    combined_df['renderedContent'] = combined_df['renderedContent'].str.replace('http', '')

    combined_df['rawContent'] = combined_df['rawContent'].str.replace('amp', '')
    combined_df['renderedContent'] = combined_df['renderedContent'].str.replace('amp', '')

    combined_df['rawContent'] = combined_df['rawContent'].str.replace('covid', '')
    combined_df['rawContent'] = combined_df['rawContent'].str.replace('coronavirus', '')

    combined_df['renderedContent'] = combined_df['renderedContent'].str.replace('covid', '')
    combined_df['renderedContent'] = combined_df['renderedContent'].str.replace('coronavirus', '')
    print("here")

    data = combined_df['renderedContent'].values.tolist()
    data_words = list(sent_to_words(data))
    # Build the bigram and trigram models
    bigram = gensim.models.Phrases(data_words, min_count=5, threshold=100) # higher threshold fewer phrases.
    trigram = gensim.models.Phrases(bigram[data_words], threshold=100)  

    # Faster way to get a sentence clubbed as a trigram/bigram
    bigram_mod = gensim.models.phrases.Phraser(bigram)
    trigram_mod = gensim.models.phrases.Phraser(trigram)

    data_words_bigrams = make_bigrams(bigram_mod,data_words)
    data_words_trigrams = make_trigrams(trigram_mod,bigram_mod,data_words)
    # Create Dictionary
    id2word = corpora.Dictionary(data_words_trigrams)

    # Create Corpus
    texts = data_words_trigrams
    print("here")
    # Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in texts]
    # score = CoherenceModel(model=lda_model, texts=data_words_trigrams, dictionary=id2word, coherence='c_v')
    # score= score.get_coherence()
    # pyLDAvis.enable_notebook()
    # vis_data = gensimvis.prepare(lda_model, corpus, id2word)
    combined_df["renderedContent"] = combined_df['renderedContent'].apply(lambda tweet:str(tweet))
    sentiment_scores = combined_df['renderedContent'].apply(sid.polarity_scores)
    # Get the topics in the LDA model
    all_topics = lda_model.print_topics()
    print(len(all_topics))
    # Print the topics
    # pprint.pprint(topics)

    print("here2")
    topics=  []
    # print(len(corpus[2165]))
    for i in range(len(corpus)):
        # print(i)
        try:
            top_topics = (lda_model.get_document_topics(corpus[i],minimum_probability=0.0))
            topic_vec = [top_topics[i][1] for i in range(num_topics)]
            topics.append(topic_vec.index(max(topic_vec))+1)
            
        except:
            # print(corpus[i])
            # print("error")
            topics.append(int(random.randint(0, num_topics-1)+1))
            continue
    print("here")
    combined_df["Topic"] = topics
    sentiments = sentiment_scores.apply(lambda x: x["compound"])
    sentiment_label = sentiments.apply(determine_sentiment)
    combined_df["Sentiment"] = sentiment_label
    print("here2")

    topics = range(1, num_topics+1)
    
    columns = ["Negative", "Positive", "Neutral"]
    data = []

    for i in range(num_topics):
        # print(i)
        curr_topic = combined_df[combined_df["Topic"] == i+1]
        negative, positive, neutral = len(curr_topic[curr_topic["Sentiment"] == "Negative"]), len(curr_topic[curr_topic["Sentiment"] == "Positive"]), len(curr_topic[curr_topic["Sentiment"] == "Neutral"]) 
        data.append([negative, positive, neutral])

    print(all_topics)
    print("here")
    topic_result = []
    for i in all_topics:
        relevant_words_arr = i[1]
        relevant_words_arr = relevant_words_arr.replace("\'",'')
        relevant_words_arr = relevant_words_arr.replace("\"",'')
        relevant_words_arr = relevant_words_arr.replace(" ",'')
        split_arr = relevant_words_arr.split("+")
        temp_arr=[]
        for j in split_arr:
            temp_arr.append(j.split("*")[1])
        temp = {"topic_no":i[0], "topic_words":",".join(temp_arr)}
        
        topic_result.append(temp)
    negative = []
    positive = []
    neutral = []
    for i in data:
        negative.append(i[0])
        positive.append(i[1])
        neutral.append(i[2])
    data = [{"name":"negative","data":negative},{"name":"positive","data":positive}, {"name":"neutral","data":neutral}]
    xaxis = [i+1 for i in range(num_topics)]

    return {"topics":topic_result,"bar_chart":data,"xaxis":xaxis }
 

@app.route("/getBurnOut")
def getBurnOut():
    try:
        result = {}
        #Get Data
        conn = connectDB()
        cur = conn.cursor()
        cur.execute("select gender, company_type,WFH_setup_available,avg(designation),avg(resource_allocation),avg(mental_fatigue_score) from burnout group by gender, company_type , WFH_setup_available;")
        output = cur.fetchall()
        conn.close()
        # with open(r'models\burnout\xgb.pkl','rb') as f:
        #     model = pickle.load(f)
        #predict using model
        model = xgb.XGBRegressor()
        model.load_model("models/burnout/xgb.txt")
        for i in output:
            if i[0].lower() == "male":
                gender = 0
            else:
                gender =1
            if i[2].lower() == "no":
                wfh_setup = 0
            else:
                wfh_setup =1 
            # print(model.predict([[gender, wfh_setup, i[3], i[4], i[5]]]))
            if i[0] not in result:
                result[i[0]] ={i[1]:{i[2]: str(int(float(model.predict([[gender, wfh_setup, int(i[3]), int(i[4]), i[5]]])[0])*100))+"%"}}
            else:
                if i[1] not in result[i[0]]:
                    result[i[0]][i[1]] = {i[2]: str(int(float(model.predict([[gender, wfh_setup, int(i[3]), int(i[4]), i[5]]])[0])*100))+"%"}
                else:
                    if i[2] not in result[i[0]][i[1]]:
                        result[i[0]][i[1]][i[2]] = str(int(float(model.predict([[gender, wfh_setup, int(i[3]), int(i[4]), i[5]]])[0])*100))+"%"
                    
        return jsonify(
            {
                "code": 200,
                "message":  result
            }
        ), 200
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 500,
                "message": "server error"
            }
        ), 500
    
@app.route("/getClustering")
def getCluster():
    try:
        print(type(preProcessingCluteringCorrelation()))

        return jsonify(
            {
                "code": 200,
                "message": preProcessingCluteringCorrelation()
            }
        ), 200
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 500,
                "message": "server error"
            }
        ), 500

@app.route("/getSentimentAnalysisStart")
def getSentimentAnalysis():
    try:
        return jsonify(
            {
                "code": 200,
                "message": preprocessStartSenti("start")
            }
        ), 200
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 500,
                "message": "server error"
            }
        ), 500

@app.route("/getSentimentAnalysisCB")
def getSentimentAnalysisCB():
    try:
        return jsonify(
            {
                "code": 200,
                "message": preprocessStartSenti("cb")
            }
        ), 200
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 500,
                "message": "server error"
            }
        ), 500

@app.route("/getSentimentAnalysisPhases")
def getSentimentAnalysisPhases():
    try:
        return jsonify(
            {
                "code": 200,
                "message": preprocessStartSenti("phases")
            }
        ), 200
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 500,
                "message": "server error"
            }
        ), 500

@app.route("/getSentimentAnalysisAcutePhase")
def getSentimentAnalysisAcutePhase():
    try:
        return jsonify(
            {
                "code": 200,
                "message": preprocessStartSenti("acutePhase")
            }
        ), 200
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 500,
                "message": "server error"
            }
        ), 500

@app.route("/getSentimentAnalysisGreen")
def getSentimentAnalysisGreen():
    try:
        return jsonify(
            {
                "code": 200,
                "message": preprocessStartSenti("green")
            }
        ), 200
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 500,
                "message": "server error"
            }
        ), 500


@app.route("/getSentimentAnalysisStartUS")
def getSentimentAnalysisUS():
    try:
        return jsonify(
            {
                "code": 200,
                "message": preprocessStartSentiUS("start")
            }
        ), 200
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 500,
                "message": "server error"
            }
        ), 500

@app.route("/getSentimentAnalysisCBUS")
def getSentimentAnalysisCBUS():
    try:
        return jsonify(
            {
                "code": 200,
                "message": preprocessStartSentiUS("cb")
            }
        ), 200
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 500,
                "message": "server error"
            }
        ), 500

@app.route("/getSentimentAnalysisPhasesUS")
def getSentimentAnalysisPhasesUS():
    try:
        return jsonify(
            {
                "code": 200,
                "message": preprocessStartSentiUS("phases")
            }
        ), 200
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 500,
                "message": "server error"
            }
        ), 500

@app.route("/getSentimentAnalysisAcutePhaseUS")
def getSentimentAnalysisAcutePhaseUS():
    try:
        return jsonify(
            {
                "code": 200,
                "message": preprocessStartSentiUS("acutePhase")
            }
        ), 200
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 500,
                "message": "server error"
            }
        ), 500

@app.route("/getSentimentAnalysisGreenUS")
def getSentimentAnalysisGreenUS():
    try:
        return jsonify(
            {
                "code": 200,
                "message": preprocessStartSentiUS("green")
            }
        ), 200
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 500,
                "message": "server error"
            }
        ), 500

@app.route("/getTopicStart")
def getTopicStart():
    try:
        return jsonify(
            {
                "code": 200,
                "message": preprocessTopicSg("start")
            }
        ), 200
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 500,
                "message": "server error"
            }
        ), 500

@app.route("/getTopicCB")
def getTopicCB():
    try:
        return jsonify(
            {
                "code": 200,
                "message": preprocessTopicSg("cb")
            }
        ), 200
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 500,
                "message": "server error"
            }
        ), 500

@app.route("/getTopicPhases")
def getTopicPhases():
    try:
        return jsonify(
            {
                "code": 200,
                "message": preprocessTopicSg("phases")
            }
        ), 200
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 500,
                "message": "server error"
            }
        ), 500

@app.route("/getTopicAcute")
def getTopicAcute():
    try:
        return jsonify(
            {
                "code": 200,
                "message": preprocessTopicSg("acutePhase")
            }
        ), 200
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 500,
                "message": "server error"
            }
        ), 500

@app.route("/getTopicGreen")
def getTopicGreen():
    try:
        return jsonify(
            {
                "code": 200,
                "message": preprocessTopicSg("green")
            }
        ), 200
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 500,
                "message": "server error"
            }
        ), 500


@app.route("/getTopicStartUS")
def getTopicStartUS():
    try:
        return jsonify(
            {
                "code": 200,
                "message": preprocessTopicUS("start")
            }
        ), 200
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 500,
                "message": "server error"
            }
        ), 500

@app.route("/getTopicCBUS")
def getTopicCBUS():
    try:
        return jsonify(
            {
                "code": 200,
                "message": preprocessTopicUS("cb")
            }
        ), 200
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 500,
                "message": "server error"
            }
        ), 500

@app.route("/getTopicPhasesUS")
def getTopicPhasesUS():
    try:
        return jsonify(
            {
                "code": 200,
                "message": preprocessTopicUS("phases")
            }
        ), 200
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 500,
                "message": "server error"
            }
        ), 500

@app.route("/getTopicAcuteUS")
def getTopicAcuteUS():
    try:
        return jsonify(
            {
                "code": 200,
                "message": preprocessTopicUS("acutePhase")
            }
        ), 200
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 500,
                "message": "server error"
            }
        ), 500

@app.route("/getTopicGreenUS")
def getTopicGreenUS():
    try:
        return jsonify(
            {
                "code": 200,
                "message": preprocessTopicUS("green")
            }
        ), 200
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 500,
                "message": "server error"
            }
        ), 500


if __name__ == '__main__':
    app.run(port=5000, debug=True)

