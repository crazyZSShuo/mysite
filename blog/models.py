from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse

class Category(models.Model):

	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Tag(models.Model):

	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Post(models.Model):

	title = models.CharField(max_length=70)
	body = models.TextField()
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	excerpt = models.CharField(max_length=200,blank=True)

	category = models.ForeignKey(Category)
	tags = models.ManyToManyField(Tag,blank=True)
	author = models.ForeignKey(User)

	# 文章阅读量字段
	views = models.PositiveIntegerField(default = 0)

	def increase_views(self):
		self.views += 1
		self.save(update_fields = ['views'])

	def __str__(self):

		return self.title

	#  此方法返回post对应的url
	def get_absolute_url(self):

		return reverse('blog:detail',kwargs = {'pk':self.pk})


	class Meta: # 此类的作用就是制定默认文章的排序方式，先发表的靠前排列

		ordering = ['-created_time']


