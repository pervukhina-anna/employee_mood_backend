# Generated by Django 4.2.1 on 2023-06-11 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("metrics", "0006_remove_variant_for_type_survey_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="text",
            field=models.CharField(max_length=500, verbose_name="Текст вопроса"),
        ),
        migrations.AlterField(
            model_name="survey",
            name="description",
            field=models.TextField(
                blank=True, max_length=800, null=True, verbose_name="Описание опроса"
            ),
        ),
    ]
