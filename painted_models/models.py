from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


def thumbnail_path_file_name(instance, filename):
    return '/'.join(filter(None, (instance.name, filename)))


def gallery_path_file_name(instance, filename):
    return '/'.join(filter(None, (instance.figure.name, filename)))


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
    description = models.CharField(max_length=300)
    thumbnail = models.ImageField(null=True, blank=True, upload_to=thumbnail_path_file_name,
                                  height_field=None,
                                  width_field=None,
                                  max_length=100)
    tags = models.ManyToManyField(Tag, null=True)

    def __str__(self):
        return self.name


class FigureImages(models.Model):
    figure_key = models.ForeignKey(Figure, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to="test_template/")
