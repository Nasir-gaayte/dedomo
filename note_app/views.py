from django.shortcuts import render
from requests import request
from note_app.models import Users


# Create your views here.

def index(request):
    data = Users.objects.order_by('username')
    dict = {'intohtml': data}
    return render(request, 'note_app/index.html', content_type=dict)


def user_view(request):
    form = Users()
    if request.method == 'POST':
        form = Users(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ErrOr")
    
    return render(request, 'note_app/user.html')

    