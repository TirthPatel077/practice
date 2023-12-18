from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data={
        'new':'sankalp',
        'wow':['tirth','ayush','chatta'],
        'student':[
            
               {'name':'tirth' , 'phone':'8320745443'},
               {'name':'ayush','phone':'9664834516'}
            
        ]
    }
    return render(request,"Home.html",data)

def aboutus(request):
    return HttpResponse("Hii , how are you?")
def aboutus1(request,id):
    return HttpResponse(id)
def no(request):
    data={
        'new':'sankalp',
        'wow':['tirth','ayush','chatta'],
        'student':[
            
               {'name':'tirth' , 'phone':'8320745443'},
               {'name':'ayush','phone':'9664834516'}
            
        ]
    }
    return render(request,"no.html",data)