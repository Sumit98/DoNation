# Generated by Django 3.1.6 on 2021-02-17 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0057_auto_20210217_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngohelper',
            name='resource_image',
            field=models.ImageField(blank=True, help_text='Images should be  more than 500x500px and should be of good quality', upload_to='', verbose_name='Resource Images'),
        ),
    ]
