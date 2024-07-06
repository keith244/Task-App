from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns =[
    path('',views.index, name='index'),
    #CRUD OPERATIONS BEGIN HERE
    path('<int:task_id>/',views.task_detail, name='detail'),
]
