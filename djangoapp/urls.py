from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about-us/',views.Aboutus,name='aboutus'),
    path('service/',views.Service,name='service'),
    path('contact-us/',views.Contactus,name='contactus'),
    path('about-us/',views.aboutus,name='aboutus'),
    path('course/',views.course,name='course'),
    path('course/<int:courseid>',views.coursedetails,name='coursedetails'),
    path('course/<str:courseid>',views.coursedetails,name='coursedetails'),
    path('course/<slug:courseid>',views.coursedetails,name='coursedetails'),
    path('course/<courseid>',views.coursedetails,name='coursedetails'),
    path('submitform/',views.Submitform,name='submitform'),
    path('userfrom/',views.Userform,name='userform'),
]
