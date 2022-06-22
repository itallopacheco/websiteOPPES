import imp

from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.ListaPostagem.as_view(), name='home'),
    path('<slug:slug>/', views.DetalhesPostagem.as_view(),name='post_detail'),

]
