import pymysql
import re
f = open('dict.txt')
db = pymysql.connect(host = 'localhost',user = 'root',passwd = '979818137zzn',db = 'dict',port = 3306,charset = 'utf8')

cursor = db.cursor()

for line in f:
	l = re.findall(r'\S+',line)
	print(l)
	word = l[0]
	interpret = ' '.join(l[1:])
	sql = "insert into words(word,interpret) values ('%s','%s')"%(word,interpret)
	print(sql)
	try:
		cursor.execute(sql)

		db.commit()
		print('成功')
	except:
		db.rollback()
		print('失败')
f.close()
db.close()