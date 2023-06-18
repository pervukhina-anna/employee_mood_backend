# Generated by Django 4.2.1 on 2023-06-18 13:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "incident_type",
                    models.TextField(
                        blank=True,
                        choices=[
                            ("Опрос", "Survey"),
                            ("Событие", "Event"),
                            ("Сообщение", "Message"),
                        ],
                        verbose_name="тип уведомления",
                    ),
                ),
                (
                    "incident_id",
                    models.PositiveIntegerField(
                        verbose_name="индивидуальный идентификатор события"
                    ),
                ),
                (
                    "is_viewed",
                    models.BooleanField(
                        default=False, verbose_name="просмотрено/не просмотрено"
                    ),
                ),
                (
                    "creation_date",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="дата и время создания уведомления",
                    ),
                ),
            ],
            options={
                "verbose_name": "уведомление",
                "verbose_name_plural": "уведомления",
                "ordering": ("-creation_date",),
            },
        ),
    ]
