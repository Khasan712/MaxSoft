from multiprocessing import context
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render

# Create your views here.
from . models import Lessons, Module, Courses


def courses(request):
    courses = Courses.objects.all().filter(status=True)

    if request.user.is_authenticated:
        courses = Courses.objects.all().filter(course_mentor__username=request.user, status=True)[::-1]
    else:
        return HttpResponseNotFound('Page Not Found 404')
    
    context = {
        'courses':courses
    }
    return render(request, 'courses/course_page.html', context)


def view_course(request, slug):
    course_mentor = Courses.objects.filter(course_mentor__username=request.user)
    if request.user.is_authenticated and course_mentor:
        course = Courses.objects.get(slug=slug, course_mentor__username=request.user)
    else:
        return HttpResponseNotFound('Page not found 404')
        
    context = {
        'course':course,
        'course_mentor':course_mentor,
    }
    return render(request, 'courses/view_course.html', context)


def view_module(request, slug):
    modules = Module.objects.get(slug=slug)
    
    context = {
        'modules':modules,
    }
    return render(request, 'courses/module.html', context)



