# Generated by Django 3.0.4 on 2020-03-25 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hub", "0031_auto_20200324_2325"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="ngoneed",
            options={"ordering": ["-urgency"], "verbose_name": "NGO need", "verbose_name_plural": "NGO needs"},
        ),
    ]
