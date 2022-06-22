from django.contrib import admin
from .models import Figure, FigureImages, Tag


class FigureImagesInline(admin.TabularInline):
    model = FigureImages
    extra = 3


class FigureAdmin(admin.ModelAdmin):
    inlines = [ FigureImagesInline, ]


class FigureImagesAdmin(admin.ModelAdmin):
    fields = ('figure_key', 'images')


class FigureTagsAdmin(admin.ModelAdmin):
    fields = ('tag_name',)


admin.site.register(Figure, FigureAdmin)
admin.site.register(FigureImages, FigureImagesAdmin)
admin.site.register(Tag, FigureTagsAdmin)