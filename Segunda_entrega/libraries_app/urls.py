from django.urls import path
from libraries_app import views

urlpatterns = [
    path('', views.home, name='Home')
]

urlpatterns += [
    path('register/', views.register, name='Sign Up')
]

urlpatterns += [
    path('books/', views.books_page, name='Libros')
]

urlpatterns += [
    path('libraries/', views.libraries_page,name='Biblioteca')
]

urlpatterns += [
    path('login/', views.login, name='Log In')
]

urlpatterns += [
    path('loadUser/', views.UsersFormularios, name="UsersFormularios"),
    path('loadBook/',views.BooksFormularios,name='BooksFormularios'),
    path('loadLibrary', views.LibrariesFormularios,name='LibrariesFormularios')
]