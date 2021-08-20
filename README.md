# Creating Twitter Clone Tutorial

This is a simple tutorial by Daniyar Aubekerov on how to build minimalistic twitter application.


## Creating new django project:
```
django-admin startproject twitterclone
```


## Creating new django applications for users and twits:
Open twitterclone folder and enter:
``` python
python manage.py startapp accounts
python manage.py startapp twits
```

## Add applications to settings

```
twitterclone/twitterclone/settings.py:

INSTALLED_APPS = [
    'accounts', 'twits',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

## Creating models

```python
twitterclone/accounts/models.py:

class Account(models.Model):
    login = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    image = models.FileField(upload_to = 'images/accounts/', blank = True)
    follows = models.ManyToManyField('self',blank=True)
```

```python
twitterclone/twits/models.py:

from django.db import models
from accounts.models import Account
class Twit(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.CharField(max_length = 250)
    image = models.FileField(upload_to = 'images/twits/', blank = True)

class Comment(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.CharField(max_length = 100)
    twit = models.ForeignKey(Twit, on_delete=models.CASCADE)
```

## Set up admin panels

```
twitterclone/twits/admins.py:

from django.contrib import admin
from .models import Twit, Comment

admin.site.register(Twit)
admin.site.register(Comment)
```

```
twitterclone/accounts/admins.py:

from django.contrib import admin
from .models import Account

admin.site.register(Account)
```


## Run Migrations
```
python manage.py migrate
python manage.py makemigrations
```


## Update project's settings
Insert in the end of the file:

```
twitterclone/twitterclone/settings.py:

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static/static_root')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

```


## Accesing Media files from url

```
twitterclone/twitterclone/urls.py:

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```


## Adding templates folder
Create 'templates' folder in the main folder and then:

```
twitterclone/twitterclone/settings.py:

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```


## inside of the templates folder create base.html file
``` html
    <html>
    <head>
        <title> {% block title %}{% endblock %} </title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
        {% block styles %}{% endblock %}
    </head>

    <body>
        {% if request.session.user %}
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
                <div class="container-fluid">
                    <a class="navbar-brand" href="{% url 'index' %}">TwitClone</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                            <li class="nav-item">
                                <a class="nav-link active" aria-current="page" href="{% url 'index' %}">Twits</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="{% url 'about' %}">Post a twit</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="{% url 'users' %}">Users</a>
                            </li>
                        </ul>
                        <div class="d-flex">
                            <a class="btn btn-outline-success" href = "{% url 'login' %}">My account</a>
                            <a class="btn btn-outline-success" href = "{% url 'register' %}">Sign Out</a>
                        </div>
                    </div>
                </div>
            </nav>
        {% else %}
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
                <div class="container-fluid">
                    <a class="navbar-brand" href="{% url 'index' %}">TwitClone</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                            <li class="nav-item">
                                <a class="nav-link active" aria-current="page" href="{% url 'index' %}">Home</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="{% url 'about' %}">About</a>
                            </li>
                        </ul>
                        <div class="d-flex">
                            <a class="btn btn-outline-success" href = "{% url 'login' %}">Login</a>
                            <a class="btn btn-outline-success" href = "{% url 'register' %}">Register</a>
                        </div>
                    </div>
                </div>
            </nav>
        {% endif %}
        {% block body %}{% endblock %}
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
        {% block scripts %}{% endblock %}
    </body>

</html>
```

## Create empty functions:

```
twitterclone/twitterclone/views.py:

from django.shortcuts import render
def index(request):
    context = dict()
    return render(request, 'general/index.html', context)

def about(request):
    context = dict()
    return render(request, 'general/about.html', context)
```

```
twitterclone/accounts/views.py:

from django.shortcuts import render
def login(request):
    context = dict()
    return render(request, 'general/login.html', context)

def register(request):
    context = dict()
    return render(request, 'general/register.html', context)

def users(request):
    context = dict()
    return render(request, 'app/users.html', context)
```

## Edit urls

```python
twitterclone/twitterclone/urls.py:

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, about
from accounts.views import login, register, users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('about/', about, name = 'about'),
    path('login/', login, name = 'login'),
    path('register/', register, name = 'register'),
    path('users/', users, name = 'users'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Add html files
Make each of the files below extend base.html and change title
```
templates/general/index.html
templates/general/about.html
templates/general/login.html
templates/general/register.html
templates/general/404.html
templates/app/users.html

{% extends 'base.html' %}

{% block title%}Name of the page{% endblock %}
```

## Create registration


``` html
templates/general/register.html

{% extends 'base.html' %}

{% block title%}Register page{% endblock %}

{% block body %}
    
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        <label for="login">Your login: </label>
        <input id="login" type="text" name="login">
        <label for="password">Your password: </label>
        <input id="password" type="password" name="password">
        <label for="image">Your image: </label>
        <input type="file" name = "image">
        <input type="submit" value="Register">
    </form>

    {% if error_data %}
        <br> Some of your data is invalid
    {% endif %}

    {% if error_login %}
        <br> This login is already taken
    {% endif %}
{% endblock %}

```

```python
accounts/views.py 

def register(request):
    context = dict()
    if (request.method == 'POST'):
        login = request.POST['login']
        password = request.POST['password']
        try:
            image = request.FILES['image']
            has_image = True
        except:
            has_image = False
        
        if (len(login)>30 or len(password)>30 or len(login) < 2 or len(password)<5):
            context['error_data'] = True
            return render(request, 'general/register.html', context)
        else:
            try:
                potential_duplicate = Account.objects.get(login = login)
                context['error_login'] = True
                return render(request, 'general/register.html', context)
            except:
                #Correct input
                if (has_image):
                    user = Account(login = login, password = password, image = image)
                else:
                    user = Account(login = login, password = password)
                user.save()
                request.session['user'] = login

    
    return render(request, 'general/register.html', context)
```

## Create login

``` html
templates/general/login.html

{% extends 'base.html' %}

{% block title%}Login page{% endblock %}

{% block body %}
    
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        <label for="login">Your login: </label>
        <input id="login" type="text" name="login">
        <label for="password">Your password: </label>
        <input id="password" type="password" name="password">
        <input type="submit" value="login">
    </form>

    {% if error_data %}
        <br> Some of your data is invalid
    {% endif %}

    {% if error_login %}
        <br> This login is already taken
    {% endif %}
{% endblock %}

```



```python
accounts/views.py 

def login(request):
    context = dict()
    if (request.method == 'POST'):
        login = request.POST['login']
        password = request.POST['password']
        
        try:
            potential_user = Account.objects.get(login = login)
            if (potential_user.password == password):
                request.session['user'] = login
                return render(request, 'app/users.html', context)
            else:
                context['error_password'] = True
                return render(request, 'general/login.html', context)
        except:
            context['error_login'] = True
            return render(request, 'general/login.html', context)
    return render(request, 'general/login.html', context)

```


## Signout

Add url:
```python
twitterclone/twitterclone/urls.py:

path('signout/', signout, name = 'signout')
```

Write view

```python
accounts/views.py 

def signout(request):
    context = dict()
    request.session['user'] = None
    return render(request, 'general/index.html', context)
```

Update base.html

```html
<a class="btn btn-outline-success" href = "{% url 'signout' %}">Sign Out</a>
```

## All users

```python
accounts/views.py 

def users(request):
    context = dict()
    users = Account.objects.all()
    context['users'] = users
    return render(request, 'app/users.html', context)
```


``` html
templates/app/users.html

{% extends 'base.html' %}

{% block title %}Users Page{% endblock %}


{% block body %}
    <div>
        <table class="table">
            <thead class="table-dark">
                <tr>
                <th scope="col">#</th>
                <th scope="col">Login</th>
                <th scope="col">Image</th>
                <th scope="col">View</th>
                </tr>
            </thead>
            <tbody>
                {% for user in users %}
                    <tr>
                        <th scope="row">{{forloop.counter}}</th>
                        <td>{{user.login}}</td>
                        {% if user.image %}
                            <td><img src = "/media/{{user.image}}" style = "width:50px; height: 50px"></td>
                        {% else %}
                            <td>???</td>
                        {% endif %}
                        <td><a class = "btn btn-primary" href = "{% url 'user' user.login %}">Open</a></td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>

{% endblock %}
```

## Accounts page

```python
accounts/views.py 

def user(request, login):
    context = dict()
    try:
        user = Account.objects.get(login = login)
        context['user'] = user
        return render(request, 'app/user.html', context)
    except:
        return render(request, 'general/404.html', context)

    return render(request, 'app/user.html', context)
```

```python
twitterclone/twitterclone/urls.py:

path('users/<str:login>/', user, name = 'user')
```

```html
templates/app/user.html

{% extends 'base.html' %}

{% block title%}User page{% endblock %}

{% block body %}
    <div class="container">
        <div class="row">
            <div class="col-8">
                {% for twit in twits %}
                    <div class="alert alert-primary" role="alert">
                        {{twit.content}}
                    </div>
                {% empty %}
                    <div class="alert alert-danger" role="alert">
                        No twits yet
                    </div>
                {% endfor %}
            </div>
            <div class="col-4">
                <div class="card" style="width: 18rem;">
                <img src="/media/{{user.image}}" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">{{user.login}}</h5>
                    </div>
                </div>
            </div>
        </div>
    </div>
{% endblock %}
```

## My Account

```
accounts/views.py 

def my_account(request):
    context = dict()
    try:
        login = request.session['user']
        user = Account.objects.get(login = login)
        context['user'] = user
        try:
            twits = Twit.objects.filter(author = user)
            context['twits'] = twits
        except:
            context['twits'] = []
        return render(request, 'app/user.html', context)
    except:
        return render(request, 'general/404.html', context)

    return render(request, 'app/user.html', context)
```


```
urls.py

path('account/', my_account, name = 'my_account')
```

Update HTML
```html
templates/base.html

<a class="btn btn-outline-success" href = "{% url 'my_account' %}">My account</a>
```

## Twits 

```python
twits/views.py

def twits(request):
    context = dict()
    user = Account.objects.get(login = request.session['user'])
    friends = user.follows.all()
    print(friends)
    twits = []
    all_twits = Twit.objects.all()
    for twit in all_twits:
        if twit.author in friends:
            twits.append(twit)
    context['twits'] = twits
    return render(request, 'app/twits.html', context)

```

```
urls.py

path('twits/', twits, name = 'twits')
```

```html
templates/app/twits.html

{% extends 'base.html' %}

{% block title%}Twits page{% endblock %}

{% block body %}
    {% for twit in twits %}
        <div class="alert alert-primary" role="alert">
            <b><a href = "{% url 'user' twit.author.login %}">{{twit.author.login}}</a></b>: {{twit.content}}   <a class = "btn btn-primary" style = "height: 35px" href = "{% url 'twit' twit.pk %}">Open</a>
            <br>
        </div>
    {% endfor %}
{% endblock %}
```

Update base
```html
templates/base.html

<a class="nav-link active" aria-current="page" href="{% url 'twits' %}">Twits</a>
```

## Twit page

```python
twits/views.py

def twit(request, pk):
    context = dict()
    twit = Twit.objects.get(pk = pk)
    context['twit'] = twit
    if (request.method == 'POST'):
        content = request.POST['comment']
        user = Account.objects.get(login = request.session['user'])
        comment = Comment(author = user, content = content, twit = twit)
        comment.save()
    comments = Comment.objects.filter(twit = twit)
    context['comments'] = comments
    
    return render(request, 'app/twit.html', context)
```

```python
urls.py

path('twits/<int:pk>', twit, name = 'twit'),
```

```html
templates/app/twit.html

{% extends 'base.html' %}

{% block title%}Twit page{% endblock %}

{% block body %}
    <div class="alert alert-info" role="alert">
        Author: <a href = "{% url 'user' twit.author.login %}">{{twit.author.login}}</a> <br>
        Content: {{twit.content}} 
        {% if twit.image %}
            <br>
            <img src = "/media/{{twit.image}}" style = "height: 100px">
        {% endif %}
    </div>
    <form method = "post"  id = "comment">
        {% csrf_token %}
        <input type="text" id = "comment" name = "comment" class="form-control" placeholder="Add comment">
        <input type = "submit" class = "btn btn-primary" value = "Submit" />
</form>
    {% for comment in comments %}
        <div class="alert alert-secondary" role="alert">
            <a href = "{% url 'user' twit.author.login %}">{{twit.author.login}}</a>: {{comment.content}}<br>
        </div>
    {% endfor %}
{% endblock %}
```

## Post a twit

```python
urls.py

path('twits/add', add_twit, name = 'add_twit'),
```

```python
twits/views.py

def add_twit(request):
    context = dict()
    if (request.method == 'POST'):
        user = Account.objects.get(login = request.session['user'])
        content = request.POST['content']
        try:
            image = request.FILES['image']
            has_image = True
        except:
            has_image = False
        
        if (has_image):
            twit = Twit(author = user, content = content, image = image)
        else:
            twit = Twit(author = user, content = content)
        twit.save()
        context['success'] = True
        return render(request, 'app/add_twit.html', context)
    else:
        return render(request, 'app/add_twit.html', context)
    return render(request, 'app/add_twit.html', context)
```


```html
templates/app/add_twit.html
{% extends 'base.html' %}

{% block title%}Add Twit page{% endblock %}

{% block body %}
    
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        <label for="content">: </label>
        <input id="content" type="text" name="content">
        <label for="image">Your image: </label>
        <input type="file" name = "image">
        <input type="submit" value="Send">
    </form>

    {% if success %}
        <br> Twit was added!
    {% endif %}

{% endblock %}
```

## Adding follow button

```python
accounts/views.py

def user(request, login):
    context = dict()
    try:
        user = Account.objects.get(login = login)
        context['user'] = user
        me = Account.objects.get(login = request.session['user'])
        context['button'] = not (user in me.follows.all())
        if (request.method == 'POST'):
            me.follows.add(user)
            me.save()

        try:
            twits = Twit.objects.filter(author = user)
            context['twits'] = twits
        except:
            context['twits'] = []


        follows = user.follows.all()
        context['follows'] = follows
        

        
        return render(request, 'app/user.html', context)
    except:
        return render(request, 'general/404.html', context)

    return render(request, 'app/user.html', context)

```

```html
{% extends 'base.html' %}

{% block title%}User page{% endblock %}

{% block body %}
    <div class="container">
        <div class="row">
            <div class="col-8">
                {% for twit in twits %}
                    <div class="alert alert-primary" role="alert">
                        {{twit.content}}
                    </div>
                {% empty %}
                    <div class="alert alert-danger" role="alert">
                        No twits yet
                    </div>
                {% endfor %}
            </div>
            <div class="col-4">
                <div class="card" style="width: 18rem;">
                <img src="/media/{{user.image}}" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">{{user.login}}</h5>
                        {% if button %}
                            <form method = "post">{% csrf_token %}<input type = "submit" name = "submit" value = "Follow" class = "btn btn-light"></form>
                        {% endif %}
                    </div>
                </div>
            </div>
        </div>
    </div>

    
{% endblock %}
```
