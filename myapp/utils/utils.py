import re
def createPostslug(text):
    # Replace any non-alphanumeric character (symbols, spaces, etc.) with a hyphen
    return re.sub(r'[^a-zA-Z0-9]', '-', text)



def getPostIndexfromslug(slug:str,data:list):
    for x in range(len(data)):
        if(data[x]["post_slug"] == slug):
            return x
    return -1

def getPostsListwithSlugindex(idx:int,data:list):
    lst = data.copy()
    if(idx < 0):
        return lst
    val = lst.pop(idx)
    lst.insert(0,val)
    return lst