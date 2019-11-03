from django.urls import path
from .import views

urlpatterns = [
    path("", views.products, name="products"),
    path("policies/", views.policies, name="policies")
]