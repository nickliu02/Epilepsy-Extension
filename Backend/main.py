from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from pytube import YouTube
import json
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/check',methods = ["POST"])
def check():
    data = json.loads(request.get_data().decode('UTF-8'))
    print(data["url"])


    video = YouTube(data["url"])
    video.streams.filter(file_extension = "mp4").first().download()

    return jsonify({"ini":1})




if __name__ == '__main__':
    app.run(debug=True)

