# Generated by Django 4.2.1 on 2023-06-17 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0003_event_to_all"),
    ]

    operations = [
        migrations.RenameField(
            model_name="event",
            old_name="to_all",
            new_name="for_all",
        ),
    ]