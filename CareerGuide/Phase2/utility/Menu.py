'''
Created on Aug 31, 2015

@author: Kaarthikha Nataraj
'''

from functionality import RegisterFunctionality
from database import ViewDB
from functionality import LoginFunctionality
from functionality import updateFunctionality
from functionality import JobSearchFunctionality
from functionality import viewjobFunctionality
from functionality import JobsavailableFunctionality
'''
This module displays a menu to the user.
'''

print("Welcome to Career Guide")
print("=======================")
print()


end=False

while(end==False):
    print("Choose an option from below")
    print("1. Register or Login")
    print("2. Update details")
    print("3. View job status and accept offer")
    print("4. Apply for job")
    print("5. Search for jobs")
    print("6. Exit")
    option=input()
    if(option.isdigit() and (int(option)>=1 or int(option)<=6)):
        if(int(option)==1):
            print("Register or Login")
            option1=input("Press 'R' to Register. Press 'L' to Login")
            if(option1=='R' or option1=='r'):
                RegisterFunctionality.register_module()
            elif(option1=='L' or option1=='l'):
                
                ap_id=LoginFunctionality.login_module()
                #print("ap_id",ap_id)
                if(ap_id.isdigit()):
                    ViewDB.get_user(ap_id)
                
                option2=input("Would you like to update your details? Press 'Y' to update or 'N' to exit")
                if(option2=='Y' or option2=='y'):
                    updateFunctionality.update_details(ap_id)
                elif(option2=='N' or option2=='n'):
                    pass
                else:
                    print("Enter valid choice")
                
            else:
                print("Invalid option returning to the menu.")
                
        if(int(option)==2):
            print("Update details")
            login=LoginFunctionality.login_module()
            ViewDB.get_user(login)
                
            updateFunctionality.update_details(login)
            option3=input("Would you like to view or accept any applied jobs? Press 'Y' to update or 'N' to exit")
            if(option3=='Y' or option3=='y'):
                viewjobFunctionality.view_job(login)    
            elif(option3=='N' or option3=='n'):
                pass
            else:
                print("Enter valid choice")
                
        if(int(option)==3):
            print("View job status and accept offer")
            login=LoginFunctionality.login_module()
            ViewDB.get_user(login)
            viewjobFunctionality.view_job(login)
            option4=input("Would you like to apply for any job? Press 'Y' to apply or 'N' to exit")
            if(option4=='Y' or  option4=='y'):
                JobsavailableFunctionality.apply(login)    
            elif(option4=='N' or option4=='n'):
                pass
            else:
                print("Enter valid choice")
            
            
        if(int(option)==4):
            print("Apply for job")
            login=LoginFunctionality.login_module()
            ViewDB.get_user(login)
            JobsavailableFunctionality.apply(login)
        if(int(option)==5):
            print("Search for jobs")
            login=LoginFunctionality.login_module()
            ViewDB.get_user(login)
            JobSearchFunctionality.job_search()
            
        if(int(option)==6):
            print("Thank you!")
            end=True
    else:
        print("Please enter a valid option ( 1,2,3,4,5,6 )")
    