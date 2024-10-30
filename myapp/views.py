from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

import requests
from .utils.utils import createPostslug,getPostIndexfromslug,getPostsListwithSlugindex
from .utils.DBManager import DBManager


def index(request:HttpRequest):
    post_slug = request.GET.get("post","")
    print(post_slug)
    # Fetch categories from Firebase
    try:
        categories = DBManager.getCategories()
        #print(categories)  # Debugging output
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        categories = {}
    # Fetch news posts from Firebase
    try:
        news_posts = DBManager.getNewsList()
        #print(news_posts)  # Debugging output
        i = getPostIndexfromslug(post_slug,news_posts)
        news_data = getPostsListwithSlugindex(i,news_posts)
        print(news_data)

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        news_posts = {}

    # Prepare the context with the fetched categories and news posts
    context = {
        'categories': categories[1:],
        'news_posts': news_data
    }

    return render(request=request, template_name='index.html', context=context)
