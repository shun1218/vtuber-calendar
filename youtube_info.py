# coding: utf-8
from youtube_api import YoutubeAPI
from video_history import VideoHistory
from event import Event
from scheduler import Scheduler
from upcoming_events import UpcomingEvents
from upcoming_event import UpcomingEvent
import datetime

class YoutubeInfo():
    def __init__(self, base_time):
        self.base_time = base_time

    def get_info(self, vtuber):
        converted_updated_at = vtuber.updated_at.strftime('%Y-%m-%dT%H:%M:%S') + '.000Z'
        video_info = YoutubeAPI().get_video_info(channel_id=vtuber.channel_id, published_after=converted_updated_at)
        updated_time = self.get_details(video_info['items'], vtuber.updated_at, vtuber.calendar_id, vtuber.vtuber_id)
        while 'nextPageToken' in video_info:
            page_token = video_info['nextPageToken']
            video_info = YoutubeAPI().get_video_info(channel_id=vtuber.channel_id, page_token=page_token)
            updated_time = self.get_details(video_info['items'], updated_time, vtuber.calendar_id, vtuber.vtuber_id)
        return updated_time
    
    def get_details(self, items, updated_time, calendar_id, vtuber_id):
        tz = datetime.timezone(datetime.timedelta(hours=9))
        video_ids = ''
        for item in items:
            if 'videoId' in item['id']:
                video_ids += item['id']['videoId']
                video_ids += ', '
        video_details = YoutubeAPI().get_video_details(video_ids[:-2])
        for video_item in video_details['items']:
            VideoHistory().insert_video_details(value=video_item)
            print(video_item['snippet']['publishedAt'], video_item['snippet']['title'])
            if 'liveStreamingDetails' in video_item:
                # スケジュール
                event = Event()
                event.summary = video_item['snippet']['title']
                event.description = 'https://www.youtube.com/watch?v=' + video_item['id']
                if 'actualEndTime' in video_item['liveStreamingDetails']:
                    start_time = datetime.datetime.fromisoformat(video_item['liveStreamingDetails']['actualStartTime'][:-1] + '+00:00')
                    end_time = datetime.datetime.fromisoformat(video_item['liveStreamingDetails']['actualEndTime'][:-1] + '+00:00')
                    # カレンダーに書き込む時間は日本時間にする
                    event.start_datetime = start_time.astimezone(tz).strftime('%Y-%m-%dT%H:%M:%S')
                    event.end_datetime = end_time.astimezone(tz).strftime('%Y-%m-%dT%H:%M:%S')
                    # 配信とアーカイブ公開の時間差が原因で重複して拾ってしまった動画はスルー
                    if end_time <= self.base_time:
                        continue
                    if end_time > updated_time:
                        updated_time = end_time
                elif 'actualStartTime' in video_item['liveStreamingDetails']:
                    start_time = datetime.datetime.fromisoformat(video_item['liveStreamingDetails']['actualStartTime'][:-1] + '+00:00')
                    end_time = start_time + datetime.timedelta(hours=1)
                    event.start_datetime = start_time.astimezone(tz).strftime('%Y-%m-%dT%H:%M:%S')
                    event.end_datetime = end_time.astimezone(tz).strftime('%Y-%m-%dT%H:%M:%S')
                else:
                    start_time = datetime.datetime.fromisoformat(video_item['liveStreamingDetails']['scheduledStartTime'][:-1] + '+00:00')
                    end_time = start_time + datetime.timedelta(hours=1)
                    event.start_datetime = start_time.astimezone(tz).strftime('%Y-%m-%dT%H:%M:%S')
                    event.end_datetime = end_time.astimezone(tz).strftime('%Y-%m-%dT%H:%M:%S')
                event_id = Scheduler().insert_event(event, calendar_id, video_item['id'])
                if not 'actualEndTime' in video_item['liveStreamingDetails']:
                    upcoming_event = UpcomingEvents()
                    upcoming_event.event_id = event_id
                    upcoming_event.vtuber_id = vtuber_id
                    upcoming_event.video_id = video_item['id']
                    UpcomingEvent().insert(upcoming_event)
        return updated_time
    
    def check_video(self, calendar_id, event_id, video_id):
        video_details = YoutubeAPI().get_video_details(video_id)
        if len(video_details['items']) == 0:
            # 削除
            Scheduler().delete_event(calendar_id, event_id)
            UpcomingEvent().delete(event_id)
        elif 'actualEndTime' in video_details['items'][0]['liveStreamingDetails']:
            UpcomingEvent().delete(event_id)
        return