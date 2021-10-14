from django.shortcuts import render,redirect
from .models import Image

def index(request):
    images = Image.objects.all()
    return render(request, "index.html", {"images": images})


def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"
        if len(searched_images) > 0:
            return render(request, 'search.html', {"message": message, "images": searched_images})
        else:
            return render(request, 'search.html', {"message": message, "term_included": True})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message, "term_included": False})

def image_location(request, location):
    images = Image.filter_by_location(location)
    return render(request, 'location.html', {'images': images})
