import pymysql
import uuid
from datetime import datetime
from dotenv import load_dotenv
import os
import csv
def connectDB():
    load_dotenv()
    return pymysql.connect(
        host=os.getenv("HOST"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DATABASE")
    )


def createData():
    conn = connectDB()
    # cur.execute(
    #     "INSERT INTO corona_nlp"+
    #     "(id,system_id,sub_system_id,status,failureType,failMetric, description,priority,priority_desc )"+
    #      "VALUES ("+ conn.escape(cid)+","+ conn.escape(systemInfo["system_id"])+","+ conn.escape(systemInfo["sub_system_id"])+","+ conn.escape(systemInfo["status"]) +","+ conn.escape(systemInfo["failureType"])+","+ conn.escape(systemInfo["failMetric"]) +","+ conn.escape(systemInfo["description"])+","+ conn.escape(systemInfo["priority"])+","+ conn.escape(systemInfo["priotity_desc"]) +");"  
    # )
    
    # Replace the file path and name with the location of your CSV file
    csv_file_path = "Corona_NLP_test.csv"

    # Open the CSV file

    with open(csv_file_path, newline='', encoding="ISO-8859-1", errors='replace') as csv_file:
        
        heading = next(csv_file)
        # try:
        # Create a CSV reader object
        csv_reader = csv.reader(csv_file)
        
        # Loop through each row in the CSV file
        for row in csv_reader:
            try:
                cid = str(uuid.uuid4())[:8]
                cur = conn.cursor()
                # Print each row
                # print(row[3], type(datetime.strptime(row[3] +' 00:00:00', '%d-%m-%Y %H:%M:%S')))
                cur.execute(
                    "INSERT INTO corona_nlp"+
                    "(cid,UserName,ScreenName,Location,TweetAt,OriginalTweet, Sentiment)"+
                    "VALUES ("+ conn.escape(cid)+","+ conn.escape(row[0])+","+ conn.escape(row[1])+","+ conn.escape(row[2]) +","+ conn.escape(datetime.strptime(row[3] +' 00:00:00', '%d-%m-%Y %H:%M:%S'))+","+ conn.escape(row[4]) +","+ conn.escape(row[5]) +");"  
                )
                # break
                conn.commit()
                print("done")
            except:
                print("Error")
                continue
        
            
    conn.close()

def createFakeNewsData():
    conn = connectDB()
    # cur.execute(
    #     "INSERT INTO corona_nlp"+
    #     "(id,system_id,sub_system_id,status,failureType,failMetric, description,priority,priority_desc )"+
    #      "VALUES ("+ conn.escape(cid)+","+ conn.escape(systemInfo["system_id"])+","+ conn.escape(systemInfo["sub_system_id"])+","+ conn.escape(systemInfo["status"]) +","+ conn.escape(systemInfo["failureType"])+","+ conn.escape(systemInfo["failMetric"]) +","+ conn.escape(systemInfo["description"])+","+ conn.escape(systemInfo["priority"])+","+ conn.escape(systemInfo["priotity_desc"]) +");"  
    # )
    
    # Replace the file path and name with the location of your CSV file
    csv_file_path = "fake_news.csv"

    # Open the CSV file

    with open(csv_file_path, newline='', encoding="ISO-8859-1", errors='replace') as csv_file:
        
        heading = next(csv_file)
        # try:
        # Create a CSV reader object
        csv_reader = csv.reader(csv_file)
        
        # Loop through each row in the CSV file
        for row in csv_reader:
            try:
                cid = str(uuid.uuid4())[:8]
                cur = conn.cursor()
                # Print each row
                # print(row[3], type(datetime.strptime(row[3] +' 00:00:00', '%d-%m-%Y %H:%M:%S')))
                cur.execute(
                    "INSERT INTO fake_news"+
                    "(fid,id,tweet,label)"+
                    "VALUES ("+ conn.escape(cid)+","+ conn.escape(row[0])+","+ conn.escape(row[1])+","+ conn.escape(row[2])+");"  
                )
                # break
                conn.commit()
                print("done")
            except:
                print("Error")
                continue
        
            
    conn.close()


def createBurnoutData():
    conn = connectDB()
    # cur.execute(
    #     "INSERT INTO corona_nlp"+
    #     "(id,system_id,sub_system_id,status,failureType,failMetric, description,priority,priority_desc )"+
    #      "VALUES ("+ conn.escape(cid)+","+ conn.escape(systemInfo["system_id"])+","+ conn.escape(systemInfo["sub_system_id"])+","+ conn.escape(systemInfo["status"]) +","+ conn.escape(systemInfo["failureType"])+","+ conn.escape(systemInfo["failMetric"]) +","+ conn.escape(systemInfo["description"])+","+ conn.escape(systemInfo["priority"])+","+ conn.escape(systemInfo["priotity_desc"]) +");"  
    # )
    
    # Replace the file path and name with the location of your CSV file
    csv_file_path = "burnout_train.csv"

    # Open the CSV file

    with open(csv_file_path, newline='', encoding="ISO-8859-1", errors='replace') as csv_file:
        
        heading = next(csv_file)
        # try:
        # Create a CSV reader object
        csv_reader = csv.reader(csv_file)
        
        # Loop through each row in the CSV file
        for row in csv_reader:
            try:
                cid = str(uuid.uuid4())[:8]
                cur = conn.cursor()
                # Print each row
                # print(row[3], type(datetime.strptime(row[3] +' 00:00:00', '%d-%m-%Y %H:%M:%S')))
                if row[7] =="":
                    row[7] =0
                if row[6] =="":
                    row[6] =0
                if row[5] =="":
                    row[5] =0
                cur.execute(
                    "INSERT INTO burnout"+
                    "(bid,Employee_ID,date_of_joining,gender,company_type,WFH_setup_available,designation,resource_allocation,mental_fatigue_score)"+
                    "VALUES ("+ conn.escape(cid)+","+ conn.escape(row[0])+","+ conn.escape(datetime.strptime(row[1] +' 00:00:00', '%Y-%m-%d %H:%M:%S'))+","+ conn.escape(row[2])+","+ conn.escape(row[3])+","+ conn.escape(row[4])+","+ conn.escape(row[5])+","+ conn.escape(row[6])+","+ conn.escape(row[7])+");"  
                )
                # break
                conn.commit()
                print("done")
            except Exception as e:
                print("Error: " + str(e))
                continue
        
            
    conn.close()


def createSgTweets():
    conn = connectDB()
    # cur.execute(
    #     "INSERT INTO corona_nlp"+
    #     "(id,system_id,sub_system_id,status,failureType,failMetric, description,priority,priority_desc )"+
    #      "VALUES ("+ conn.escape(cid)+","+ conn.escape(systemInfo["system_id"])+","+ conn.escape(systemInfo["sub_system_id"])+","+ conn.escape(systemInfo["status"]) +","+ conn.escape(systemInfo["failureType"])+","+ conn.escape(systemInfo["failMetric"]) +","+ conn.escape(systemInfo["description"])+","+ conn.escape(systemInfo["priority"])+","+ conn.escape(systemInfo["priotity_desc"]) +");"  
    # )
    
    # Replace the file path and name with the location of your CSV file
    csv_file_path = "coronavirus_singapore_tweets.csv"

    # Open the CSV file

    with open(csv_file_path, newline='', encoding="ISO-8859-1", errors='replace') as csv_file:
        
        heading = next(csv_file)
        # try:
        # Create a CSV reader object
        csv_reader = csv.reader(csv_file)
        
        # Loop through each row in the CSV file
        for row in csv_reader:
            try:
                cid = str(uuid.uuid4())[:8]
                cur = conn.cursor()
                # # Print each row
                # # print(row[3], type(datetime.strptime(row[3] +' 00:00:00', '%d-%m-%Y %H:%M:%S')))
                if row[7] =="":
                    row[7] =0
                if row[6] =="":
                    row[6] =0
                if row[8] =="":
                    row[8] =0
                if row[9] =="":
                    row[9] =0
                if row[27] =="":
                    row[27] =0
                # print(row, len(row))
                # break
                cur.execute(
                    "INSERT INTO corona_sg_tweets"+
                    "(sid,url,date,rawContent,renderedContent, id,user,replyCount,retweetCount,likeCount,quoteCount,converstationID,lang,source,sourceUrl,sourceLabel,links,media,retweetedTweet,quotedTweet,inReplyToTweetId,inReplyToUser,mentionedUsers,coordinates,place,hashtags,cashtags,card,viewCount,vibe)"+
                    "VALUES ("+ conn.escape(cid)+","+ conn.escape(row[0])+","+ conn.escape(datetime.strptime(row[1].split("+")[0], '%Y-%m-%d %H:%M:%S'))+","+ conn.escape(row[2])+","+ conn.escape(row[3])+","+ conn.escape(row[4])+","+ conn.escape(row[5])+","+ conn.escape(row[6])+","+ conn.escape(row[7])+","+ conn.escape(row[8])+","+ conn.escape(row[9])+","+ conn.escape(row[10])+","+ conn.escape(row[11])+","+ conn.escape(row[12])+","+ conn.escape(row[13])+","+ conn.escape(row[14])+","+ conn.escape(row[15])+","+ conn.escape(row[16])+","+ conn.escape(row[17])+","+ conn.escape(row[18])+","+ conn.escape(row[19])+","+ conn.escape(row[20])+","+ conn.escape(row[21])+","+ conn.escape(row[22])+","+ conn.escape(row[23])+","+ conn.escape(row[24])+","+ conn.escape(row[25])+","+ conn.escape(row[26])+","+ conn.escape(row[27])+","+ conn.escape(row[28])+");"  
                )
                # break
                conn.commit()
                print("done")
            except Exception as e:
                print("Error: " + str(e))
                print(row)
                continue
        
            
    conn.close()

createSgTweets()