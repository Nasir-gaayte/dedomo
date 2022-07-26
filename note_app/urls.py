from django.urls import path
from note_app import views


urlpatterns = [
    path('',views.index, name='index'), 
    path('user/',views.user, name='user'),
]


