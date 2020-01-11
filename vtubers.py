# coding: utf-8
class Vtubers():
    def __init__(self, vtuber_id=None, name=None, channel_id=None, channel_title=None, calendar_id=None, updated_at=None):
        self.__vtuber_id = vtuber_id
        self.__name = name
        self.__channel_id = channel_id
        self.__channel_title = channel_title
        self.__calendar_id = calendar_id
        self.__updated_at = updated_at
    
    @property
    def vtuber_id(self):
        return self.__vtuber_id
    
    @vtuber_id.setter
    def vtuber_id(self, vtuber_id):
        self.__vtuber_id = vtuber_id

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def channel_id(self):
        return self.__channel_id
    
    @channel_id.setter
    def channel_id(self, channel_id):
        self.__channel_id = channel_id
    
    @property
    def channel_title(self):
        return self.__channel_title
    
    @channel_title.setter
    def channel_title(self, channel_title):
        self.__channel_title = channel_title

    @property
    def calendar_id(self):
        return self.__calendar_id
    
    @calendar_id.setter
    def calendar_id(self, calendar_id):
        self.__calendar_id = calendar_id
    
    @property
    def updated_at(self):
        return self.__updated_at
    
    @updated_at.setter
    def updated_at(self, updated_at):
        self.__updated_at = updated_at