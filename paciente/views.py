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


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode('UTF-8')), response
        )
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf'
            )
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse('Error Renderig PDF', status=400)


class PDF(View):

    def get(self, request, id):
        clinica = Clinica.objects.get(id=id)
        hoje = timezone.now().date()
        ano = timezone.now().year
        mes = timezone.now().month
        mes_nome = calendar.month_name[timezone.now().month]
        primeiro_dia = datetime(ano, mes, 1, tzinfo=pytz.timezone('America/Sao_Paulo'))
        ultimo_dia = datetime(ano, mes, calendar.monthrange(ano, mes)[1], tzinfo=pytz.timezone('America/Sao_Paulo'))
        pacientes = Paciente.objects.filter(clinica=clinica, criado_em__range=(primeiro_dia, ultimo_dia)).order_by(
            'criado_em')
        nome_arquivo = '%s%s' % (clinica.nome.replace(' ', ''), mes_nome)
        params = {
            'imagem': 'staticfiles/img/logo-h.png',
            'clinica': clinica,
            'hoje': hoje,
            'mes': mes,
            'pacientes': pacientes,
            'request': request,
        }
        return Render.render('paciente/relatorio.html', params, nome_arquivo)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        pass
