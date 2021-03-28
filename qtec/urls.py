from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.qtec_problem_0, name="search"),
]