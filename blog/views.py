from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Blog

def blogs(req):
    blogs = Blog.objects
    return render(req, "blogs.html",{"blogs":blogs})
def detail(req,blog_id):
    detail_blog = get_object_or_404(Blog,pk = blog_id)
    return render(req,'detail.html',{'blog':detail_blog})
