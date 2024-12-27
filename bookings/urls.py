from django.urls import path  # Importing path for URL routing
from .views import book_listing  # Importing the booking view

urlpatterns = [
    path('book/', book_listing, name='book_form'),  # URL for the booking form
]