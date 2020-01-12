# coding: utf-8
from pymongo import MongoClient
import constant

url = constant.MONGO_URL
client = MongoClient(url)
db = client.vtuber
collection = db.videos

class VideoHistory():
    def get_video_details(self, channel_id):
        values = collection.find({'snippet.channelId': channel_id}, {'id': 1, '_id': 0, 'snippet.title': 1, 'snippet.publishedAt': 1, 'liveStreamingDetails': 1})
        return values

    def insert_video_details(self, value):
        if 'liveStreamingDetails' in value:
            result = collection.update({ 'id': value['id'] }, { '$set': { 'kind': value['kind'], 'etag': value['etag'], 'snippet': value['snippet'], 'liveStreamingDetails': value['liveStreamingDetails'] } }, True, False )
        else:
            result = collection.update({ 'id': value['id'] }, { '$set': { 'kind': value['kind'], 'etag': value['etag'], 'snippet': value['snippet'] } }, True, False )
        return result