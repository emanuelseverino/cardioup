import datetime
import io
import calendar
from datetime import datetime
import pytz as pytz
from django.utils import timezone
from django.http import HttpResponse
from django.views import View
from django.views.generic import DeleteView, UpdateView

from clinica.models import Clinica
from paciente.models import Paciente
import xhtml2pdf.pisa as pisa
from django.template.loader import get_template


class PacienteUpdateView(UpdateView):
    model = Paciente
    fields = ['nome', ]
    template_name_suffix = "_update_form"

    def get_success_url(self):
        paciente = Paciente.objects.get(pk=self.kwargs['pk'])
        return '/clinica/%s/paciente/novo' % paciente.clinica.pk


class PacienteDeleteView(DeleteView):
    model = Paciente

    def get_success_url(self):
        paciente = Paciente.objects.get(pk=self.kwargs['pk'])
        return '/clinica/%s/paciente/novo' % paciente.clinica.pk
