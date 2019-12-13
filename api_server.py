from flask import Flask, request, jsonify
import json
import scraping

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/news/switch", methods=['GET'])
def switch():
    minutes = request.args.get("minutes", default=30)
    news = scraping.get_switch_news(minutes)
    return jsonify(news)


host_addr = "0.0.0.0"
host_port = 8080
if __name__ == "__main__":
    app.run(host=host_addr, port=host_port)
