from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Book, Order


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ('title', 'get_authors', 'price', 'book_available',)
    list_filter = ('book_available',)
    search_fields = ('title',)
    ordering = ('title',)

    def get_authors(self, obj):
        authors = obj.authors.all()  # getting all authors for this book
        if authors:
            # generating clickable links for each author
            return format_html(
                ", ".join(
                    f'<a href="{reverse("admin:authors_author_change", args=[author.id])}">{author.first_name} {author.last_name}</a>'
                    for author in authors
                )
            )
        return "No authors"

    get_authors.short_description = 'Authors'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('ordered_book', 'user', 'created_at')
    search_fields = ('ordered_book__title', 'user__username')
    ordering = ('created_at',)
