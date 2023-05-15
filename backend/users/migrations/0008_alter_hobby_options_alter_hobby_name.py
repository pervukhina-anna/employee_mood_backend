# Generated by Django 4.2.1 on 2023-05-15 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_remove_position_departments_position_department"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="hobby",
            options={"verbose_name": "Интерес", "verbose_name_plural": "Интересы"},
        ),
        migrations.AlterField(
            model_name="hobby",
            name="name",
            field=models.CharField(
                max_length=255, unique=True, verbose_name="Наименование"
            ),
        ),
    ]
