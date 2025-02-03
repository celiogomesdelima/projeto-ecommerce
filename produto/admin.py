from django.contrib import admin
from produto import models

# Register your models here.


class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    extra = 1
    
@admin.register(models.Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = 'nome',
    ordering = '-id',
    list_display_links = 'nome',
    inlines = [
        VariacaoInline
    ]

@admin.register(models.Variacao)
class VariacaoAdmin(admin.ModelAdmin):
    list_display = 'nome',
    ordering = '-id',
    list_display_links = 'nome',