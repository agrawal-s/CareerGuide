'''
Created on Sep 8, 2015

@author: Shivangi.PAndey02
'''
class InvalidCategoryException(Exception):
    def __init__(self):
        super().__init__("The applicant id is invalid")