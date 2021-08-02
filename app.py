from flask import Flask, jsonify, request
import time
import pafy
import re

app = Flask(__name__)
@app.route("/bot", method=["POST"])


#response
def response():
    query = dict(request.from)['query']
     url = "https://www.youtube.com/watch?v="+query#http://www.youtube.com/watch?v=" + search_results[0]
    video = pafy.new(url)
    print(video)
    best = video.getbestaudio()
    playurl = best.url

    result = query + " " + time.ctime()
    return jsonify({"response": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0",)

    
