# Generated by Django 4.1.5 on 2023-01-27 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("file_parser", "0003_alter_fileupload_file_parser"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="fileparsermodel",
            name="dono",
        ),
        migrations.RemoveField(
            model_name="fileparsermodel",
            name="loja",
        ),
        migrations.AddField(
            model_name="fileparsermodel",
            name="dono_da_loja",
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="fileparsermodel",
            name="nome_da_loja",
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="fileparsermodel",
            name="hora",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="fileparsermodel",
            name="tipo",
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name="fileupload",
            name="file_parser",
            field=models.FileField(upload_to="storeged_file"),
        ),
    ]