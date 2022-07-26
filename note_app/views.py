from django.shortcuts import render
from requests import request



# Create your views here.

def index(request):
    return render(request, 'note_app/index.html')


def user(request):
    return render(request, 'note_app/user.html')
    