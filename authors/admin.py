from django.urls import reverse
from django.contrib import admin
from django.utils.html import format_html
from authors.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = ('formatted_name', 'get_books',)
    search_fields = ('last_name', 'first_name',)
    ordering = ('last_name',)
    readonly_fields = ('get_books',)

    def formatted_name(self, obj):
        return f"{obj.last_name}, {obj.first_name}"

    formatted_name.short_description = 'Full name'

    def get_books(self, obj):
        books = obj.books.all()
        if books:
            return format_html(
                ", ".join(
                    f'<a href="{reverse("admin:books_book_change", args=[book.id])}">{book.title}</a>'
                    for book in books
                )
            )
        return "No books"

    get_books.short_description = 'Books by author'
