import pymysql
import sys
#===========================================
try:
	conn = pymysql.connect(host = 'localhost',user = 'root',passwd = '979818137zzn',db = 'gkdb',port = 3306,charset = 'utf8')
except:
	print("打开数据库连接出错，请检查！")
	conn.close()
	sys.exit()
#===========================================
cur = conn.cursor()
sql = '''create table if not exists T_fish(date1 char(12)primary key not null ,name1 char(10)not null ,
nums int not null ,price decimal (10,2)not null ,  sExplain varchar (200));'''
try:
	cur.execute(sql)
	conn.commit()
	print("T_fish表可以使用！")
except:
	print("T_fish表是否建立过程中出错！")
conn.close()
