# Generated by Django 4.1.5 on 2023-02-20 10:16

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0008_cart"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="product",
            name="specification",
            field=ckeditor.fields.RichTextField(),
        ),
    ]