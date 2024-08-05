from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'libraries_app/home.html')

def register(request):
    return render(request,'libraries_app/register.html')

def books_page(request):
    return render(request,'libraries_app/books.html')

def libraries_page(request):
    return render(request,'libraries_app/library.html')

def login(request):
    return render(request,'libraries_app/login.html')