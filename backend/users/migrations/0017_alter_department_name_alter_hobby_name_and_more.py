# Generated by Django 4.2.1 on 2023-05-22 15:53

import django.core.validators
from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0016_alter_passwordresetcode_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="department",
            name="name",
            field=models.CharField(
                max_length=48,
                unique=True,
                validators=[
                    django.core.validators.MinLengthValidator(2),
                    users.validators.alpha_space_dash_validator,
                ],
                verbose_name="Наименование",
            ),
        ),
        migrations.AlterField(
            model_name="hobby",
            name="name",
            field=models.CharField(
                max_length=32,
                unique=True,
                validators=[
                    django.core.validators.MinLengthValidator(2),
                    users.validators.alpha_space_dash_validator,
                ],
                verbose_name="Наименование",
            ),
        ),
        migrations.AlterField(
            model_name="position",
            name="name",
            field=models.CharField(
                max_length=48,
                unique=True,
                validators=[
                    django.core.validators.MinLengthValidator(2),
                    users.validators.alpha_space_dash_validator,
                ],
                verbose_name="Название должности",
            ),
        ),
    ]