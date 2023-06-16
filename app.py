import os
import pytz
from datetime import datetime
from flask import Flask, render_template


IST = pytz.timezone('Asia/Kolkata')

app = Flask(__name__)

# to be passed from platform env
# os.environ["FLASK_ENV"]="development" 

@app.route('/')
def hello():
    curr_time = datetime.now(IST).strftime('%Y:%m:%d %H:%M:%S')
    env = os.getenv("FLASK_ENV")
    return render_template('index.html', env=env, curr_time=curr_time)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")