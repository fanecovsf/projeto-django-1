
from django.urls import path, include

urlpatterns = [
    path('cad-resid/', include('app_cad_resid.urls'), name='residente'),
]

