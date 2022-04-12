# django-starter

This simple project is done insde a virtual environment. 

To get started, follow these steps. 

Note: The below steps are to autogenerate some boilerplate code, just like create-react-app.

make a dir --> cd to it. 

```
sudo pip3 install virtualenvwrapper
```

```
pip3 install django
```

To setup a new project structure. 
```
django-admin startproject <projectName>
```


To start server.
```
python3 manage.py runserver
```

If there are some warnings saying something about 'migrations' run this.

```
python manage.py migrate
```

to start a new app that inside the project
```
django-admin manage.py startapp <app_name>
``` 
For help, refer to this [playlist](https://www.youtube.com/watch?v=SIyxjRJ8VNY&list=PLsyeobzWxl7r2ukVgTqIQcl-1T0C2mzau)




Project Structure:
1. dir django_one is the root project name.
2. dir calc is an app of the root project (for unknown reasons, I don't understand why can't we keep calc inside django_one dir)
3. dir templates is the place we keep html files.
4. local urls are set in calc/urls.py and then included in django_one/urls.py
5. line 58 of settings.py was modified to ```'DIRS': [os.path.join(BASE_DIR, 'templates' )],```, don't forget to import os at top.