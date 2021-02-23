# Generated by Django 3.1.6 on 2021-02-15 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0050_auto_20210213_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngohelper',
            name='image',
            field=models.ImageField(blank=True, help_text='Images should be  more than 500x500px and should be of good quality', max_length=300, upload_to='', verbose_name='Resource Images'),
        ),
        migrations.AlterField(
            model_name='registerngorequest',
            name='description',
            field=models.TextField(blank=True, help_text="Organization's short description - max 500 chars.", max_length=500, verbose_name='Description'),
        ),
    ]
