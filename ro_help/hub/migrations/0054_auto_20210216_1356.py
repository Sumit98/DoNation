# Generated by Django 3.1.6 on 2021-02-16 13:56

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0053_auto_20210216_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngohelper',
            name='image',
            field=models.ImageField(blank=True, help_text='Images should be  more than 500x500px and should be of good quality', max_length=300, storage=django.core.files.storage.FileSystemStorage(), upload_to='', verbose_name='Resource Images'),
        ),
    ]
