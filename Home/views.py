from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact

# Create your views here.
def index(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        comment = request.POST.get("comment")
        contact = Contact(name=name, email=email, phone=phone, comment=comment, date=datetime.today()) 
        contact.save()
    return render(request, 'contact.html')
    