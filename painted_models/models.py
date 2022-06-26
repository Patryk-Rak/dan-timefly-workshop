from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


def thumbnail_path_file_name(instance, filename):
    return '/'.join(filter(None, (instance.name, filename)))


def gallery_path_file_name(instance, filename):
    return '/'.join(filter(None, ('gallery', filename)))


class Tag(models.Model):
    tag_name = models.CharField(max_length=200)

    def __str__(self):
        return self.tag_name


class Figure(models.Model):
    name = models.CharField(max_length=30)
    height = models.IntegerField(validators=[
                                   MaxValueValidator(1000),
                                   MinValueValidator(1)
                               ]
                               )
    is_resin = models.BooleanField()
    description = models.TextField(max_length=3000)
    thumbnail = models.ImageField(null=True, blank=True, upload_to=thumbnail_path_file_name,
                                  height_field=None,
                                  width_field=None,
                                  max_length=100)
    tags = models.ManyToManyField(Tag, null=True)
    painted_date = models.DateField(null=True, blank=True)
    entry_created_at = models.DateTimeField(auto_now_add=True)
    entry_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class FigureImages(models.Model):
    figure_key = models.ForeignKey(Figure, default=None, on_delete=models.CASCADE)
    image_name = models.ImageField(upload_to=gallery_path_file_name)
