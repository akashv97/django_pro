from django.shortcuts import render, HttpResponse
from datetime import datetime
from akash.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("this is homepage")
def about(request):
     return render(request,'about.html')
   # return HttpResponse("this is about Page")
def Service(request):
     return render(request,'service.html')
   # return HttpResponse("this is service page")
def contact(request):
   if request.method == "POST":
      email=request.POST.get('email')
      name=request.POST.get('name')
      phone=request.POST.get('phone')
      desc=request.POST.get('desc')
      contact=Contact(email=email, name=name, phone=phone, desc=desc, date=datetime.today())
      contact.save()
      messages.success(request, 'welldone Submited!!!!')
   return render(request,'contact.html')
   # return HttpResponse("this is contact page")            
