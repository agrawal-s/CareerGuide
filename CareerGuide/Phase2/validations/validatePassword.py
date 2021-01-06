'''
Created on Sep 9, 2015

@author: Shivangi.PAndey02
'''
#import re
def validate_password(ap_pass):
    c_a=0
    c_1=0
    c_s=0
    for i in ap_pass:
        if(i.isdigit()):
            c_1+=1
        elif(i.isalpha()):
            c_a+=1
        else:
            c_s+=1
    if(c_1<1):
        return -1
    elif(c_a<1):
        return -2
    elif(c_s<1):
        return -3
    else:
        return 1
    
#print(validate_password('james@123'))
def validate_contact(ap_contact):
    if(len(ap_contact)==10 and ap_contact.isdigit()):
        return 1
    else:
        return -1
#