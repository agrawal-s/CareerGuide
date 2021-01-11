'''
Created on Sep 10, 2015

@author: shivangi.pandey02
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
        
list1=get_applicants()

for row in list1:
    print(row.get_ap_id(),row.get_ap_name(),row.get_ap_pass(),row.get_ap_skill(),row.get_ap_exp(),row.get_ap_tech())
