from api.v1.metrics.filters import CompletedSurveyFilter, SurveyFilter
from api.v1.metrics.serializers import (CompletedSurveyCreateSerializer,
                                        CompletedSurveySerializer,
                                        ConditionReadSerializer,
                                        ConditionWriteSerializer,
                                        SurveyCreateSerializer,
                                        SurveySerializer)
from api.v1.permissions import HRAllPermission, SurveyAuthorOrAdminOnly
from django.contrib.auth import get_user_model
# from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from metrics.models import CompletedSurvey, Condition, Question, Survey
# from rest_framework import request
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

User = get_user_model()


class ConditionViewSet(ModelViewSet):
    queryset = Condition.objects.all()
    filter_backends = (DjangoFilterBackend,)
    http_method_names = ('get', 'post',)
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ConditionReadSerializer
        return ConditionWriteSerializer


class SurveyViewSet(ModelViewSet):
    queryset = Survey.objects.select_related(
        'author', 'department',
    ).prefetch_related('questions').all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SurveyFilter
    http_method_names = ('get', 'post', 'patch',)
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.request.method == 'PATCH':
            self.permission_classes = (SurveyAuthorOrAdminOnly,)
        return super().get_permissions()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SurveySerializer
        return SurveyCreateSerializer

    def perform_create(self, serializer):
        questions_list = serializer.validated_data.pop('questions')
        instance = serializer.save(author=self.request.user)
        Question.objects.bulk_create(
            Question(
                survey=instance, text=obj['text']
            ) for obj in questions_list
        )

    def perform_update(self, serializer):
        questions_list = serializer.validated_data.pop('questions', None)
        instance = serializer.save()
        if questions_list:
            Question.objects.bulk_create(
                Question(
                    survey=instance, text=obj['text']
                ) for obj in questions_list
            )


class CompletedSurveyViewSet(ModelViewSet):
    queryset = CompletedSurvey.objects.select_related(
        'employee', 'survey',
    ).all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CompletedSurveyFilter
    http_method_names = ('get', 'post',)
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = (HRAllPermission,)
        return super().get_permissions()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CompletedSurveySerializer
        return CompletedSurveyCreateSerializer

    def perform_create(self, serializer):
        serializer.save(employee=self.request.user)
