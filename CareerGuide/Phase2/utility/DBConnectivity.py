
import cx_Oracle
def create_connection():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') #if needed, place an 'r' before any parameter in order to address any special character such as '\'.
    conn = cx_Oracle.connect(user=r'S4562394', password='w', dsn=dsn_tns) #if needed, place an 'r' before any parameter in order to address any special character such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'

    return conn

def create_cursor(con):
    return cx_Oracle.Cursor(con)