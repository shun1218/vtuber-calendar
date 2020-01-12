import urllib.request
import json
import constant

class YoutubeAPI():
<<<<<<< HEAD
    def get_video_info(self, channel_id, page_token=None, published_after=None):
=======
    def get_video_info(self, channel_id, page_token='', published_after=''):
>>>>>>> origin/master
        url = 'https://www.googleapis.com/youtube/v3/search'
        params = {
            'key': constant.YOUTUBE_API_KEY,
            'part': 'id',
            'channelId': channel_id,
            'maxResults': 50,
<<<<<<< HEAD
            'order': 'date'
        }
        if page_token is not None:
            params['pageToken'] = page_token
        if published_after is not None:
            params['publishedAfter'] = published_after
=======
            'order': 'date',
            'pageToken': page_token,
            'publishedAfter': published_after
        }
>>>>>>> origin/master
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