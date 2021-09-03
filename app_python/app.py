from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)
moscow_tz = pytz.timezone("Europe/Moscow")

def get_moscow_time():
    return datetime.now(moscow_tz).strftime("%H:%M:%S")

@app.route('/')
def current_time():
    moscow_time = get_moscow_time()
    return f"<center><h1>Current time in Moscow is {moscow_time}</h1></center>"

if __name__ == '__main__':
    app.run('0.0.0.0')
