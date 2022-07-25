from django.contrib import admin
from .models import Book, Order, Book_Category, Download



admin.site.register(Book)
admin.site.register(Book_Category)
admin.site.register(Download)
admin.site.register(Order)
