from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path("", GuiaViewList.as_view(), name="guia_list"),
    path("chronogram/<int:pk>", GuiaChronogramView.as_view(), name="chronogram_single"),
    path("contents/", GuiaContentsViewList.as_view(), name="contents"),
    path("contents/<int:pk>/", GuiaContentsViewSingle.as_view(), name="contents_single"),
    path("competencies/", GuiaCompetenciasView.as_view(), name="competencias"),
    path("competencies/<int:id>/", GuiaCompetenciasSingleView.as_view(), name="competencias_single"),
    path("competencies/<str:key>/", GuiaCompetenciasSingleViewByKey.as_view(), name="competencias_single_by_key"),
    re_path(r'^competencies/list/(?P<ids>[0-9,]+)/?$', GuiaCompetenciasListView.as_view(), name="competencias_list"),
    path("guias", GuiaViewList.as_view(), name="guia_list"),
    path("guias/<int:guia_id>", GuiaViewSingle.as_view(), name="guia_single"),
    path("resources/", GuiaResourcesViewList.as_view(), name="resources_list"),
    path("resources/<int:pk>/", GuiaResourcesViewSingle.as_view(), name="resources_single"),
    path("results/", GuiaResultsViewList.as_view(), name="results"),
    path("results/<int:pk>/", GuiaResultsViewSingle.as_view(), name="results_single"),
    path("specialties/", GuiaSpecialtiesViewList.as_view(), name="specialties_list"),
    path("specialties/<int:pk>/", GuiaSpecialtiesViewSingle.as_view(), name="specialties_single"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
