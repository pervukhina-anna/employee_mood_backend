# Generated by Django 4.2.1 on 2023-06-11 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("metrics", "0008_alter_question_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="text",
            field=models.TextField(max_length=800, verbose_name="Текст вопроса"),
        ),
    ]
