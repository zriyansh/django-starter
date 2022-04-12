# django-starter

This simple project is done insde a virtual environment. 

To get started, follow these steps. 

make a dir --> cd to it. 

```
sudo pip3 install virtualenvwrapper
```

```
pip3 install django
```

To setup a project structure. 
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