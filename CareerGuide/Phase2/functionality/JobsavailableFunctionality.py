'''
Created on Sep 10, 2015

@author: shivangi.pandey02
'''
from functionality import InsertjobFunctionality
#from functionality import LoginFunctionality
from validations import ViewValidations
#from validations.ViewValidations import validate_job_id

def apply(loginid):
    try:
        #loginid=LoginModule.login_module()
        end=False
        while(end is not True):
            JobId=input("Enter the Id of the job that you wish to apply for:")
        
            v=ViewValidations.validate_job_id(loginid, JobId)
        
            if(v==True): 
                v=InsertjobFunctionality.insert_Jobid(loginid, JobId)
                if v:
                    print("Applied for job successfully")
                    end=True
                    return
            elif(v==1):
                print("Insufficient Experience")
            elif(v==2):
                print("Do not possess required skill set")
            elif(v==3):
                print("Do not match with required technology")
            else:
                print("Invalid job id")
            print("press 1. to enter again")
            print("press 2. to exit without update")
            try:
                option=input()
                if(int(option)==1):
                    pass
                elif(int(option)==2):
                    end=True
                    return
                else:
                    print("invalid option. Exiting the module")
                    end = True
                    return
            except:
                print("invalid option. Exiting the Module")
                end = True
                return
            
    except Exception as e:
        print(e)
        print("Not able to retrieve data")

#apply()