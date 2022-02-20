from django.urls import path
from . import views

urlpatterns = [path("", views.list_blog),
               path("posts/<slug:blog_slug>/", views.blogpost)
               ]
