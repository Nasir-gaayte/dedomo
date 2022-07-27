from django.shortcuts import render
from note_app.models import Users_model
from note_app.forms import UserData
from django.core  import validators



# Create your views here.

def index(request):
    data = Users_model.objects.order_by('username')
    dict = {'intohtml': data}
    return render(request, 'note_app/index.html', context=dict)


def user_view(request):
    form_data = UserData()
    if request.method == 'POST':
        form_data = UserData(request.POST)
        
        if form_data.is_valid():
            form_data.save(commit=True)
            return index(request)
        else:
            print("ErrOr")
    
    return render(request, 'note_app/user.html', {'gogit': form_data})

    