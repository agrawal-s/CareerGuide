'''
Created on Sep 10, 2015

@author: shivangi.pandey02
'''
'''
Created on Sep 8, 2015

@author: shrikant.agrawal
'''

import cx_Oracle

from utility import DBConnectivity
#from functionality import viewjobFunctionality
#from functionality import LoginModule

def update_details(ap_id):
            
    if ap_id == 0:
        print("Please log in to continue")
    else:
        end=False
        while(end is not True):
            print("Enter new name. Press ENTER to skip")
            option=input()
            if option is not None:
                variable=option
            else:
                end=True
            r0=1
            
            
            if variable is not '' :
                con=DBConnectivity.create_connection()
                cur=DBConnectivity.create_cursor(con)
                out_param = cur.var(cx_Oracle.STRING)
                execute_proc= cur.callproc('UPDATE_NAME',[ap_id,variable,out_param])
                con.commit()
                cur.close()
                con.close()
         
                r0=int(out_param.getvalue())
            
            
            #print(r0)
                
            if(r0 ==-2):
                print("Same Name entered")
                print("press 1. to enter again")
            
                print("press 2. to exit without update")
                try:
                    option=input()
                    if(int(option)==1):
                        pass
                    elif(int(option)==2):
                        end=True
                    else:
                        print("invalid option. Exiting the name update")
                        end = True
                except:
                    print("invalid option. Exiting the name update")
                    end = True
            
            if(r0 ==-3):
                print("Name and Password combination already exists")
                print("press 1. to enter again")
            
                print("press 2. to exit without update")
                try:
                    option=input()
                    if(int(option)==1):
                        pass
                    elif(int(option)==2):
                        end=True
                    else:
                        print("invalid option. Exiting the name update")
                        end = True
                except:
                    print("invalid option. Exiting the name update")
                    end = True
            
            
            elif(r0 is not 1):
                print("update unsuccessful")
                print("press 1. to enter again")
            
                print("press 2. to exit without update")
                try:
                    option=input()
                    if(int(option)==1):
                        pass
                    elif(int(option)==2):
                        end=True
                    else:
                        print("invalid option. Exiting the name update")
                        end = True
                except:
                    print("invalid option. Exiting the name update")
                    end = True
            else:
                end = True
                
        end=False
        while(end is not True):
            print("Enter new additional skills. Press ENTER to skip")
            option=input()
            if option is not None:
                variable=option
            else:
                end=True
            r1=1
            
            if variable is not '' :
                con=DBConnectivity.create_connection()
                cur=DBConnectivity.create_cursor(con)
                out_param = cur.var(cx_Oracle.NUMBER)
                execute_proc= cur.callproc('UPDATE_skills',[ap_id,variable,out_param])
                con.commit()
                cur.close()
                con.close()
                r1=int(out_param.getvalue())
            
            if(r1 == -2):
                print("skill already present")
                print("press 1. to enter again")
                print("press 2. to exit without update")
                try:
                    option=input()
                    if(int(option)==1):
                        pass
                    elif(int(option)==2):
                        end=True
                    else:
                        print("invalid option. Exiting the skills update")
                        end = True
                except:
                    print("invalid option. Exiting the skills update")
                    end = True
            elif(r1==-1):
                print("update unsuccessful")
                print("press 1. to enter again")
                print("press 2. to exit without update")
                try:
                    option=input()
                    if(int(option)==1):
                        pass
                    elif(int(option)==2):
                        end=True
                    else:
                        print("invalid option. Exiting the skills update")
                        end = True
                except:
                    print("invalid option. Exiting the skills update")
                    end = True
            else:
                end = True
            
        end=False
        while(end is not True):
            print("Enter total years of experience. Press ENTER to skip")
            option=input()
            if option is not None:
                variable=option
            else:
                end=True
            r2=1
            
            if variable is not '' and variable.isdigit():
                con=DBConnectivity.create_connection()
                cur=DBConnectivity.create_cursor(con)
                out_param = cur.var(cx_Oracle.STRING)
                execute_proc= cur.callproc('UPDATE_EXP',[ap_id,variable,out_param])
                con.commit()
                cur.close()
                con.close()
                r2=int(out_param.getvalue())
            
            if(r2 == -2):
                print("Current input less than the previous input")
                print("press 1. to enter again")
                print("press 2. to exit without update")
                try:
                    option=input()
                    if(int(option)==1):
                        pass
                    elif(int(option)==2):
                        end=True
                    else:
                        print("invalid option. Exiting the experience update")
                        end = True
                except:
                    print("invalid option. Exiting the experience update")
                    end = True
            elif(r2 == -3):
                print("years of experience must be between 1 to 30 years")
                print("press 1. to enter again")
                print("press 2. to exit without update")
                try:
                    option=input()
                    if(int(option)==1):
                        pass
                    elif(int(option)==2):
                        end=True
                    else:
                        print("invalid option. Exiting the experience update")
                        end = True
                except:
                    print("invalid option. Exiting the experience update")
                    end = True
        
            elif(r2==-1):
                print("update unsuccessful")
                print("press 1. to enter again")
                print("press 2. to exit without update")
                try:
                    option=input()
                    if(int(option)==1):
                        pass
                    elif(int(option)==2):
                        end=True
                    else:
                        print("invalid option. Exiting the experience update")
                        end = True
                except:
                    print("invalid option. Exiting the experience update")
                    end = True
            else:
                end = True
    if(r0==1 and r1==1 and r2==1):
        end=True
        print("details updated successfully..")
    '''
    option1=input("Do you wish to view job status and accept job offers? press Y or N.")
    if(option1=='Y' or option1=='y'):
        viewjobModule.view_job(ap_id)
    elif(option1=='N' or option1=='n'):
        return
    else:
        print("Invalid option. ")
        return
    '''
    
    
    
#update_details(101)

#print(list1)
