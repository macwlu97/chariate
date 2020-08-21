# chariate
- Find NGO activities happening near you. 
- Get involved. 
- Organize events with the help of NGOs. Donate. 
- Watch your donations help.

## Project setup

```bash
pip install -r requirements.txt 

```

* [Chariate Frontend](https://github.com/macwlu97/chariate_frontend) (React Web Application)

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

### Load Default Dictionaries Data
```
After migrations and migrate
python manage.py loaddata initialData.json
```

### Compiles and hot-reloads for development

```
python manage.py runserver
```



