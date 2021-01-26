from django.urls import path
from . import views
#import include in app urls.py

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login',views.login),
    path('logout', views.logout),
    # wishes path
    path('wishes', views.wishes),
    path('stats', views.stats),
    path('wishes/new', views.new_wish),
    path('create_wish',views.add_wish),
    path('wishes/edit/<int:id>',views.edit_wish),
    path('wishes/delete/<int:id>',views.delete_wish),
    path('granted_wish/<int:id>',views.grant_wish),
    path('like/<int:id>',views.add_like),
]