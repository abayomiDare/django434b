from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from .forms import *


def print_hello(request):
    return HttpResponse('Hello World')


def add_age(request, a, b):
    return HttpResponse(a + b)


def json_intro(request, name, age):
    file = dict([('name', name),
                ('age', age)
                 ])
    return JsonResponse(file)


def myfirstpage(request):
    return render(request, 'index.html')


def secondpage(request):
    return render(request, 'second.html')


def thirdpage(request):
    num1, num2 = 10, 67
    ans = num1 > num2
    var = 'userNames Needed'
    fruit = ['apple', 'banna', 'mango', 'pineapple', 'cashewnut']
    dictionary = dict([('var', var),
                       ('fruits', fruit),
                       ('num1', num1),
                       ('num2', num2),
                       ('answer', ans)
                       ])
    return render(request, 'thirdpage.html', context=dictionary)


def myimagepage(request):
    return(render(request, 'imagepage.html'))


def myform(request):
    return render(request, 'myform.html')


def submitmyform(request):

    # myDictonary = {
    #     'var1': request.GET['mytext'],
    #     'var2': request.GET['mytextarea'],
    #     'method': request.method
    # }
    # return JsonResponse(myDictonary)
    myDictonary = {
        'var1': request.POST['mytext'],
        'var2': request.POST['mytextarea'],
        'method': request.method
    }
    return JsonResponse(myDictonary)


def myform2(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            print(title)
            print(subject)
            var = str('form submitted' + str(request.method))
            return HttpResponse(var)
        else:
            mydictionary = {
                'form' : form
            }
            return render(request, 'myform2.html', context=mydictionary)
    elif request.method == 'GET':
        form = FeedBackForm()
        mydictionary = {
            'form':form
        }
        return render(request, 'myform2.html', context=mydictionary)

