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

def preProcessingCluteringCorrelation():
    d = { "ID":[],"Name":[],"Age":[],"Occupation":[],"Gender":[],"Same_office_home_location":[],"kids":[],"RM_save_money":[],"RM_quality_time":[],"RM_better_sleep":[],"calmer_stressed":[],"RM_professional_growth":[],"RM_lazy":[],"RM_productive":[],"digital_connect_sufficient":[],"RM_better_work_life_balance":[],"RM_improved_skillset":[],"RM_job_opportunities":[], "Target":[]}
    conn = connectDB()
    cur = conn.cursor()
    cur.execute("select ID,Name,Age,Occupation,Gender,Same_office_home_location,kids,RM_save_money,RM_quality_time,RM_better_sleep,calmer_stressed,RM_professional_growth,RM_lazy,RM_productive,digital_connect_sufficient,RM_better_work_life_balance,RM_improved_skillset,RM_job_opportunities, Target from wfh_wfo;")
    output = cur.fetchall()
    conn.close()
    # print(output)
    error =[]
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


@app.route("/getBurnOut")
def Acknowledge():
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
                result[i[0]] ={i[1]:{i[2]:float(model.predict([[gender, wfh_setup, int(i[3]), int(i[4]), i[5]]])[0])}}
            else:
                if i[1] not in result[i[0]]:
                    result[i[0]][i[1]] = {i[2]: float(model.predict([[gender, wfh_setup, int(i[3]), int(i[4]), i[5]]])[0])}
                else:
                    if i[2] not in result[i[0]][i[1]]:
                        result[i[0]][i[1]][i[2]] = float(model.predict([[gender, wfh_setup, int(i[3]), int(i[4]), i[5]]])[0])
                    
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




if __name__ == '__main__':
    app.run(port=5000, debug=True)

