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
#from validations import validate_input

#from functionality import RegisterFunctionality

'''
positive test cases
'''
case1=ValidateData.validate_name('abcde')
print(case1)
case2=ValidateData.validate_name('Abcde')
print(case2)

case10=validatePassword.validate_password('123#abc')
print(case10)
case11=validatePassword.validate_password('abc@123')
print(case11)
case12=validatePassword.validate_contact('1231231321')
print(case12)

'''
negative test cases
'''
case3=validatePassword.validate_password('abc')
print(case3)
case4=validatePassword.validate_password('123@')
print(case4)
case5=validatePassword.validate_password('abc@')
print(case5)
case6=validatePassword.validate_contact('123123132')
print(case6)
case6=validatePassword.validate_contact('12312313200')
print(case6)
case7=ValidateData.validate_name('123')
print(case7)
case8=ValidateData.validate_name('!@#@')
print(case8)
case9=validatePassword.validate_contact('12312313200aa')
print(case9)


