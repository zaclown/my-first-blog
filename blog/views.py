"""
   views connect models and templates (from djangogirls tutorial)
"""

from django.shortcuts import render
from django.utils import timezone
from .models import Post

"""
    The dot before models means current directory 
    or current application. Both views.py and models.py are in the same directory. 
    This means we can use . and the name of the file (without .py). Then we import the name of the model (Post).
"""


def post_list(request):
    # we create a variable for our QuerySet: posts. Treat this as the name of our QuerySet. 
    # From now on we can refer to it by this name.
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {"posts": posts})