from clinica.views import PacienteNovoView, ClinicaNovaView, ClinicaDeleteView, ClinicaListView, ClinicaDetailView, \
    MesView, RelatorioView
from django.urls import path

from core.views import IndexView

urlpatterns = [
    path('', ClinicaListView.as_view(), name='clinica_lista'),
    path('<int:pk>', ClinicaDetailView.as_view(), name='clinica_detail'),
    path('nova', ClinicaNovaView.as_view(), name='clinica_nova'),
    path('<int:clinica_id>/paciente/novo', PacienteNovoView.as_view(), name='paciente_novo'),
    path('<int:pk>/apagar', ClinicaDeleteView.as_view(), name='clinica_delete'),
    path('mes', MesView.as_view(), name='meses'),
    path('<int:id>/relatorio', RelatorioView.as_view(), name='relatorio_clinica'),
]
