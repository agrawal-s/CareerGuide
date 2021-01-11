'''
Created on Sep 9, 2015

@author: Shivangi.PAndey02
'''
from validations import validatePassword
from validations import ValidateData

def validate_input(ap_name,ap_pass,ap_skill,ap_exp,ap_tech,ap_gender,ap_contact):
    if(ap_name==''):
        return -1
    if(validatePassword.validate_password(ap_pass)<1):
        return -2
    if(ap_skill==''):
        return -3
    if((not ap_exp.isdigit()) or (int(ap_exp)<1 or int(ap_exp)>30)):
        return -4
    if(ap_tech==''):
        return -5
    if(ap_gender not in ['M','F']):
        return -6
    if(validatePassword.validate_contact(ap_contact)<1):
        return -7
    return 1
#print(validate_input('abc', 'james@123', 'ap_skill', 23, 'ap_tech','F','9980878078'))

def validate_exp(ap_exp):
    if((not ap_exp.isdigit()) or (int(ap_exp)<1 or int(ap_exp)>30)):
        return False
    else:
        return True
    
    
    
def validate_skills(ap_skill):
    if(ap_skill==''):
        return False
    else:
        return True
    