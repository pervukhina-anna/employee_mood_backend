# Generated by Django 4.2.1 on 2023-06-21 08:34

import datetime

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

import metrics.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CompletedSurvey",
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
                    "summary",
                    models.JSONField(default=None, null=True, verbose_name="Сводка"),
                ),
                ("results", models.JSONField(verbose_name="Результаты")),
                (
                    "completion_date",
                    models.DateField(
                        default=datetime.date.today,
                        verbose_name="дата прохождения опроса",
                    ),
                ),
                (
                    "next_attempt_date",
                    models.DateField(
                        default=datetime.date.today,
                        verbose_name="дата следующей попытки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Результат опроса сотрудника",
                "verbose_name_plural": "Результаты опросов сотрудников",
                "ordering": ("-id",),
            },
        ),
        migrations.CreateModel(
            name="Condition",
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
                    "mood",
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                        verbose_name="Настроение",
                    ),
                ),
                (
                    "note",
                    models.CharField(
                        blank=True,
                        max_length=128,
                        null=True,
                        validators=[django.core.validators.MinLengthValidator(4)],
                        verbose_name="Заметка",
                    ),
                ),
                (
                    "date",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Дата/время добавления показателей",
                    ),
                ),
            ],
            options={
                "verbose_name": "Состояние (сотрудника)",
                "verbose_name_plural": "Состояния",
                "ordering": ("-date",),
            },
        ),
        migrations.CreateModel(
            name="LifeDirection",
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
                ("name", models.CharField(max_length=128, verbose_name="Наименование")),
                (
                    "num",
                    models.PositiveSmallIntegerField(
                        unique=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(8),
                        ],
                        verbose_name="Номер",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=256, null=True, verbose_name="Описание"
                    ),
                ),
            ],
            options={
                "verbose_name": "Жизненное направление",
                "verbose_name_plural": "Жизненные направления",
                "ordering": ("num",),
            },
        ),
        migrations.CreateModel(
            name="Question",
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
                    "text",
                    models.TextField(max_length=800, verbose_name="Текст вопроса"),
                ),
                (
                    "key",
                    models.IntegerField(blank=True, null=True, verbose_name="Ключ"),
                ),
                (
                    "priority",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(99),
                        ],
                        verbose_name="Приоритет при выдаче",
                    ),
                ),
            ],
            options={
                "verbose_name": "Вопрос",
                "verbose_name_plural": "Вопросы",
                "ordering": ("priority", "id"),
            },
        ),
        migrations.CreateModel(
            name="Survey",
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
                    "for_all",
                    models.BooleanField(
                        default=True,
                        help_text="При положительном значении, поле с отделами игнорируется  и уведомления о появлении нового опроса отправляются всем активным сотрудникам",
                        verbose_name="Доступен всем",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=255, verbose_name="Название опроса"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        max_length=800,
                        null=True,
                        verbose_name="Описание опроса",
                    ),
                ),
                (
                    "text",
                    models.TextField(
                        blank=True,
                        null=True,
                        verbose_name="Текст после прохождения опроса",
                    ),
                ),
                (
                    "frequency",
                    models.PositiveSmallIntegerField(
                        default=30,
                        validators=[django.core.validators.MaxValueValidator(90)],
                        verbose_name="Периодичность прохождения опроса",
                    ),
                ),
                (
                    "min_range",
                    models.PositiveSmallIntegerField(
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                        verbose_name="Минимальный средний порог расчета",
                    ),
                ),
                (
                    "max_range",
                    models.PositiveSmallIntegerField(
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                        verbose_name="Максимальный средний порог расчета",
                    ),
                ),
                (
                    "creation_date",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Дата и время создания опроса",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Статус активности"),
                ),
            ],
            options={
                "verbose_name": "Опрос",
                "verbose_name_plural": "Опросы",
                "ordering": ("-id",),
            },
        ),
        migrations.CreateModel(
            name="SurveyType",
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
                ("name", models.CharField(max_length=255, verbose_name="Наименование")),
                ("slug", models.SlugField(verbose_name="Slug")),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=255, verbose_name="Описание"
                    ),
                ),
            ],
            options={
                "verbose_name": "Тип опросов",
                "verbose_name_plural": "Типы опросов",
            },
        ),
        migrations.CreateModel(
            name="UserLifeBalance",
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
                    "date",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Дата/время добавления показателей",
                    ),
                ),
                (
                    "set_priority",
                    models.BooleanField(
                        default=False, verbose_name="Задать новые приоритеты."
                    ),
                ),
                (
                    "results",
                    models.JSONField(
                        validators=[metrics.validators.validate_results],
                        verbose_name="Результаты",
                    ),
                ),
            ],
            options={
                "verbose_name": "Жизненный баланс сотрудника",
                "verbose_name_plural": "Жизненный баланс сотрудников",
                "ordering": ("-date",),
            },
        ),
        migrations.CreateModel(
            name="Variant",
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
                    "text",
                    models.CharField(max_length=255, verbose_name="Текст варианта"),
                ),
                (
                    "priority",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(99),
                        ],
                        verbose_name="Приоритет при выдаче",
                    ),
                ),
                (
                    "value",
                    models.IntegerField(blank=True, null=True, verbose_name="Значение"),
                ),
                (
                    "survey_type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="metrics.surveytype",
                        verbose_name="Тип опроса",
                    ),
                ),
            ],
            options={
                "verbose_name": "Вариант ответа",
                "verbose_name_plural": "Варианты ответа",
                "ordering": ("priority", "id"),
            },
        ),
    ]
