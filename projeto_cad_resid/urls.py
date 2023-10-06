
from django.urls import path, include

urlpatterns = [
    path('cad_resid/', include('app_cad_resid.urls'), name='residente'),
]

