# Generated by Django 4.1.1 on 2023-08-08 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0022_columna_dimensionesimagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='columna',
            name='margeninterno',
            field=models.CharField(default='0px', max_length=6),
        ),
    ]