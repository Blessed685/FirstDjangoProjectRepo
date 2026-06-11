from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def homepage(request: HttpRequest) -> HttpResponse:
    return render(request, "core/home.html")

def about_page(request: HttpRequest) -> HttpResponse:
    return render(request, "core/about.html")

def contact_page(request: HttpRequest) -> HttpResponse:
    return render(request, "core/contact.html")