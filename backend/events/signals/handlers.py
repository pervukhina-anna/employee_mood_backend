from django.contrib.auth import get_user_model
from django.db.models import Q
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from notifications.models import Notification

from ..models import Event

User = get_user_model()


@receiver(m2m_changed, sender=Event.departments.through)
def create_notification_for_event_by_departments(
    action, pk_set, **kwargs
):
    """Вызывается при cвязывании объекта модели `Event` с `Department`.

    В результате в БД создаются объекты модели `Notification`
    для всех пользователей из поля `employees` модели `Event`
    и пользователей связанных с департаментами - полем
    `departments`.
    """
    if action == 'post_add':
        Notification.objects.bulk_create([
            Notification(
                incident_type=Notification.IncidentType.EVENT,
                user=obj
            ) for obj in User.objects.filter(
                Q(department__in=pk_set) & Q(is_active=True)
            )
        ])


@receiver(m2m_changed, sender=Event.departments.through)
def create_notification_for_event_by_employees(
    action, pk_set, **kwargs
):
    """Вызывается при cвязывании объекта модели `Event` с `User`.

    В результате в БД создаются объекты модели `Notification`
    для всех пользователей из поля `employees` модели `Event`
    и пользователей связанных с департаментами - полем
    `departments`.
    """
    if action == 'post_add':
        Notification.objects.bulk_create([
            Notification(
                incident_type=Notification.IncidentType.EVENT,
                user=obj
            ) for obj in User.objects.filter(
                Q(id__in=pk_set) & Q(is_active=True)
            )
        ])
