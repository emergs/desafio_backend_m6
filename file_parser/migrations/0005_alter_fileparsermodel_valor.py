# Generated by Django 4.1.5 on 2023-01-30 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("file_parser", "0004_remove_fileparsermodel_dono_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fileparsermodel",
            name="valor",
            field=models.CharField(max_length=12),
        ),
    ]
