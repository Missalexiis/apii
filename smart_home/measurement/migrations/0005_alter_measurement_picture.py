# Generated by Django 4.1.3 on 2022-12-04 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("measurement", "0004_alter_measurement_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="measurement",
            name="picture",
            field=models.ImageField(default=None, upload_to="pictures/"),
        ),
    ]
