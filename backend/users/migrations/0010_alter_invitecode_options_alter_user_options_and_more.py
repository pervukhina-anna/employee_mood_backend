# Generated by Django 4.2.1 on 2023-05-18 09:09

from django.db import migrations, models
import phonenumber_field.modelfields
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0009_alter_user_first_name_alter_user_last_name_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="invitecode",
            options={
                "ordering": ["-created"],
                "verbose_name": "Приглашение",
                "verbose_name_plural": "Приглашения",
            },
        ),
        migrations.AlterModelOptions(
            name="user",
            options={
                "ordering": ["-date_joined"],
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
        migrations.AlterField(
            model_name="department",
            name="description",
            field=models.TextField(
                blank=True, max_length=255, null=True, verbose_name="Описание"
            ),
        ),
        migrations.AlterField(
            model_name="department",
            name="name",
            field=models.CharField(max_length=128, verbose_name="Наименование"),
        ),
        migrations.AlterField(
            model_name="hobby",
            name="name",
            field=models.CharField(
                max_length=32, unique=True, verbose_name="Наименование"
            ),
        ),
        migrations.AlterField(
            model_name="position",
            name="description",
            field=models.TextField(
                blank=True, max_length=255, null=True, verbose_name="Описание"
            ),
        ),
        migrations.AlterField(
            model_name="position",
            name="name",
            field=models.CharField(max_length=128, verbose_name="Название должности"),
        ),
        migrations.AlterField(
            model_name="user",
            name="about",
            field=models.TextField(
                blank=True, max_length=255, null=True, verbose_name="О себе"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                max_length=32,
                validators=[users.validators.validate_first_name],
                verbose_name="first name",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(
                max_length=32,
                validators=[users.validators.validate_last_name],
                verbose_name="last name",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="patronymic",
            field=models.CharField(
                blank=True,
                max_length=32,
                null=True,
                validators=[users.validators.validate_patronymic],
                verbose_name="Отчество",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                max_length=12,
                null=True,
                region=None,
                verbose_name="Телефон",
            ),
        ),
    ]