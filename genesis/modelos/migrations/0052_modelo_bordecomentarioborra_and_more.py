# Generated by Django 4.1.1 on 2023-08-13 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0051_columna_dimensionesimagen_columna_margeninterno'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelo',
            name='bordecomentarioborra',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='modelo',
            name='bordecomentarioinserta',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='modelo',
            name='bordecomentariolista',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='modelo',
            name='bordecomentarioupdate',
            field=models.BooleanField(default=False),
        ),
    ]
