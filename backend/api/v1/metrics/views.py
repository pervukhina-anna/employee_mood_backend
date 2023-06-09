from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.v1.metrics.filters import CompletedSurveyFilter, ConditionFilter
from api.v1.metrics.serializers import (CompletedSurveyCreateSerializer,
                                        CompletedSurveySerializer,
                                        ConditionReadSerializer,
                                        ConditionWriteSerializer,
                                        LifeBalanceCreateSerializer,
                                        LifeBalanceSerializer,
                                        LifeDirectionSerializer,
                                        ShortSurveySerializer,
                                        SurveySerializer)
from api.v1.permissions import HRAllPermission
from metrics.models import (CompletedSurvey, Condition, LifeDirection, Survey,
                            UserLifeBalance)

from .filters import SurveyFilter

User = get_user_model()


@method_decorator(name='create', decorator=swagger_auto_schema(
    responses={status.HTTP_201_CREATED: ConditionReadSerializer},
))
class ConditionViewSet(ModelViewSet):
    queryset = Condition.objects.select_related('employee').all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ConditionFilter
    http_method_names = ('get', 'post',)
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ConditionReadSerializer
        return ConditionWriteSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = (HRAllPermission,)
            my_conditions = self.request.query_params.get('my_conditions')
            if my_conditions:
                self.permission_classes = (IsAuthenticated,)
        return super().get_permissions()


class LifeDirectionListView(ListAPIView):
    queryset = LifeDirection.objects.all()
    serializer_class = LifeDirectionSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None


@method_decorator(name='create', decorator=swagger_auto_schema(
    responses={status.HTTP_201_CREATED: LifeBalanceCreateSerializer},
))
class LifeBalanceViewSet(ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    http_method_names = ('get', 'post',)
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('employee', 'set_priority',)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return LifeBalanceSerializer
        return LifeBalanceCreateSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.is_hr:
            return UserLifeBalance.objects.all()
        return UserLifeBalance.objects.filter(employee=self.request.user.id)


@swagger_auto_schema(responses={status.HTTP_200_OK: SurveySerializer})
class SurveyViewSet(ModelViewSet):
    queryset = (
        Survey.objects
        .select_related('author', 'type')
        .prefetch_related('department', 'questions')
        .all()
    )
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SurveyFilter
    http_method_names = ('get',)
    permission_classes = (IsAuthenticated,)
    serializer_class = ShortSurveySerializer
    detail_serializer_class = SurveySerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            if hasattr(self, 'detail_serializer_class'):
                return self.detail_serializer_class

        return super(SurveyViewSet, self).get_serializer_class()


@method_decorator(name='create', decorator=swagger_auto_schema(
    responses={status.HTTP_201_CREATED: CompletedSurveySerializer}
))
class CompletedSurveyViewSet(ModelViewSet):
    queryset = CompletedSurvey.objects.select_related(
        'employee', 'survey', 'mental_state'
    ).all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CompletedSurveyFilter
    http_method_names = ('get', 'post',)
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = (HRAllPermission,)
            my_results = self.request.query_params.get('my_results')
            if my_results:
                self.permission_classes = (IsAuthenticated,)
        return super().get_permissions()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CompletedSurveySerializer
        return CompletedSurveyCreateSerializer

# оставлю пока не дойду то эндпоинтов конструктора
#     def perform_create(self, serializer):
#         questions_list = serializer.validated_data.pop('questions')
#         instance = serializer.save(author=self.request.user)
#         Question.objects.bulk_create(
#             Question(
#                 survey=instance, text=obj['text']
#             ) for obj in questions_list
#         )

#     def perform_update(self, serializer):
#         questions_list = serializer.validated_data.pop('questions', None)
#         instance = serializer.save()
#         if questions_list:
#             Question.objects.bulk_create(
#                 Question(
#                     survey=instance, text=obj['text']
#                 ) for obj in questions_list
#             )
