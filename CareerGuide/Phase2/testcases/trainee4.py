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

case1=ViewValidations.validate_job_id(110,208)

print(case1)

case4=ViewValidations.validate_job_id(115,207)

print(case4)

#newjobsavailable.apply()

'''

negative test cases

'''

case2=ViewValidations.validate_job_id(102,201)

print(case2)

case3=ViewValidations.validate_job_id(113,208)

print(case3)

case5=ViewValidations.validate_job_id(116,208)

print(case5)

case6=ViewValidations.validate_job_id(117,208)

print(case6)