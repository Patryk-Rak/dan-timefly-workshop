from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify


def thumbnail_path_file_name(instance, filename):
    return '/'.join(filter(None, (instance.name, filename)))


def gallery_path_file_name(instance, filename):
    return '/'.join(filter(None, ('gallery', filename)))


class Tag(models.Model):
    tag_name = models.CharField(max_length=200)
    featured = models.BooleanField(default=False)

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
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        if self.slug == None:
            slug = slugify(self.name)
            has_slug = Figure.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.name) + '-' + str(count)
                has_slug = Figure.objects.filter(slug=slug).exists()

            self.slug = slug

        super().save(*args, **kwargs)



class FigureImages(models.Model):
    figure_key = models.ForeignKey(Figure, default=None, on_delete=models.CASCADE)
    image_name = models.ImageField(upload_to=gallery_path_file_name)
