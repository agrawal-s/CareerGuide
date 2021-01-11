'''
Created on Sep 8, 2015

@author: Shivangi.PAndey02
'''
class Applicant:
    def __init__(self):
        self.__ap_id=None
        self.__ap_name=None
        self.__ap_pass=None
        self.__ap_skill=None
        self.__ap_exp=None
        self.__ap_tech=None
        self.__ap_gender=None
        self.__ap_contact=None

   

    def get_ap_id(self):
        return self.__ap_id


    def get_ap_name(self):
        return self.__ap_name


    def get_ap_pass(self):
        return self.__ap_pass
    
    def get_ap_skill(self):
        return self.__ap_skill


    def set_ap_skill(self, value):
        self.__ap_skill = value



    def get_ap_exp(self):
        return self.__ap_exp


    def get_ap_tech(self):
        return self.__ap_tech


    def get_ap_gender(self):
        return self.__ap_gender


    def get_ap_contact(self):
        return self.__ap_email


    def set_ap_id(self, value):
        self.__ap_id = value


    def set_ap_name(self, value):
        self.__ap_name = value


    def set_ap_pass(self, value):
        self.__ap_pass = value


    def set_ap_exp(self, value):
        self.__ap_exp = value


    def set_ap_tech(self, value):
        self.__ap_tech = value


    def set_ap_gender(self, value):
        self.__ap_gender = value


    def set_ap_contact(self, value):
        self.__ap_email = value

