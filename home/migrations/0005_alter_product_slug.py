# Generated by Django 4.1.5 on 2023-02-09 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_review"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="slug",
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
