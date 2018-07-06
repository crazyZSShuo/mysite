from django.conf.urls import url
from . import views

app_name = 'blog'  # 视图函数命名空间；就是告诉Django，这个urls.py是属于blog应用的；
urlpatterns = [
	
	# 普通视图函数的url格式
	# url(r'^index$',views.index,name = 'index'),
	# 改为类视图函数后：
	url(r'^index$',views.IndexView.as_view(),name = 'index'),

	url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name = 'detail'),
	
	url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives,name = 'archives'),
	
	# url(r'^category/(?P<pk>[0-9]+)/$',views.category,name = 'category')
	url(r'^category/(?P<pk>[0-9]+)/$',views.CategoryView.as_view(),name = 'category')
]