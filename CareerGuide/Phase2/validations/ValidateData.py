'''
Created on Sep 10, 2015

@author: shivangi.pandey02
'''
def validate_name(input):
    count=0
    for i in input:
        if(i.isdigit() or (not i.isalpha())):
            count+=1
    if(count>1):
        return False
    else:
        return True
#print(validate_name('james@'))