#coding=utf-8
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from blogapp.models import post,Category
from django.http import Http404


def index(request):
    categories = Category.objects.all()
    posts = post.objects.all()
    return render_to_response("blog/index.html",
                  {"posts": posts,
                   "categories": categories
                   },
                  context_instance=RequestContext(request))



def Post(request,pk):
    categories = Category.objects.all()
    posts = post.objects.get(pk=pk)
    return render_to_response("blog/post.html",
                  {"post": posts,
                   "is_category": False,
                   "categories": categories
                   },
                  context_instance=RequestContext(request))


('django.contrib.auth.context_processors.auth',
 'django.core.context_processors.debug',
 'django.core.context_processors.i18n',
 'django.core.context_processors.media',
 'django.core.context_processors.static',
 'django.core.context_processors.tz',
'django.core.context_processors.request',
)
# def Index_Post(request):
#     categories = Category.objects.all()
#     posts = post.objects.all()
#     for contentss in posts:
#         content1=contentss[0:10]
#     return render_to_response("blog/post.html",
#                   {"post": posts,
#                    "categories": categories,
#                    'contents':content1
#                    },
#                   context_instance=RequestContext(request))


def category(request, pk):
  """相应分类下的文章检索"""

  try:
    cate = Category.objects.get(pk=pk)
  except Category.DoesNotExist:  ## 读取分类，如果不存在，则引发错误，并404
    raise Http404

  categories = Category.objects.all()
  posts = cate.post_set.all() ## 获取分类下的所有文章
  return render_to_response('blog/index.html', ## 使用首页的文章列表模版，但加入了的一个`is_category`开关
    {"posts": posts,
    "is_category": True,
    "cate_name": cate.name,
    "categories": categories},
    context_instance=RequestContext(request)
  )

