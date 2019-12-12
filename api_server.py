from flask import Flask, request
import json
import scraping

app = Flask(__name__)


@app.route("/news/switch")
def switch():
    minutes = request.args.get("minutes")
    news = scraping.get_switch_news(minutes)
    return json.dumps(news, ensure_ascii=False)


host_addr = "0.0.0.0"
host_port = 8080
if __name__ == "__main__":
    app.run(host=host_addr, port=host_port)
