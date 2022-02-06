from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from pytube import YouTube
import json
import os
import random
import analyze
import reporting

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/check', methods=["POST"])
def check():
    data = json.loads(request.get_data().decode('UTF-8'))
    print(data["url"])

    video_data = reporting.get_video_data(data["url"])
    if video_data is not None:
        pairs = video_data
        return jsonify({'intervals': pairs})
    else:
        filename = str(random.randint(1000, 9999))
        video = YouTube(data["url"])
        video.streams.filter(file_extension="mp4").first() \
            .download(output_path="Backend/videos", filename=filename)

        pairs = analyze.analyze("Backend/videos/" + filename + ".mp4")

        reporting.add_timestamps(data["url"], pairs)

        return jsonify({'intervals': pairs})


if __name__ == '__main__':
    app.run(debug=True)
