'''
Created on Sep 10, 2015

@author: shivangi.pandey02
'''
'''
Created on Sep 9, 2015


@author: Shubham.Sharma13
'''
#from validations import viewvalidation
#from exceptions.CustomExceptions import InvalidJobidException
#from exceptions.CustomExceptions import InvalidAppliidException
from database import ViewDB


def view_job(ap_id):
    try:
        #ap_id=101 
        '''RegisterFunction.register_login()'''
        '''seeking for application id after login'''
        if(ap_id):
            print("The status of jobs for which you had applied are as below:")
            
            list_of_job_details=[]
            list_of_job_details=ViewDB.display_jobs(ap_id)
            if(len(list_of_job_details)>0):
                #print("JobId    PositionAppliedFor    Status")
                #print("========================================")
                for i in range (0,len(list_of_job_details)):
                    length=20
                    space=' '*(length-len(list_of_job_details[i][1]))
                    print(list_of_job_details[i][0],"\t",list_of_job_details[i][1],space,list_of_job_details[i][2])
                    
                
                choice=input("would you like to accept any offer?Press 'Y' or 'N' ")
                if(choice=='Y' or choice=="y"):
                    if(ViewDB.get_accepted(ap_id)==1):
                            print("Offer accepted")

                    else:
                        print("Offer not accepted.")
                elif(choice=='N' or choice=="n"):
                    return
                else:
                    print("Invalid credentials. Returning to the main menu.")
                    return       
            else:
                print("you have not applied for any jobs")
                return
    finally:
        pass
      


#view_job(101)
        


        