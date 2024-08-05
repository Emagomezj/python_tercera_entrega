from django.contrib import admin
from .models import Users,Books,Users_libraries

# Register your models here.
admin.site.register(Users)
admin.site.register(Books)
admin.site.register(Users_libraries)