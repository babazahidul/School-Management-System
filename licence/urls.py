from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.licence, name="licence"),
    path('search/', views.search_licence, name="search-licence")
]