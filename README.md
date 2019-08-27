# chariate
- Find NGO activities happening near you. 
- Get involved. 
- Organize events with the help of NGOs. Donate. 
- Watch your donations help.

## Project setup

```bash
pip install -r requirements.txt 

```

### Configure Database settings

```
Copy apps_config.example and change name to apps_config.json
Then change ENV Vars values
```

### Make migrations and migrate

```
python manage.py makemigrations
python manage.py migrate
```

### Compiles and hot-reloads for development

```
python manage.py runserver
```


### Load Default Dictionaries Data
```
After migrations and migrate
python manage.py loaddata ... .json
```

### Redis
```
sudo systemctl start redis
```

### Celery
```
#for windows
#pip install gevent
celery -A chariate_backend worker -l info -P gevent

#for linux
celery -A chariate_backend worker -l info

#clean
celery -A chariate_backend purge

```
