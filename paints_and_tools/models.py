from django.db import models


class Brand(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/brand/', height_field=None, width_field=None, max_length=100)


class Paint(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/paints/', height_field=None, width_field=None, max_length=100)


class Chemicals(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/chemicals/', height_field=None, width_field=None, max_length=100)


class Tool(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/tools/', height_field=None, width_field=None, max_length=100)


class Accessory(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/accessories/', height_field=None, width_field=None, max_length=100)