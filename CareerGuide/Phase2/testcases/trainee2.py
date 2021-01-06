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


case1=ValidateData.validate_name('abcde')
print(case1)
case2=ValidateData.validate_name('Abcde')
print(case2)
case3=ValidateData.validate_name('123')
print(case3)
case4=ValidateData.validate_name('!@#@')
print(case4)
case5=validateInput.validate_exp('35')
print(case5)
case6=validateInput.validate_exp('0')
print(case6)
case7=validateInput.validate_exp('23')
print(case7)
case8=validateInput.validate_skills('')
print(case8)
case9=validateInput.validate_exp('Struts')
print(case9)



