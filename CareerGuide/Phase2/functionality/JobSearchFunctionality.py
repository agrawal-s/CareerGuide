from database import ViewDB
#from classes import JobModule
def job_search():
    list1=ViewDB.get_jobs()

    end=False
    while(end==False):
        v_tech=input("Enter the technology you want to search for")
        v_sal=input("Enter minimum salary expected")
        v_exp=input("Enter expected minimum years of experience")
        if(v_tech is not '' and v_sal is not '' and v_exp is not ''):
            print("Details of all the jobs that matched with any of the search criteria")
            print("JobId        JobName            Technology        SkillSet        SalaryOffered        MinExperience")
            print("=====================================================================================================")
            
            for row in list1:
                t_tech=row.get_pref_tech()
                t_sal=row.get_salary_off()
                t_exp=row.get_min_exp()
    
                if(v_tech==t_tech or int(v_sal)<=t_sal or int(v_exp)>=t_exp):
                    print(row.get_job_id(),'        ',row.get_job_name(),'            ',row.get_pref_tech(),'        ',row.get_skill_set(),'        ',row.get_salary_off(),'        ', row.get_min_exp())
            print("Jobs that exactly matches the technology:")
            print("JobId        JobName            Technology        SkillSet        SalaryOffered        MinExperience")
            print("=====================================================================================================")
            for row in list1:
                t_tech=row.get_pref_tech()
                t_sal=row.get_salary_off()
                t_exp=row.get_min_exp()
                if(v_tech==t_tech):
                    print(row.get_job_id(),'        ',row.get_job_name(),'            ',row.get_pref_tech(),'        ',row.get_skill_set(),'        ',row.get_salary_off(),'        ', row.get_min_exp())
                
            print("Jobs that match the minimum salary expected:")
            print("JobId        JobName            Technology        SkillSet        SalaryOffered        MinExperience")
            print("=====================================================================================================")
            for row in list1:
                t_tech=row.get_pref_tech()
                t_sal=row.get_salary_off()
                t_exp=row.get_min_exp()
                if(v_sal.isdigit() and int(v_sal)<=t_sal):
                    print(row.get_job_id(),'        ',row.get_job_name(),'            ',row.get_pref_tech(),'        ',row.get_skill_set(),'        ',row.get_salary_off(),'        ', row.get_min_exp())
                
            print("Jobs that match the minimum years of experience expected:")
            print("JobId        JobName            Technology        SkillSet        SalaryOffered        MinExperience")
            print("=====================================================================================================")
            for row in list1:
                t_tech=row.get_pref_tech()
                t_sal=row.get_salary_off()
                t_exp=row.get_min_exp()
                if(v_exp.isdigit() and int(v_exp)>=t_exp):
                    print(row.get_job_id(),'        ',row.get_job_name(),'            ',row.get_pref_tech(),'        ',row.get_skill_set(),'        ',row.get_salary_off(),'        ', row.get_min_exp())
                
            print("Jobs that match all the criteria:")
            print("JobId        JobName            Technology        SkillSet        SalaryOffered        MinExperience")
            print("=====================================================================================================")
            for row in list1:
                t_tech=row.get_pref_tech()
                t_sal=row.get_salary_off()
                t_exp=row.get_min_exp()
                if(v_tech==t_tech and v_exp.isdigit() and v_sal.isdigit() and int(v_sal)<=t_sal and int(v_exp)>=t_exp and v_exp.isdigit() and v_sal.isdigit()):
                    print(row.get_job_id(),'        ',row.get_job_name(),'            ',row.get_pref_tech(),'        ',row.get_skill_set(),'        ',row.get_salary_off(),'        ', row.get_min_exp())
                else:
                    pass
            end=True
        else:
            print("Incorrect Entries. Please ReEnter")
#get_jobs_all()

    