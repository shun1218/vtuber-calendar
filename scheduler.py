from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from upcoming_event import UpcomingEvent

SCOPES = ['https://www.googleapis.com/auth/calendar']

creds = None
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = build('calendar', 'v3', credentials=creds)

class Scheduler():
    def insert_event(self, event, calendar_id, video_id):
        existing_event = UpcomingEvent().find_by_video_id(video_id)
        event = {
            'summary': event.summary,
            'description': event.description,
            'start': {
                'dateTime': event.start_datetime,
                'timeZone': 'Japan',
            },
            'end': {
                'dateTime': event.end_datetime,
                'timeZone': 'Japan',
            }
        }
        if existing_event.event_id:
            event = service.events().update(calendarId=calendar_id, eventId=existing_event.event_id, body=event).execute()
        else:
            event = service.events().insert(calendarId=calendar_id, body=event).execute()
        return event['id']
    
    def delete_event(self, calendar_id, event_id):
        event = service.events().delete(calendarId=calendar_id, eventId=event_id).execute()
        return