from flask import Flask, Markup
from flask import render_template
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler
 
import time
 
app = Flask(__name__)

'''scheduler = BackgroundScheduler({'apscheduler.timezone':'America/Los_Angeles'})
scheduler.add_job(job_function, 'interval', minutes=5)
scheduler.start()'''

def job_function():
    print("Hello World!")

@app.route('/')
def welcome():
    scheduler = BackgroundScheduler({'apscheduler.timezone':'America/Los_Angeles'})
    scheduler.add_job(job_function, 'interval', minutes=5)
    scheduler.start()
    return render_template('home.html')
  
if __name__=="__main__":
    app.run(debug=False)
