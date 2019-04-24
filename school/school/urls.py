"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import(
    home,
    student,
    delete_student,
    add_student,
    teacher,
    delete_teacher,
    add_teacher,
    subject,
    delete_subject,
    add_subject
)

urlpatterns = [
    path('', home),
    path('home', home),
    path('admin/', admin.site.urls),
    path('student/', student),
    path('student/added', add_student),
    path('student/removed', delete_student),
    path('subject/', subject),
    path('subject/added', add_subject),
    path('subject/removed', delete_subject),
    path('teacher/', teacher),
    path('teacher/added', add_teacher),
    path('teacher/removed', delete_teacher)
]
