# Generated by Django 3.0.8 on 2020-07-27 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20200727_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='./img/default.png', upload_to=None),
        ),
    ]
