from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import usersForm

def Userform(request):
    finalans=0
    fn=usersForm()
    data={'form':fn}
    return render(request,'usersform.html',data)

def Submitform(request):
    finalans=None
    try:
        if request.method == "POST":
            form = usersForm(request.POST)
            if form.is_valid():
                num1 = int(form.cleaned_data['num1'])
                num2 = int(form.cleaned_data['num2'])
                finalans = num1 + num2
    except:
        pass
    return HttpResponse(finalans)




# def home(request):
#     data={
#         'title':"Home pagev ok",
#         'bdata':"Welcome to wscubetech",
#         'clist':["java","python","django"],
#         'numbers':[10,20,30,50,89,100],
#         'students_details':[
#             {'name':'pradeep','phone':9012747344},
#             {'name':'testing','phone':46373479734},

#             ]
#     }
#     return render(request,'index.html',data)

def home(request):
    return render(request,'index1.html')

def Aboutus(request):
    output=None
    if request.method=="GET":
        output=request.GET.get('output')
 
    return render(request,'aboutus.html',{'output':output})


def Contactus(request):
    finalans=None
    try:
        if request.method=="POST":
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            finalans=n1+n2
        print(n1+n2)
        context={'output':finalans}
        url="/about-us/?output={}".format(finalans)
        return HttpResponseRedirect(url)
        return redirect(url)

    except:
        pass
    
    return render(request,'contact.html',{'output':finalans})

def Service(request):
    return render(request,'service.html')

# def Submitform(request):
#     finalans=None
#     try:
#         if request.method=="POST":
#             n1=int(request.POST.get('num1'))
#             n2=int(request.POST.get('num2'))
#             finalans=n1+n2
#         print(n1+n2)
#         context={'output':finalans}
#     except:
#         pass
#     return HttpResponse(finalans)

def aboutus(request):       
    return HttpResponse("Hello to Wscubetech")

def course(request):
    return HttpResponse("welcome to wscubetech")



def coursedetails(request,courseid):
    return HttpResponse(courseid)