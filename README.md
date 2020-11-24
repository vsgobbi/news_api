# News Portal ( Micro Service)
[![built with Python3](https://img.shields.io/badge/built%20with-Python3-red.svg)](https://www.python.org/)

## Description
Micro API built with flask backend as example. <br>
Endpoints are: 'create', 'update', 'delete' and 'view' <br>
'News'
Welcome and Reminders email when receiving a new registration form from www.agig.app/cadastro integrated with Google Sheets API.
and from validation form.

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

Project deploy and hosted at:
```
https://news-portal-dev.uc.r.appspot.com
```

#### Deploy cron job to GAE
```
gcloud app deploy cron.yaml --project encoded-shape-249320
```

#### To view your application in the web browser run:
```
gcloud app browse
```

#### To upload your cron jobs, 
you must specify the cron.yaml as a parameter to the following gcloud command:
```
gcloud app deploy cron.yaml
```
