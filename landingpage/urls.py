from django.urls import path
from . import views 


app_name = 'landing'

urlpatterns = [
    path('',views.Index,name="index"),
    path('blog-list/',views.Blog,name="blog"),
]
