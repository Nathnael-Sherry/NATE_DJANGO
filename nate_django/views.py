from django.shortcuts import render
from .forms import user_reg
from .forms import members_reg


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


def reg(request):
    submit_button = request.POST.get("sherry")
    name = ''
    email = ''
    password = ''

    reg_form = user_reg(request.POST or None)
    if reg_form.is_valid():
        name = reg_form.cleaned_data.get("name")
        email = reg_form.cleaned_data.get("email")
        password = reg_form.cleaned_data.get("password")
    context = {'reg_form': reg_form, 'name': name, 'email': email, 'password': password, 'submit_button': submit_button}
    return render(request, 'register.html', context)

def members(request):
    submit_members = request.POST.get("members")
    Name =''
    Age =''
    Phone =''
    City =''
    Country =''

    reg_members_form = members_reg(request.POST or None)
    if reg_members_form.is_valid():
        Name = reg_members_form.cleaned_data.get("Name")
        Age = reg_members_form.cleaned_data.get("Age")
        Phone = reg_members_form.cleaned_data.get("Phone")
        City = reg_members_form.cleaned_data.get("City")
        Country = reg_members_form.cleaned_data.get("Country")
    context = {'reg_members_form': reg_members_form,
               'Name':Name,
               'Age':Age,
               'Phone':Phone,
               'City':City,
               'Country':Country,
               'submit_members':submit_members
    }
    return render(request, 'members.html',context)