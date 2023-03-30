import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime
# import pytz
# import tzlocal
# from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.background import BlockingScheduler
# from apscheduler.triggers.cron import CronTrigger
# from apscheduler.schedulers.blocking import BlockingScheduler
# from apscheduler.schedulers.asyncio import AsyncIOScheduler
app = Flask(__name__)
CORS(app)

def saveResult():
    return 

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(func=saveResult, trigger="cron", minute=00, timezone = 'Asia/Singapore')
    scheduler.start()
