# Generated by Django 4.1.1 on 2023-03-03 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0024_zonareporte'),
    ]

    operations = [
        migrations.AddField(
            model_name='zonareporte',
            name='modeloid',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]