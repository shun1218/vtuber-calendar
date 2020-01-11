# coding: utf-8
class Event():
    def __init__(self, summary=None, description=None, start_datetime=None, end_datetime=None):
        self.__summary = summary
        self.__description = description
        self.__start_datetime = start_datetime
        self.__end_datetime = end_datetime
    
    @property
    def summary(self):
        return self.__summary
    
    @summary.setter
    def summary(self, summary):
        self.__summary = summary

    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, description):
        self.__description = description
    
    @property
    def start_datetime(self):
        return self.__start_datetime
    
    @start_datetime.setter
    def start_datetime(self, start_datetime):
        self.__start_datetime = start_datetime
    
    @property
    def end_datetime(self):
        return self.__end_datetime
    
    @end_datetime.setter
    def end_datetime(self, end_datetime):
        self.__end_datetime = end_datetime