from flask import Flask
from datetime import datetime
from prometheus_flask_exporter import PrometheusMetrics
import pytz

app = Flask(__name__)
metrics = PrometheusMetrics(app)
moscow_tz = pytz.timezone("Europe/Moscow")

def get_moscow_time():
    return datetime.now(moscow_tz).strftime("%H:%M:%S")

def log_visit(current_time):
    with open('logs/visits.log','a+') as f:
        f.write(current_time + '\n')

@app.route('/')
def current_time():
    moscow_time = get_moscow_time()
    log_visit(moscow_time)
    return f"<center><h1>Current time in Moscow is {moscow_time}</h1></center>"

@app.route('/visits')
def visits():
    lines = []
    with open('logs/visits.log', 'r+') as f:
        lines = [line.rstrip() for line in f]
    print(lines)
    table_str = "</td></tr><tr><td>".join(lines)
    return f"<center><table><tr><td>{table_str}</td></tr></table></center>"


if __name__ == '__main__':
    app.run('0.0.0.0')
