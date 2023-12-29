import json
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

from .models import *

# Create your views here.


def index(request):
    return render(request, 'api/index.html')


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        subject = request.POST["subject"]
        email = request.POST["email"]
        body = request.POST["body"]
        
        try:
            contact_info = FormData.objects.create(name=name, subject=subject, email=email, body=body)
            contact_info.save()
        except IntegrityError as err:
            print(err)
        
        return redirect(reverse("index"))
    
    return redirect(reverse("index"))
        
        
        

