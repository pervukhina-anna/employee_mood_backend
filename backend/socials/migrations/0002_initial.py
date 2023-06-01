# Generated by Django 4.2.1 on 2023-05-30 15:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("socials", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="status",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="statuses",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор",
            ),
        ),
        migrations.AddField(
            model_name="needhelp",
            name="recipient",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="received_help_requests",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Получатель",
            ),
        ),
        migrations.AddField(
            model_name="needhelp",
            name="sender",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="sent_help_requests",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Отправитель",
            ),
        ),
        migrations.AddField(
            model_name="needhelp",
            name="type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="employees",
                to="socials.helptype",
                verbose_name="Тип помощи",
            ),
        ),
    ]
