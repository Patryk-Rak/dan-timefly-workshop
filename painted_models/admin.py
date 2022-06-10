from django.contrib import admin
from .models import Figure, FigureImages


class FigureImagesInline(admin.TabularInline):
    model = FigureImages
    extra = 3


class FigureAdmin(admin.ModelAdmin):
    inlines = [ FigureImagesInline, ]


class FigureImagesAdmin(admin.ModelAdmin):
    fields = ('figure_key', 'images')

admin.site.register(Figure, FigureAdmin)
admin.site.register(FigureImages, FigureImagesAdmin)