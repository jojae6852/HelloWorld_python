from django.http import JsonResponse
from django.core.cache import cache
from django.shortcuts import render
import logging
# from .models import Post

def my_view(request):
    cache_key = 'my_blog_post_count'
    count = cache.get(cache_key, None)

    test ={
        "users" : [ {
            "email" : "0",
            "profile_picture" : "2",
            "username" : "3"
        }, {
            "email" : "36",
            "profile_picture" : "4",
            "username" : "5"
        }, {
            "email" : "39",
            "profile_picture" : "99999",
            "username" : "5"
        }, {
            "email" : "1",
            "profile_picture" : "4",
            "username" : "5"
        } ]
    }
    cache.set(cache_key,test,60*60)
    if not count:
        cache.set(cache_key,test,60*60)
        print('adsf',"success")
    else:
        count = cache.get(cache_key, None)
        print("a",count)
        # posts = cache.get_or_set('posts', list(Post.objects.all().values('id', 'text')))
    return JsonResponse(count, safe=False)
    # return render(request,'index.html',{'param':test})