'''
Created on Sep 8, 2015

@author: Shivangi.PAndey02
'''
#from exceptions.CustomExceptions import InvalidCategoryException
#from functionality import RegisterFunctionality
#from functionality import validate_input
from database import ViewDB
from utility import DBConnectivity
import cx_Oracle
from validations import validateInput

def register_module():
    valid=False
    while not valid:
        try:
            end=False    
            while(end is not True):
                ap_name=input("Enter applicant name:")
                ap_pass=input("Enter password:")
                ap_skill=input("Enter your skill set:")
                ap_exp=input("Enter no.of.years of experience:")
                ap_tech=input("Enter preferred technology:")
                ap_gender=input("Enter Gender (M/F):")
                ap_contact=input("Enter Contact info:")
                result=validateInput.validate_input(ap_name, ap_pass, ap_skill, ap_exp, ap_tech, ap_gender, ap_contact)
                if(result ==1):
                    con=DBConnectivity.create_connection()
                    cur=DBConnectivity.create_cursor(con)
                    out_param = cur.var(cx_Oracle.STRING)
                    execute_proc= cur.callproc('INSERT_APPLICANT',[ap_name,ap_pass,ap_skill,ap_exp,ap_tech,ap_gender,ap_contact,out_param])
                    con.commit()
                    cur.close()
                    con.close()
         
                    r0=int(out_param.getvalue())
                    if(r0 is not 1):
                        print("Invaild data entry. Please re-enter the details")
                    else:
                        end=True
                        valid=True
                        
                            
                elif(result ==-1):
                    print("Invalid Name or Name-Password combination already present. Please re-Enter the details")
                elif(result ==-2):
                    print("Password did not meet the criteria. Please re-Enter the details")
                elif(result ==-3):
                    print("Skillset Cannot be Null Value. Please re-Enter the details")
                elif(result ==-4):
                    print("Years of experience should be between 1 and 30. Please re-Enter the details")
                elif(result ==-5):
                    print("Preferred technology Cannot be Null Value. Please re-Enter the details")
                elif(result ==-6):
                    print("Gender should be in (M/F). Please re-Enter the details")
                elif(result ==-7):
                    print("Contact did not meet the criteria. Please re-Enter the details")
                if(end==True and valid==True):
                    print("Registered Successfully!!")
                    print("Your Applicant id is: ",ViewDB.get_ap_id(ap_name, ap_pass))
                    
                else:
                    option=input("Press 'Y' to enter again. Press 'N' to Exit.")
                    if(option=='Y' or option=='y'):
                        pass
                    else:
                        end= True
                        valid=True
                    #return
                
        finally:
            return 
                    
#register_module()
#print("returned")