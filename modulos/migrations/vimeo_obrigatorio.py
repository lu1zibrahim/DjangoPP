# Generated by Django 3.2.9 on 2021-11-25 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0008_aula_vimeo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='vimeo_id',
            field=models.CharField(max_length=32),
        ),
    ]
