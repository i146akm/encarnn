# Generated by Django 5.2.1 on 2025-05-27 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_textpage_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textpage',
            name='meta_title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Заголовок страницы'),
        ),
    ]
