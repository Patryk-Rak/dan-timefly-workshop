# Generated by Django 4.0.5 on 2022-07-07 08:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('painted_models', '0002_figure_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='figure',
            name='webpage_body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
