from django.urls import include, path, re_path

from api.v1.metrics import views
from api.v1.utils import OptionalSlashRouter

v10 = OptionalSlashRouter()

v10.register('conditions', views.ConditionViewSet, basename='conditions')
v10.register('life_balance', views.LifeBalanceViewSet, basename='life_balance')
v10.register(
    'surveys/results',
    views.CompletedSurveyViewSet,
    basename='surveys_results'
)
v10.register('surveys', views.SurveyViewSet, basename='surveys')

urlpatterns = [
    path('', include(v10.urls)),
    re_path(
        r'^life_directions/?$',
        views.LifeDirectionListView.as_view(),
        name='life_directions'
    ),
]
