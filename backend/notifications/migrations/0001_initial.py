# Generated by Django 4.2.1 on 2023-06-13 09:10

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incident_type', models.TextField(blank=True, choices=[('Опрос', 'Survey'), ('Событие', 'Event'), ('Сообщение', 'Message')], verbose_name='тип уведомления')),
                ('is_viewed', models.BooleanField(default=False, verbose_name='просмотрено/не просмотрено')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата и время создания уведомления')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL, verbose_name='сотрудник')),
            ],
            options={
                'verbose_name': 'уведомление',
                'verbose_name_plural': 'уведомления',
                'ordering': ('-creation_date',),
            },
        ),
    ]
