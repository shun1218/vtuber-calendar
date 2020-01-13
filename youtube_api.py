import urllib.request
import json
import ssl
import constant

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

class YoutubeAPI():
    def get_video_info(self, channel_id, page_token=None, published_after=None):
        url = 'https://www.googleapis.com/youtube/v3/search'
        params = {
            'key': constant.YOUTUBE_API_KEY,
            'part': 'id',
            'channelId': channel_id,
            'maxResults': 50,
            'order': 'date'
        }
        if page_token is not None:
            params['pageToken'] = page_token
        if published_after is not None:
            params['publishedAfter'] = published_after
        req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)))
        with urllib.request.urlopen(req, context=context) as res:
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
        with urllib.request.urlopen(req, context=context) as res:
            body = json.load(res)
            return body