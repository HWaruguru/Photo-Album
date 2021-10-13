from django.shortcuts import render,redirect
from .models import Image

def index(request):
    images = Image.objects.all()
    return render(request, "index.html", {"images": images})
