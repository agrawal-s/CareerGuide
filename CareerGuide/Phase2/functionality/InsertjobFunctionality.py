'''
Created on Sep 10, 2015

@author: shivangi.pandey02
'''
from utility import DBConnectivity
from classes.AppliedJobModule import applied_job
def insert_Jobid(loginid,JOB_ID):
    try: 
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur1=DBConnectivity.create_cursor(con)
        count=0
        cur1.execute("select * from APPLIED_JOBS where JOB_ID="+str(JOB_ID)+"and AP_ID="+str(loginid)+"")
        for row in cur1:
            #print(row)
            count=count+1
        if(count==0):
            cur.execute("insert into APPLIED_JOBS values("+str(loginid)+","+str(JOB_ID)+","+"'PENDING')")
            cur.execute("commit")
            status=applied_job()
            status.set_job_id(JOB_ID)
            status.set_ap_id(loginid)
            status.set_status('PENDING')
            return True
        else:
            print("Already applied for job")
            return False
    except :
        print("Already applied for job")
    finally:
        cur.close()
        con.close()

#insert_Jobid(102,204)