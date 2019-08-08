# 先是在命令行输入
# 1.sqlplus /nolog
# 2.conn / as sysdba
# 3.startuup





import cx_Oracle,os
os.environ["ORACLE_BASE"] = 'D:/app'
os.environ["ORACLE_SID"] = 'orcl'
os.environ["ORACLE_HOME"] = 'D:/app/product/11.2.0/dbhome_1'
os.environ["LD_LIBRARY_PATH"] = '$LD_LIBRARY_PATH:$ORACLE_HOME/lib'
dns = cx_Oracle.makedsn('localhost','1521','orcl') # 监听数据库
print(dns)
connection = cx_Oracle.connect('system','979818137zzn',dns)
# connection = cx_Oracle.connect('testname','ask124',dns)


cur = connection.cursor()
sql0 = '''create table T_fish(date1 char(12)primary key not null ,name1 char(10)not null ,
nums int not null ,price number(10,2)not null ,  sExplain varchar (200))'''
sql = "select * from T_fish"
# cur.execute(sql0)
cur.execute(sql)
result = cur.fetchall()
for row in result:
	print(row)
cur.close()
connection.close()