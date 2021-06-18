
from django.urls import path
#from .views import print_hello
from . import views


urlpatterns = [
    #path('hello_world/', print_hello)
    path('', views.print_hello, name='hello world'),
    path('add/<int:a>/<int:b>', views.add_age, name='add'),
    path('intro/<str:name>/<int:age>', views.json_intro, name='intro'),
    path('myfirstpage', views.myfirstpage, name='my_firstpage'),
    path('secondpage', views.secondpage, name='secondpage'),
    path('thirdpage', views.thirdpage, name='thirdpage'),
    path('myimagepage', views.myimagepage, name='myimagepage'),
    path('myform', views.myform, name='myform'),
    path('submitmyform', views.submitmyform, name='submitmyform'),
    path('myform2', views.myform2, name='myform2'),

]
