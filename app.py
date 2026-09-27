from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host="redis", port=6379, decode_responses=True)

@app.route("/")
def hello():
    count = redis.incr("counter")
    return f"Hi! You saw me {count} times."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
