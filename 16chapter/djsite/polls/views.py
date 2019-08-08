from django.shortcuts import render
from django.db import models
class Question(models.Model):       # 定义提问字段类
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')   # 设置提问时间字段
	def __str__(self):                                  # 类内部保留方法str
		return self.question_text                       # 返回问题字段
class Choice(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE)     # 建立一对多关系
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)      # 设置投票字段
	def __str__(self):                                  # 类内部保留方法str
		return self.choice_text                       # 返回选择项字段



# Create your views here.
