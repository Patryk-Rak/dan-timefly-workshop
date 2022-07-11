from django.contrib import admin
from .models import Tag, PrintedModel, PrintedModelImage, PrintedModelMaterial


class PrintedModelMaterialInLine(admin.TabularInline):
    model = PrintedModelMaterial
    extra = 1


class FigureImagesInline(admin.TabularInline):
    model = PrintedModelImage
    extra = 3


class PrintedModelAdmin(admin.ModelAdmin):
    inlines = [ PrintedModelMaterialInLine, FigureImagesInline, ]


class PrintedModelMaterialAdmin(admin.ModelAdmin):
    fields = ('figure_key', 'image_name')


class PrintedModelImageAdmin(admin.ModelAdmin):
    fields = ('figure_key', 'image_name')


class FigureTagsAdmin(admin.ModelAdmin):
    fields = ('tag_name', 'featured')


admin.site.register(PrintedModel, PrintedModelAdmin)
admin.site.register(PrintedModelMaterial, PrintedModelMaterialAdmin)
admin.site.register(PrintedModelImage, PrintedModelImageAdmin)
admin.site.register(Tag, FigureTagsAdmin)