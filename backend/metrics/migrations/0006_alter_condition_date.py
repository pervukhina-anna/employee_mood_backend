# Generated by Django 4.2.1 on 2023-06-01 09:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("metrics", "0005_alter_condition_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="condition",
            name="date",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                verbose_name="Дата/время добавления показателей",
            ),
        ),
    ]
