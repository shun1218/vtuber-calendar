import urllib.request
import json
import constant

class YoutubeAPI():
    def get_video_info(self, channel_id, page_token='', published_after=''):
        url = 'https://www.googleapis.com/youtube/v3/search'
        params = {
            'key': constant.YOUTUBE_API_KEY,
            'part': 'id',
            'channelId': channel_id,
            'maxResults': 50,
            'order': 'date',
            'pageToken': page_token,
            'publishedAfter': published_after
        }
        req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)))
        with urllib.request.urlopen(req) as res:
            body = json.load(res)
            return body

    def get_video_details(self, video_id):
        url = 'https://www.googleapis.com/youtube/v3/videos'
        params = {
            'key': constant.YOUTUBE_API_KEY,
            'part': 'snippet, liveStreamingDetails',
            'id': video_id
        }

        req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)))
        with urllib.request.urlopen(req) as res:
            body = json.load(res)
            return body