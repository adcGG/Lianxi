from django.db import models

# Create your models here.
# 创建一个实体类,-Publisher出版社
# 1.name:出版社名称（varchar（30））
# 2.address：出版社地址（varchar（200））
# 3.city：城市（varchar（50））
# 4.country：所在国家（varchar（50））
# 5.website：网址（varchar（200））

class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	website = models.URLField()

class Author(models.Model):
	name = models.CharField(max_length=15)
	age = models.IntegerField()
	email = models.EmailField(null=True)
	# isAcitve 用于表示用户激活状态,此时需要提供一个默认值，或允许为空，boolean不能为空
	# 所以提供默认值
	isActive = models.BooleanField(default=True)

class Book(models.Model):
	title = models.CharField(max_length=30)
	publicate_date = models.DateTimeField()





