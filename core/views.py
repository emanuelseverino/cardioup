from clinica.models import Clinica
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import TemplateView


class IndexView(LoginRequiredMixin, TemplateView):
    login_url = '/contas/login/'
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        context["clinicas"] = Clinica.objects.all()
        return context