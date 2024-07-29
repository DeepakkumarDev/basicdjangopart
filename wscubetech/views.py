from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data={
        'title':"Home pagev ok",
        'bdata':"Welcome to wscubetech",
        'clist':["java","python","django"]
    }
    return render(request,'index.html',data)


def aboutus(request):
    return HttpResponse("Hello to Wscubetech")

def course(request):
    return HttpResponse("welcome to wscubetech")



def coursedetails(request,courseid):
    return HttpResponse(courseid)