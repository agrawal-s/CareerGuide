'''
Created on Sep 8, 2015

@author: shrikant.agrawal
'''
class applied_job:
    def __init__(self):
        self.__ap_id=None
        self.__job_id=None
        self.__status=None

    def get_ap_id(self):
        return self.__ap_id


    def get_job_id(self):
        return self.__job_id


    def get_status(self):
        return self.__status


    def set_ap_id(self, value):
        self.__ap_id = value


    def set_job_id(self, value):
        self.__job_id = value


    def set_status(self, value):
        self.__status = value