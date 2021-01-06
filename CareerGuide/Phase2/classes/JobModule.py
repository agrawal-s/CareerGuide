'''
Created on Sep 8, 2015

@author: shrikant.agrawal
'''
class Job:
    def __init__(self):
        self.__job_id=None
        self.__job_name=None
        self.__pref_tech=None
        self.__skill_set=None
        self.__salary_off=None
        self.__min_exp=None
        self.__vacancy=None

    def get_job_id(self):
        return self.__job_id


    def get_job_name(self):
        return self.__app_name


    def get_pref_tech(self):
        return self.__pref_tech


    def get_skill_set(self):
        return self.__skill_set


    def get_salary_off(self):
        return self.__salary_off


    def get_min_exp(self):
        return self.__min_exp


    def get_vacancy(self):
        return self.__vacancy


    def set_job_id(self, value):
        self.__job_id = value


    def set_job_name(self, value):
        self.__app_name = value


    def set_pref_tech(self, value):
        self.__pref_tech = value


    def set_skill_set(self, value):
        self.__skill_set = value


    def set_salary_off(self, value):
        self.__salary_off = value


    def set_min_exp(self, value):
        self.__min_exp = value


    def set_vacancy(self, value):
        self.__vacancy = value