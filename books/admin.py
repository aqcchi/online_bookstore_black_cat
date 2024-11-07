from django.contrib import admin
from .models import Book, Order


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
    # list_display = ('title', 'author', 'price', 'book_available')
    # list_filter = ('book_available', 'author')
    # search_fields = ('title', 'author')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

