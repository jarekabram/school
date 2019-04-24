from django.http import HttpResponse
from django.db import models
from django.shortcuts import render
from .models import Teacher
from .models import Student
from .models import Subject

def home(request):
    return render(request, "home.html")

def teacher(request):
    teachers = Teacher.objects.all()
    return render(request, "teacher.html", {'teachers': teachers})

def student(request):
    students = Student.objects.all()
    return render(request, "student.html", {'students': students})

def subject(request):
    subjects = Subject.objects.all()
    return render(request, "subject.html", {'subjects': subjects})

def delete_student(request):
    removal_list = request.GET.getlist('item')

    for rem in removal_list:
        Student.objects.get(pk=rem).delete()

    students = Student.objects.all()
    return render(request, "removed_students.html", {'students': students})

def delete_subject(request):
    removal_list = request.GET.getlist('item')

    for rem in removal_list:
        Subject.objects.get(pk=rem).delete()

    subjects = Subject.objects.all()
    return render(request, "removed_subjects.html", {'subjects': subjects})

def delete_teacher(request):
    removal_list = request.GET.getlist('item')

    for rem in removal_list:
        Teacher.objects.get(pk=rem).delete()

    teachers = Teacher.objects.all()
    return render(request, "removed_teacher.html", {'teachers': teachers})

def add_student(request):
    name = request.GET.get('name')
    student = Student.objects.create(name=name)
    student.save()

    return render(request, "item_added.html")

def add_teacher(request):
    name = request.GET.get('name')
    website = request.GET.get('website')

    teacher = Teacher.objects.create(name=name, website=website)
    teacher.save()

    return render(request, "item_added.html")

def add_subject(request):
    name = request.GET.get('name')
    teacher_name = request.GET.get('teacher')
    teacher = Teacher.objects.get(name=teacher_name)
    
    subject = Subject.objects.create(name=name, teacher=teacher)
    subject.save()

    return render(request, "item_added.html")