# Generated by Django 4.1.1 on 2023-03-21 15:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0030_zonareporteadhoc'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReporteAdHocObjeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', ckeditor.fields.RichTextField()),
                ('modeloid', models.IntegerField(default=0)),
            ],
        ),
    ]
