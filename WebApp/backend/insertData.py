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

createBurnoutData()