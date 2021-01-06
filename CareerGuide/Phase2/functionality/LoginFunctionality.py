'''
Created on Sep 10, 2015

@author: shivangi.pandey02
'''

from database import ViewDB
#from functionality import updateModule
def login_module():
    end=False
    while(end==False):
        ap_id=input("Enter applicant id: ")
        ap_pass=input("Enter password")
        if(ap_id.isdigit()):
            if(ViewDB.validate_access(ap_id, ap_pass)==1):
                print("Login Successful..!!")
                    
                end=True
            
            else:
                print("press 1. to enter again")
                print("press 2. to exit without update")
                try:
                    option=input()
                    if(int(option)==1):
                        pass
                    elif(int(option)==2):
                        end=True
                    else:
                        print("invalid option. Exiting LOGIN ")
                        end = True
                except:
                    print("invalid option. Exiting LOGIN")
                    end = True
            
                
        else:
            print("Invalid Credentials.")
            print("press 1. to enter again")
            print("press 2. to exit without update")
            try:
                option=input()
                if(int(option)==1):
                    pass
                elif(int(option)==2):
                    end=True
                else:
                    print("invalid option. Exiting LOGIN ")
                    end = True
            except:
                print("invalid option. Exiting LOGIN")
                end = True
            
    return ap_id



#login_module()
#print("Returned")