from django.contrib import admin

from .models import Postagem

# Register your models here.


class PostagemAdmin(admin.ModelAdmin):
    list_display = ('titulo','slug','status','created_on')
    list_filter = ("status",)
    search_fields = ['titulo','conteudo']
    prepopulated_fields = {'slug': ('titulo',)}


admin.site.register(Postagem,PostagemAdmin)
