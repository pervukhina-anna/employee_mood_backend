# Generated by Django 4.2.1 on 2023-05-24 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0003_entry_preview_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entry",
            name="preview_image",
            field=models.ImageField(
                upload_to="entries/", verbose_name="Превью-изображение записи"
            ),
        ),
    ]