from django.urls import path
from . import views 

urlpatterns = [
    path('',views.Index,name="index"),
    path('blog-list/',views.Blog,name="blog"),
]
