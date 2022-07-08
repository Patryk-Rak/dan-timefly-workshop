from django.contrib import admin
from .models import PrintedModel, PrintedModelImage, Tag


class FigureImagesInline(admin.TabularInline):
    model = PrintedModelImage
    extra = 3


class PrintedModelAdmin(admin.ModelAdmin):
    inlines = [ FigureImagesInline, ]


class PrintedModelImageAdmin(admin.ModelAdmin):
    fields = ('figure_key', 'image_name')


class FigureTagsAdmin(admin.ModelAdmin):
    fields = ('tag_name', 'featured')


admin.site.register(PrintedModel, PrintedModelAdmin)
admin.site.register(PrintedModelImage, PrintedModelImageAdmin)
admin.site.register(Tag, FigureTagsAdmin)