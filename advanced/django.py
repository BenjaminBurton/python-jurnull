# Web Development with Python: Advanced Python

# .3.4.2 Django:

# Django is a high-level web framework for Python that encourages rapid development and clean, pragmatic design. It follows the "batteries-included" philosophy and provides everything needed to build web applications.

# Example: Creating a Simple Django App
# Step 1: Create a new Django project
# $ django-admin startproject myproject

# Step 2: Create a new Django app
# $ python manage.py startapp myapp

# Step 3: Define views in myapp/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")

# Step 4: Configure URL routing in myproject/urls.py
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
]

# Step 5: Run the development server
# $ python manage.py runserver
