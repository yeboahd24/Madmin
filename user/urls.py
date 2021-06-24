from django.urls import path
from .views import login_view, register, home, list_categories, post, comments,\
logout_view

urlpatterns = [
    path('', home, name="home"),
    path('login/', login_view, name='login'),
    path('register/', register, name="register"),
    path('categories/', list_categories, name="categories"),
    path('posts/', post, name="posts"),
    path('comments/', comments, name='comments'),
    path('logout/', logout_view, name='logout'),

    
]
