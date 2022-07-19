# Generated by Django 4.0.5 on 2022-07-11 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('printed_models', '0002_alter_printedmodel_webpage_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='printedmodel',
            name='is_resin',
        ),
        migrations.CreateModel(
            name='PrintedModelMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=30)),
                ('figure_key', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='printed_models.printedmodel')),
            ],
        ),
    ]