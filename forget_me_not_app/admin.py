from django.contrib import admin

# Register your models here.
from .models import Memo, Category

admin.site.register(Memo)
admin.site.register(Category)