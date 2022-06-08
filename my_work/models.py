from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Figure(models.Model):
    name = models.CharField(max_length=30)
    height = models.IntegerField(validators=[
                                   MaxValueValidator(1000),
                                   MinValueValidator(1)
                               ]
                               )
    is_resin = models.BooleanField()
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='uploads/brand/', height_field=None, width_field=None, max_length=100)
    images = models.FileField(blank=True)

    def __str__(self):
        return self.figure.name


def path_file_name(instance, filename):
    return '/'.join(filter(None, (instance.figure.name, filename)))


class FigureImages(models.Model):
    figure = models.ForeignKey(Figure, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to=path_file_name)

    def __str__(self):
        return self.figure.name