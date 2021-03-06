'''
Created on Sep 10, 2015

@author: shivangi.pandey02
'''
from classes import ApplicantModule
from classes import AppliedJobModule
from classes import JobModule
from database import ViewDB
from exceptions import CustomExceptions
from functionality import InsertjobFunctionality
from functionality import JobsavailableFunctionality
from functionality import JobSearchFunctionality
from functionality import LoginFunctionality
from functionality import RegisterFunctionality
from functionality import updateFunctionality
from functionality import viewjobFunctionality
from utility import DBConnectivity
from validations import ValidateData
from validations import validateInput
from validations import validatePassword
from validations import ViewValidations

'''

positive test cases

'''

case1=ViewValidations.validate_job_id_wid(201)
print(case1)
case2=ViewValidations.validate_job_id_wid(211)
print(case2)
case3=ViewValidations.validate_job_id_wid('201')
print(case3)
case1=ViewValidations.validate_job_id_wid('as')
print(case1)
