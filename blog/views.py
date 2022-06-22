from django.shortcuts import render
from django.views import generic

from .models import Postagem

# Create your views here.

class ListaPostagem(generic.ListView):
    queryset = Postagem.objects.filter(status=1).order_by('-created_on')



class DetalhesPostagem(generic.DetailView):
    model = Postagem
    template_name = 'postagem_details.html'
