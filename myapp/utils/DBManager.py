
from firebase import firebase




class DBManager:
    __config = {
    "apiKey": "AIzaSyAjimJxm2UZHP7L5rHIpAdBIWlDr2_NFKs",
    "authDomain": "news-in-briefs-db.firebaseapp.com",
    "databaseURL": "https://news-in-briefs-db-default-rtdb.firebaseio.com",
    "storageBucket": "news-in-briefs-db.appspot.com"
    }
    __firebaseconn = firebase.FirebaseApplication(__config["databaseURL"], None)
    @staticmethod
    def getNewsList()->list:
        data = DBManager.__firebaseconn.get('/News', None)
        lst = []
        for x in data:
            data[x]["id"] = x
            lst.append(data[x])
        return lst
    @staticmethod
    def getCategories()->list:
        data = DBManager.__firebaseconn.get('/NewsCategories', None)
        return data