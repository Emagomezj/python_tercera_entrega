from django import forms
from .models import Users, Books, Users_libraries

class UsersFormulario(forms.Form):
    name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=30)

class BooksFormulario(forms.Form):
    name = forms.CharField(max_length=40)
    author = forms.CharField(max_length=40)
    year = forms.DateField()
    editorial = forms.CharField(max_length=40)
    edition = forms.CharField(max_length=40)
    available = forms.BooleanField()
    
class LibrariesFormulario(forms.Form):
    user = forms.ModelChoiceField(queryset=Users.objects.all())
    books = forms.ModelMultipleChoiceField(queryset=Books.objects.all(), widget=forms.CheckboxSelectMultiple)
    available = forms.BooleanField()