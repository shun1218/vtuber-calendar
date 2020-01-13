# coding: utf-8
import pyodbc
import constant
from upcoming_events import UpcomingEvents

server = constant.DB_SERVER
database = constant.DB_NAME
username = constant.DB_USER
password = constant.DB_PASSWORD
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

SELECT_BY_VIDEO_ID = "SELECT event_id, vtuber_id, video_id FROM upcoming_events WHERE video_id='{video_id}'"
SELECT_BY_EVENT_ID = "SELECT * FROM upcoming_events WHERE event_id='{event_id}'"
SELECT_BY_VTUBER_ID = "SELECT event_id, vtuber_id, video_id FROM upcoming_events WHERE vtuber_id={vtuber_id}"
INSERT_SQL = "INSERT INTO upcoming_events (event_id, vtuber_id, video_id) VALUES ('{event_id}', {vtuber_id}, '{video_id}')"
DELETE_BY_EVENT_ID = "DELETE FROM upcoming_events WHERE event_id='{event_id}'"

class UpcomingEvent():
    def find_by_video_id(self, video_id):
        edit_sql = SELECT_BY_VIDEO_ID.replace('{video_id}', video_id)
        upcoming_event = UpcomingEvents()
        with cursor.execute(edit_sql):
            row = cursor.fetchone()
            if row != None:
                upcoming_event.event_id = row[0]
                upcoming_event.vtuber_id = row[1]
                upcoming_event.video_id = row[2]
        return upcoming_event
    
    def find_by_vtuber_id(self, vtuber_id):
        edit_sql = SELECT_BY_VTUBER_ID.replace('{vtuber_id}', str(vtuber_id))
        upcoming_events = []
        with cursor.execute(edit_sql):
            row = cursor.fetchone()
            while row:
                upcoming_event = UpcomingEvents()
                upcoming_event.event_id = row[0]
                upcoming_event.vtuber_id = row[1]
                upcoming_event.video_id = row[2]
                upcoming_events.append(upcoming_event)
                row = cursor.fetchone()
        return upcoming_events
    
    def insert(self, upcoming_event):
        edit_sql = SELECT_BY_EVENT_ID.replace('{event_id}', upcoming_event.event_id)
        with cursor.execute(edit_sql):
            row = cursor.fetchone()
            if row == None:
                edit_sql = INSERT_SQL.replace('{event_id}', upcoming_event.event_id)
                edit_sql = edit_sql.replace('{vtuber_id}', str(upcoming_event.vtuber_id))
                edit_sql = edit_sql.replace('{video_id}', upcoming_event.video_id)
                cursor.execute(edit_sql)
                cursor.commit()
                return
        return
    
    def delete(self, event_id):
        edit_sql = DELETE_BY_EVENT_ID.replace('{event_id}', event_id)
        cursor.execute(edit_sql)
        cursor.commit()
        return