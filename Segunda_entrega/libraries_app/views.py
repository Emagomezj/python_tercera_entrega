from django.shortcuts import render
from .models import Users,Books,Users_libraries
from libraries_app.forms import UsersFormulario,BooksFormulario,LibrariesFormulario,SearchBooks

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

def UsersFormularios(request):
    if request.method == "POST":
        mi_formulario = UsersFormulario(request.POST) 
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            user = Users(name=informacion["name"], surname=informacion["surname"],email=informacion["email"])

            user.save()
            return render(request, "libraries_app/home.html")
    else:
        mi_formulario = UsersFormulario()

    return render(request, "libraries_app/forms_page.html.html", {"mi_formulario": mi_formulario})

def BooksFormularios(request):
    if request.method == "POST":
        mi_formulario = BooksFormulario(request.POST) 
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            book = Books(name = informacion["name"],author = informacion["author"],
                        year = informacion["year"],
                        editorial = informacion["editorial"],
                        edition = informacion["edition"],
                        available = informacion["available"])

            book.save()
            return render(request, "libraries_app/home.html")
    else:
        mi_formulario = BooksFormulario()

    return render(request, "libraries_app/forms_page.html", {"mi_formulario": mi_formulario})

def LibrariesFormularios(request):
    if request.method == "POST":
        mi_formulario = LibrariesFormulario(request.POST) 
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            library = Users_libraries(user=informacion['user'],available=informacion['available'])
            

            library.save()
            library.books.set(informacion['books'])
            return render(request, "libraries_app/home.html")
    else:
        mi_formulario = LibrariesFormulario()

    return render(request, "libraries_app/forms_page.html", {"mi_formulario": mi_formulario})

def Search(request):
    if request.method == "POST":
        miFormulario = SearchBooks(request.POST) # Aqui me llega la informacion del html

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            books = Books.objects.filter(name__icontains=informacion["book"])

            return render(request, "libraries_app/results.html", {"books": books})
    else:
        miFormulario = SearchBooks()

    return render(request, "libraries_app/search.html", {"miFormulario": miFormulario})