# Generated by Django 4.2 on 2023-05-16 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('immobilier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to='photo'),
        ),
    ]
