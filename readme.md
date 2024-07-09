
## Basic Django Project Setup Guide

### 1. Install Django

First, ensure you have Python installed on your system. Then, you can install Django using pip:

```bash
pip install django
```

### 2. Create a Django Project

Create a new Django project using the `django-admin` command:

```bash
django-admin startproject projectname
```

### 3. Create a Django App

Navigate into your project directory and create a new app:

```bash
cd projectname
python manage.py startapp appname
```

### 4. Configure Settings

In your project's `settings.py` file, add your app to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    ...
    'appname',
]
```

### 5. Define Models

In `appname/models.py`, define your database models. For example, let's create an `Article` model:

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

### 6. Create and Apply Migrations

Create migrations for your models and apply them to your database:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a Superuser

Create a superuser to access the Django admin:

```bash
python manage.py createsuperuser
```

### 8. Register Models in Admin

In `appname/admin.py`, register your models to make them accessible via the admin interface:

```python
from django.contrib import admin
from .models import Article

admin.site.register(Article)
```

### 9. Define Views

In `appname/views.py`, define your views:

```python
from django.shortcuts import render
from .models import Article

def index(request):
    articles = Article.objects.all()
    return render(request, 'appname/index.html', {'articles': articles})
```

### 10. Configure URLs

In `appname/urls.py`, define URL patterns for your views:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

Include your app's URLs in the project's `urls.py`:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appname/', include('appname.urls')),
]
```

### 11. Create Templates

Create HTML templates in `appname/templates/appname/index.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Index</title>
</head>
<body>
    <h1>Articles</h1>
    <ul>
    {% for article in articles %}
        <li>{{ article.title }}: {{ article.content }}</li>
    {% endfor %}
    </ul>
</body>
</html>
```

### 12. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/appname/` to see your app in action.

### 13. Creating an Article in Django Shell

Follow these steps to create an article using the Django shell:

Open the Django shell:

```bash
python manage.py shell
```

Then, in the shell:

```python
from appname.models import Article

Article.objects.create(title="Test Article", content="This is a test article.")
```

