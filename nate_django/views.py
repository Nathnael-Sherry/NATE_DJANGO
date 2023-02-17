from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def services(request):
    return render(request, "services.html")

def about2(request):
    return render(request, "about2.html")

def testimonials(request):
    return render(request, "testimonials.html")

def contact2(request):
    return render(request, "contact2.html")

def services2(request):
    return render(request, "services2.html")

def index(request):
    return render(request, "index.html")