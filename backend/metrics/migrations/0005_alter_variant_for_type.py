# Generated by Django 4.2.1 on 2023-06-11 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("metrics", "0004_question_mark"),
    ]

    operations = [
        migrations.AlterField(
            model_name="variant",
            name="for_type",
            field=models.BooleanField(default=False, verbose_name="Под типовой опрос"),
        ),
    ]