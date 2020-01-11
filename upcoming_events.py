# coding: utf-8
class UpcomingEvents():
    def __init__(self, event_id=None, vtuber_id=None, video_id=None):
        self.__event_id = event_id
        self.__vtuber_id = vtuber_id
        self.__video_id = video_id

    @property
    def event_id(self):
        return self.__event_id
    
    @event_id.setter
    def event_id(self, event_id):
        self.__event_id = event_id

    @property
    def vtuber_id(self):
        return self.__vtuber_id
    
    @vtuber_id.setter
    def vtuber_id(self, vtuber_id):
        self.__vtuber_id = vtuber_id

    @property
    def video_id(self):
        return self.__video_id
    
    @video_id.setter
    def video_id(self, video_id):
        self.__video_id = video_id