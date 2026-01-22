from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import logging
import random
import time

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Prometheus metric
REQUEST_COUNTER = Counter('myapp_requests_total', 'Total number of requests')

@app.route('/')
def home():
    REQUEST_COUNTER.inc()
    logging.info("Home endpoint hit")
    if random.random() < 0.2:
        logging.warning("Random warning happened!")
    return "Hello, World!\n"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

