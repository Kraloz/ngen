from django.views.generic import TemplateView
from django.urls import path

urlpatterns = [
  path('catalogo/',   TemplateView.as_view(template_name='catalogo.html')),
  path('produccion/', TemplateView.as_view(template_name='produccion.html')),
  path('',            TemplateView.as_view(template_name='index.html')),
]