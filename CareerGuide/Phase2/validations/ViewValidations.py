'''
Created on Sep 8, 2015

@author: Shivangi.PAndey02
'''
from database import ViewDB
from exceptions.CustomExceptions import InvalidCategoryException
from utility import DBConnectivity
import re

def validate_view():
    list_of_applicants=ViewDB.get_applicants()
    if(len(list_of_applicants)==0):
        raise InvalidCategoryException()
    
    return list_of_applicants

def validate_session(ap_id,ap_pass):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        
        cur.execute("select ap_id,ap_pass from applicant_details where ap_id=:ap_id",{"ap_id":ap_id,"ap_pass":ap_pass}) 
        for ap_id, in cur:
            print("In DB",ap_id)
            if(ap_id==None):
                raise InvalidCategoryException()
        return ap_id
        
        for ap_pass, in cur:
            if(len(ap_pass)<5):
                print("Password length too small")
            elif(re.search(r"\d",ap_pass)==None):
                print("Password should contain atleast one digit")
            elif(re.search(r"[A-Z]",ap_pass)==None):
                print("Password should contain atleast one alphabet")
            elif(re.search(r"\w",ap_pass)==None):
                print("Password should contain atleast one special character")
        return ap_pass
    
    finally:
        cur.close()
        con.close()
        

def validate_job_id(loginid,JOB_ID):
    try:
        jobdetails=ViewDB.get_job(JOB_ID)
        
        applicantdetails=ViewDB.get_user_wd(loginid) 
        skill_set=[]
        #print(jobdetails.get_pref_tech())
        #print(applicantdetails.get_ap_tech())
        if(jobdetails.get_pref_tech()==applicantdetails.get_ap_tech()):
            skill_set=applicantdetails.get_ap_skill()
            #print(skill_set)
            if(jobdetails.get_skill_set() in skill_set):
                if(jobdetails.get_min_exp()<=applicantdetails.get_ap_exp()):
                    #print("T")
                    return True
                else:
                    #print("1")
                    return 1        
            else:
                #print("2")
                return 2     
        else:
            #print("3")
            return 3
            
    except:
        print("Some error occured") 

def validate_job_id_wid(JOB_ID):
    try:
        jobdetails=ViewDB.get_job(JOB_ID)
        
        if(jobdetails):
            return True
        else:
            return False        #print("1")
            
    except:
        print("Some error occured")
        return False 
