from django.shortcuts import render
from .models import contactus
from django.http import HttpResponseRedirect
# Create your views here.

from django.shortcuts import render

def signin(request):
    return render(request,'signin.html') 
def contact(request):
    return render(request,'contact.html')   
def index(request):
    return render(request,'index.html')  
def login(request):
    return render(request,'login.html')

def insert(request):
     if request.method == 'POST':
         contactus_model=contactus(
             firstname=request.POST['fname'],
             lastname=request.POST['lname'],
             message=request.POST['message'],)
         contactus_model.save()
         return HttpResponseRedirect('')
     else:
         return render(request,'login.html')
         