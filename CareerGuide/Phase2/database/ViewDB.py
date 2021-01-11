'''
Created on Sep 8, 2015

@author: Shivangi.PAndey02
'''
import cx_Oracle
from utility import DBConnectivity
from classes.ApplicantModule import Applicant
from classes import JobModule
from classes.JobModule import Job

def get_applicants():
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_applicants=[]
        cur.execute("select * from applicant_details ")
        for ap_id,ap_name,ap_pass,ap_skill,ap_exp,ap_tech,ap_gender,ap_contact in cur:
            '''
            In this loop, we are creating a product object for every row
            and setting the values from the row into the product object
            '''
            applicant=Applicant()
            applicant.set_ap_id(ap_id)
            applicant.set_ap_name(ap_name)
            applicant.set_ap_pass(ap_pass)
            applicant.set_ap_skill(ap_skill)
            applicant.set_ap_exp(ap_exp)
            applicant.set_ap_tech(ap_tech)
            applicant.set_ap_gender(ap_gender)
            applicant.set_ap_contact(ap_contact)
 
            '''
            Here were are adding the product to a list
            '''
            list_of_applicants.append(applicant)
            
        return list_of_applicants
    #except cx_Oracle.DatabaseError as e:
        #print(e)
    finally:
        cur.close()
        con.close()
        

def get_user(ap_id):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        
        cur.execute("select * from applicant_details where ap_id="+str(ap_id))
        for ap_id,ap_name,ap_pass,ap_skill,ap_exp,ap_tech,ap_gender,ap_contact in cur:
            applicant=Applicant()
            applicant.set_ap_id(ap_id)
            applicant.set_ap_name(ap_name)
            applicant.set_ap_pass(ap_pass)
            applicant.set_ap_skill(ap_skill)
            applicant.set_ap_exp(ap_exp)
            applicant.set_ap_tech(ap_tech)
            applicant.set_ap_gender(ap_gender)
            applicant.set_ap_contact(ap_contact)
            #list_of_applicants.append(applicant)
            #print(ap_name,' ',ap_skill,' ',ap_exp,' ',ap_tech)
            print("The details are :")
            print("-----------------")
            print("Name : ",ap_name)
            print("Skill set: ",ap_skill)
            print("Total Experience : ",ap_exp)
            print("Preferred Technology : ",ap_tech)
            return applicant
    finally:
        cur.close()
        con.close() 

def get_user_wd(ap_id):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        
        cur.execute("select * from applicant_details where ap_id="+str(ap_id))
        for ap_id,ap_name,ap_pass,ap_skill,ap_exp,ap_tech,ap_gender,ap_contact in cur:
            applicant=Applicant()
            applicant.set_ap_id(ap_id)
            applicant.set_ap_name(ap_name)
            applicant.set_ap_pass(ap_pass)
            applicant.set_ap_skill(ap_skill)
            applicant.set_ap_exp(ap_exp)
            applicant.set_ap_tech(ap_tech)
            applicant.set_ap_gender(ap_gender)
            applicant.set_ap_contact(ap_contact)
            #list_of_applicants.append(applicant)
            #print(ap_name,' ',ap_skill,' ',ap_exp,' ',ap_tech)
            return applicant
    finally:
        cur.close()
        con.close() 

        
def get_ap_id(ap_name,ap_pass):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        
        cur.execute("select ap_id from applicant_details where ap_name='"+str(ap_name)+"' and ap_pass='"+str(ap_pass)+"'")
        for ap_id, in cur:
            result=ap_id
            
            #list_of_applicants.append(applicant)
            #print(ap_name,' ',ap_skill,' ',ap_exp,' ',ap_tech)
            
    finally:
        cur.close()
        con.close()
    return result 



#get_user(102)   
def validate_access(ap_id,ap_pass):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        out_param = cur.var(cx_Oracle.STRING)
        execute_proc= cur.callproc('VALIDATE_LOGIN',[ap_id,ap_pass,out_param])
        con.commit()
         
        r0=int(out_param.getvalue())
        if(r0 == -1):
            print("Invaild id. Please re-enter the details")
            return -1
        elif(r0 == -2):
            print("Invaild password. Please re-enter the details")
            return -1
        else:
            #print("")
            return 1
    finally:
        cur.close()
        con.close()
        

def get_jobs():
    con=DBConnectivity.create_connection()
    cur=DBConnectivity.create_cursor(con)
    list_of_jobs=[]
    cur.execute("select * from jobs ")
    for job_id,job_name,pref_tech,skill_set,salary_off,min_exp,vacancy in cur:
        job=Job()
        job.set_job_id(job_id)
        job.set_job_name(job_name)
        job.set_pref_tech(pref_tech)
        job.set_skill_set(skill_set)
        job.set_salary_off(salary_off)
        job.set_min_exp(min_exp)
        job.set_vacancy(vacancy)
        list_of_jobs.append(job)
        #print(job_id,' ',job_name,' ',pref_tech,' ',skill_set)
    return list_of_jobs
#get_jobs()

def get_job(job_id):
    con=DBConnectivity.create_connection()
    cur=DBConnectivity.create_cursor(con)
    
    cur.execute("select * from jobs where job_id="+str(job_id)+"")
    for job_id,job_name,pref_tech,skill_set,salary_off,min_exp,vacancy in cur:
        job=Job()
        job.set_job_id(job_id)
        job.set_job_name(job_name)
        job.set_pref_tech(pref_tech)
        job.set_skill_set(skill_set)
        job.set_salary_off(salary_off)
        job.set_min_exp(min_exp)
        job.set_vacancy(vacancy)
        #print(job_id,' ',job_name,' ',pref_tech,' ',skill_set)
    return job


'''
Created on Sep 8, 2015


@author: Shubham.Sharma13
'''
'''
these function retrieves all jobs status and accepted offers
'''
def display_jobs(ap_id):
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        #print(aid_value)
        print("===============================================")
        print("Job Id Position Applied for     Status")
        print("===============================================")
        
        cur.execute("SELECT J.JOB_ID,J.JOB_NAME,AJ.STATUS FROM JOBS J,APPLIED_JOBS AJ WHERE J.JOB_ID=AJ.JOB_ID AND AJ.AP_ID="+str(ap_id)+"")
        
        list_of_job_details=[]
        for x,y,z in cur:
            #print("1")
            ind_list=[]
            ind_list.append(x)
            ind_list.append(y)
            ind_list.append(z)
            list_of_job_details.append(ind_list)
        cur.close()
        con.commit()
        con.close()
        #print(len(list_of_job_details))
        return list_of_job_details
    
def get_accepted(ap_id):
    con=DBConnectivity.create_connection()
    cur1=DBConnectivity.create_cursor(con)
    '''print("Enter JobId: ",aid_value)'''
    #print(1)
    cur1.execute("select job_id from applied_jobs where status='SELECTED' and ap_id=:c_ap_id",{"c_ap_id":ap_id})
    #print(2)
    list_of_Jid=[]
    Jid=input("Enter JobID")
    #print("Jid",Jid)
    count=0
    for jj in cur1:
        #print(3)
        list_of_Jid.append(jj[0])
        #print("Jid",Jid,"jj[0]",jj[0])
        if int(jj[0])==int(Jid):
            count+=1
            break
    cur1.close()
    con.commit()
    con.close()
    if(count==1):
        return 1
    else:
        return 0


#get_jobs()
#r_val=get_accepted(101)        
#if(r_val==1):
#    print("accepted")
#else:
#    print("error")
'''
list1=display_jobs(101)
for row in list1:
    print(row[0],row[1],row[2])
'''
            

#valid=0
#while(valid is not 1):
    
#    valid=validate_access(101,'SHR@123')
#print("login Successful")
#get_user(101)

#print(get_ap_id('RAM', 'RAM@123'))