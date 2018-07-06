#  当用户提交表单后，Django需要调用相应的视图函数来处理这些数据
from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from blog.models import Post
from .models import Comment
from .forms import CommentForm

def post_comment(request,post_pk):
	# 首先要获取被评论的文章，之后需要把评论和被评论的文章进行关联
	# 若获取到，则获取；获取不到，返回404
	post = get_object_or_404(Post,pk = post_pk)
	if request.method == 'POST': # 用户提交一般为POST方式
		# 用户提交的数据保存在request.POST中，通过这些数据来构造CommentForm类的实例
		form = CommentForm(request.POST)
		# 数据提交后，调用form.is_valid方法，来检查数据是否符合格式要求
		if form.is_valid():
			# 若符合要求，调用SAVE方法保存到数据库
			# commit = False，作用是仅仅利用表单的数据生成Comment模型实例，但还不保存评论数据到数据库
			comment = form.save(commit = False)

			# 将评论和被评论的文章关联起来
			comment.post = post

			# 最终将评论数据保存到数据库，调用模型实例的SAVE方法
			comment.save()

			# 重定向到post的详情页，实际上，redirect函数接收一个模型实例时，会调用这个模型实例的get_absolute_url方法
			# 然后重定向到get_absolute_url方法返回的url
			return redirect(post)

		else:
			comment_list = post.comment_set.all() # 类似于Post.objects.all(),获取这篇文章下的所有评论（反向）
			context = {

				'post':post,
				'form':form,
				'comment_list':comment_list
			}
			return render(request,'blog/detail.html',context = context)
	# 若不是post请求，说明用户没有提交数据，重定向到文章详情页
	return redirect(post)
