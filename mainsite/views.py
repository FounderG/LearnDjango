from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from django.template.loader import get_template
from datetime import datetime

# Create your views here.
def homepage(request):
	template = get_template('index.html')
	posts = Post.objects.all()
	now = datetime.now()
	#post_lists = list()
	html = template.render(locals())
	#for count, post in enumerate(posts):
		#post_lists.append("No.{}:".format(str(count))+str(post)+"<br>")
	return HttpResponse(html)