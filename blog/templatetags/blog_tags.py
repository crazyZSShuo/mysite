#  自动从数据库中获取最新文章，显示在前台
#  自定义模板标签

from ..models import Post,Category
from django import template  # 目的是告诉django，该怎样使用此自定义模板标签，首要要注册；


register = template.Library() #  实例化一个template.Library类

@register.simple_tag
def get_recent_posts(num = 5):
	return Post.objects.all().order_by('-created_time')[:num]


#  归档模板标签
@register.simple_tag
def archives():
	# dates返回一个列表，DESC表示降序排序（时间越晚，越靠前）
	return Post.objects.dates('created_time','month',order = 'DESC')


#  分类模板标签
@register.simple_tag
def get_categories():
	return Category.objects.all()