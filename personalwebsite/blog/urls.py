from django.urls import path
from . import views
app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path("search/",views.blog_search, name = "blog_search"),
    path("register/", views.register, name= "register"),
    path("logout/", views.logout, name = "logout")
]