from multiprocessing import context
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from accounts.models import CustomUser

def user_profile(request, username):
    if request.user.is_authenticated:
        user_profile = CustomUser.objects.all().filter(username=username)
    else:
        return HttpResponseNotFound('Page Not Found 404')
    context = {
        'user_profile':user_profile,
    }
    return render(request, 'user_profile/profile.html', context)
