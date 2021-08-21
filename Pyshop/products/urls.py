from django.urls import path
from . import views


# products/1/New
urlpatterns = [
    path('', views.index),
    path('New',views.new)
]