from django.contrib.auth import get_user_model
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver

from notifications.models import Notification
from notifications.signals.handlers import notification

from ..models import SurveyDepartment

User = get_user_model()


@receiver(post_save, sender=SurveyDepartment)
def create_notification_for_survey(sender, instance, created, **kwargs):
    """Вызывается при cвязывании объекта модели `Survey` с `Department`.

    В результате в БД создаются объекты модели `Notification`
    для всех пользователей из связанных департаментов модели `Survey`.
    """
    if created:
        department_id = instance.department.id
        Notification.objects.bulk_create([
            Notification(
                incident_type=Notification.IncidentType.SURVEY,
                incident_id=instance.survey.id,
                user=obj
            ) for obj in User.objects.filter(
                Q(department=department_id) & Q(is_active=True)
            )
        ])
        for obj in User.objects.filter(
            Q(department=department_id) & Q(is_active=True)
        ):
            notification.send(sender=Notification, user=obj)
