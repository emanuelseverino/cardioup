from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('clinica/', include('clinica.urls'), ),
    path('paciente/', include('paciente.urls'), ),
    path('', include('core.urls'), ),
    path('contas/', include('django.contrib.auth.urls'), ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)