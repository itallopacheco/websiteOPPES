import imp

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


STATUS = (
    (0, "Rascunho"),
    (1, "Publicado"),
)

class Postagem(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    autor = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    conteudo = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS,default=0)


    class Meta:
        ordering = ['-created_on']

    def __str__(self) :
        return self.titulo
