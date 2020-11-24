# News Portal ( Micro Service)
[![built with Python3](https://img.shields.io/badge/built%20with-Python3-red.svg)](https://www.python.org/)

## Description
Micro API built with flask backend as example. <br>
Endpoints are: 'create', 'update', 'delete' and 'view' <br>
'News' and 'Authors' CRUD using MongoDB Atlas. <br>
news json example:
```
{
    "title": "Pymongo if very fun and Python is Beautiful!",
    "content": "This is another content of something...",
    "author_id": "5fbcb69ff66d1f21699ba150"
}
```
 

### Using Google Cloud App Engine with MongoDB using libs as: <br> 'anom', 'python3' standard, 'flask', 'flask jwt'

## **Usage**
#### Install venv:
```
virtualenv -p python3.8 venv && source venv/bin/activate && pip install -r requirements.txt 
```

#### Install requirements (Only install locally, don't need to specify for GAE Python3)
``` 
pip install -r requirements.txt
```

#### Test before Google Cloud Deploy
```
dev_appserver.py app.yaml
```

#### Testing routes are available with Postman Collection

#### Endpoints:
```
/api/news
/api/news/create
/api/news/delete
/api/news/update

/api/authors
/api/authors/create
```

#### Project endpoints collection for Postman at:
```
Flask MongoDB API Example.postman_collection.json
```

#### Project deployment and hosted at:

https://news-portal-dev.uc.r.appspot.com


#### Git Repo:
https://github.com/vsgobbi/news_api
#### GPL licensed: @vsgobbi
