from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import GuiaListView, GuiaSingleView

urlpatterns = [
    path("", GuiaListView.as_view(), name="guia_list"), 
    path("guias", GuiaListView.as_view(), name="guia_list"), 
    path("guias/<int:guia_id>", GuiaSingleView.as_view(), name="guia_single")
]
urlpatterns = format_suffix_patterns(urlpatterns)