from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(AdminRegister)
admin.site.register(UserRegister)
admin.site.register(Book)
admin.site.register(BookRecord)
