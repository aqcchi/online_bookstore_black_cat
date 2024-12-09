from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('', include('authors.urls')),
    path('', include('common.urls')),
    path('', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
