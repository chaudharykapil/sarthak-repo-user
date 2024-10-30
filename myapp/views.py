from django.shortcuts import render
from firebase import firebase
import requests

config = {
    "apiKey": "AIzaSyAjimJxm2UZHP7L5rHIpAdBIWlDr2_NFKs",
    "authDomain": "news-in-briefs-db.firebaseapp.com",
    "databaseURL": "https://news-in-briefs-db-default-rtdb.firebaseio.com",
    "storageBucket": "news-in-briefs-db.appspot.com"
}

def index(request):
    firebaseconn = firebase.FirebaseApplication(config["databaseURL"], None)

    # Fetch categories from Firebase
    try:
        categories = firebaseconn.get('/NewsCategories', None)
        print(categories[1:])  # Debugging output
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        categories = {}

    # Fetch news posts from Firebase
    try:
        news_posts = firebaseconn.get('/News', None)
        print(news_posts)  # Debugging output
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        news_posts = {}

    # Prepare the context with the fetched categories and news posts
    context = {
        'categories': categories[1:],
        'news_posts': news_posts
    }

    return render(request=request, template_name='index.html', context=context)
