from django.urls import path
from paciente.views import PacienteDeleteView, PDF, PacienteUpdateView

urlpatterns = [
    path('<int:pk>/atualizar', PacienteUpdateView.as_view(), name='paciente_update'),
    path('<int:pk>/apagar', PacienteDeleteView.as_view(), name='paciente_delete'),
    path('relatorio_pdf/<int:id>', PDF.as_view(), name='relatorio_pdf'),
]
