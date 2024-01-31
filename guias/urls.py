from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path("", GuiaListView.as_view(), name="guia_list"),
    path("guias", GuiaListView.as_view(), name="guia_list"),
    path("guias/<int:guia_id>", GuiaSingleView.as_view(), name="guia_single"),
    path("results/<int:pk>", GuiaResultsView.as_view(), name="guia_results"),
    path("resources/<int:pk>", GuiaResourcesView.as_view(), name="guia_results"),
    path("chronogram/<int:pk>", GuiaChronogramView.as_view(), name="chronogram_single"),
    path("competencias", GuiaCompetenciasView.as_view(), name="competencias"),
    path("competencias/<int:id>", GuiaCompetenciasSingleView.as_view(), name="competencias_single"),
    path("competencias/<str:key>", GuiaCompetenciasSingleViewByKey.as_view(), name="competencias_single_by_key"),
    re_path(r'^competencias/list/(?P<ids>[0-9,]+)/?$', GuiaCompetenciasListView.as_view(), name="competencias_list"),
]
urlpatterns = format_suffix_patterns(urlpatterns)