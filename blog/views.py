from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from .models import Post,Category
from django.shortcuts import get_object_or_404
from comments.forms import CommentForm

# 引入类视图函数
from django.views.generic import ListView

#  首页
# 普通视图函数逻辑，利用类视图函数来改些此逻辑
# def index(request):

	# return HttpResponse('欢迎访问我的博客!!')
	# return render(request,'blog/index.html',context={
	# 	'title':'我的博客首页',
	# 	'welcome':'欢迎访问我的博客'
	# 	})

	# post_list = Post.objects.all().order_by('-created_time')  # objects：模型管理器,all方法获取所有文章
	# return render(request,'blog/index.html',context={
	# 	'post_list':post_list
	# 	})

# 类视图函数
class IndexView(ListView):

	model = Post
	template_name = 'blog/index.html'
	context_object_name = 'post_list'
	#  ListView本身已包含分页逻辑，只需指定paginate_by属性来开启分页功能即可
	paginate_by = 5 # 5篇文章为一页

#  文章详情页视图函数
def detail(request,pk):

	#  get_object_or_404:当传入的pk（id）对应的Post（文章）在数据库中存在时，返回对应的post，若不存在，返回404错误！
	post = get_object_or_404(Post,pk = pk)
	post.increase_views() # 文章阅读量
	form = CommentForm()
	comment_list = post.comment_set.all() # 获取此篇文章下的所有评论
	# 将文章，表单，以及文章下的评论列表作为模板变量传给detail.html模板，以便渲染相应数据
	context = {

		'post':post,
		'form':form,
		'comment_list':comment_list
	}
	return render(request,'blog/detail.html',context = context)


#  归档试图函数
def archives(request,year,month):
	# 此时使用filter来过滤数据，不使用all
	post_list = Post.objects.filter(created_time__year = year,created_time__month = month).order_by('-created_time')
	return render(request,'blog/index.html',context = {'post_list':post_list})




#  分类视图函数
# 普通视图函数逻辑，利用类视图函数来改些此逻辑
# def category(request,pk):
# 	cate = get_object_or_404(Category,pk = pk)
# 	post_list = Post.objects.filter(category = cate).order_by('-created_time')
# 	return render(request,'blog/index.html',context = {'post_list':post_list})

# 类视图函数
class CategoryView(ListView):

	model = Post
	template_name = 'blog/index.html'
	context_object_name = 'post_list'

	def get_queryset(self):
		cate = get_object_or_404(Category,pk = self.kwargs.get('pk'))
		return super(CategoryView,self).get_queryset().filter(category = cate)

