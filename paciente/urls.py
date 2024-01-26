from django.urls import path
from paciente.views import PacienteDeleteView, PacienteUpdateView

urlpatterns = [
    path('<int:pk>/atualizar', PacienteUpdateView.as_view(), name='paciente_update'),
    path('<int:pk>/apagar', PacienteDeleteView.as_view(), name='paciente_delete'),
]
