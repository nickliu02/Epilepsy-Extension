import pymongo
from config import *

client = pymongo.MongoClient(DB_URI)
db = client['Data']
videos_db = db['videos']

def get_video_data(url):
    result = videos_db.find_one({ 'url': url })

    if result:
        return result['timestamps']
    else:
        return None

def add_timestamps(url, timestamps):
    result = videos_db.find_one({ 'url': url })

    if result:
        old_timestamps = result['timestamps']
        for timestamp in timestamps:
            old_timestamps.append(timestamp)

        videos_db.update_one({ 'url': url }, {'$set' : {'timestamps': old_timestamps}})
    else:
        videos_db.insert_one({
            'url': url,
            'timestamps': timestamps
        })

