from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from scrape import retrieve_tweets_sentiments_and_keywords
from dotenv import load_dotenv
import os
import xgboost as xgb
import openai
import pickle
from datetime import datetime, timedelta
import pytz

openai.api_key = os.getenv("APIKEY")

app = Flask(__name__)
CORS(app)

def ask_chatgpt(question):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question}
        ]
    )

    # print(completion.choices[0].message)


    # print(answer)
    return completion.choices[0].message

@app.route("/getLiveBurnOut",methods=["POST"])
def getLiveBurnOut():
    try:
        data = request.get_json()["data"]
        model = xgb.XGBRegressor()
        model.load_model("models/burnout/xgb.txt")
        
        if data[0].lower() == "male":
            gender = 0
        else:
            gender =1
        if data[1].lower() == "no":
            wfh_setup = 0
        else:
            wfh_setup =1 
        return jsonify(
            {
                "code": 200,
                "message":  str(int(float(model.predict([[gender, wfh_setup, int(data[2]), int(data[3]), float(data[4])]])[0])*100))+"%"
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

@app.route("/getRealFakeNews",methods=["POST"])
def getRealFakeNews():
    try:
        text = request.get_json()["data"]
        logreg_filename = "models/misinformation/logreg.txt"
        logreg = pickle.load(open(logreg_filename, 'rb'))
        vectorizer = pickle.load(open("models/misinformation/vectorizer.txt", "rb"))
        fact = vectorizer.transform([text])
        pred = logreg.predict(fact)[0]
        result = "Fake"
        if pred == 0:
            result = "Real"
        return jsonify(
            {
                "code": 200,
                "message": result
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

@app.route("/getCurrentSentimentAndTopic",methods=["POST"])
def getCurrentSentimentAndTopic():
    try:
        
        # now_utc = datetime.now().tz_localize("Etc/GMT+8")

        # Convert to string in the required format
        # now_str = now_utc.strftime('%Y-%m-%d_%H:%M:%S_UTC')

        # Get the datetime object for 30 minutes before the current time
        # before_30_mins = now_utc - timedelta(minutes=30)
        # before_30_mins = before_30_mins.tz_localize("Etc/GMT+8")
        # Convert to string in the required format
        # before_30_mins_str = before_30_mins.strftime('%Y-%m-%d_%H:%M:%S_UTC')
        question = "write me a paragraph each about these topics relates to covid. "
        result = retrieve_tweets_sentiments_and_keywords(100,"Singapore")
        start = result[0]
        negative = start[start["Sentiment"] == "Negative"]
        neutral = start[start["Sentiment"] == "Neutral"]
        positive = start[start["Sentiment"] == "Positive"]
        # resampled_negative = negative.resample("W-MON").count()["Sentiment"]
        # resampled_neutral = neutral.resample("W-MON").count()["Sentiment"]
        # resampled_positive = positive.resample("W-MON").count()["Sentiment"]
        print(len(positive), len(neutral) ,len(negative))
        if len(positive)>= len(neutral) and len(positive)>= len(negative):
            overall_senti ="Positive"
        elif len(neutral)>= len(positive) and len(neutral)>= len(negative):
            overall_senti ="Neutral"
        elif len(negative)>= len(positive) and len(negative)>= len(neutral):
            overall_senti ="Negative"

        counter = 1
        for i in result[1]:
            question+=str(counter)+". "+i+" "
            counter +=1
        print(question)
        try:
            answer = ask_chatgpt(question)
            # answer = "HELLO WORLD"
        except Exception as e:
            print(e)
            answer = "Error"
        # print(answer["content"])
        answer = answer["content"]
        print(answer)
        answer = answer.replace("2.","<br/><br/>2.")
        answer = answer.replace("3.","<br/><br/>3.")
        # answer = answer.replace("\n", "<br/>")

        return jsonify(
            {
                "code": 200,
                "message": {"overallSenti":overall_senti,"topWords":result[1],"analysis":answer}
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
    # ask_chatgpt("What to do if there employees are burnout ?")
    app.run(port=5001, debug=True)

