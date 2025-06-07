# Backend/api/urls.py

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views


from .views import (
    # Artista
    ArtistaListView, ArtistaCreateView, ArtistaUpdateView, ArtistaDeleteView,
    # Cliente
    ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView,
    # Entrada
    EntradaListView, EntradaCreateView, EntradaUpdateView, EntradaDeleteView,
)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Páginas estáticas
    path('',      TemplateView.as_view(template_name='index.html'), name='home'),
    path('info/', TemplateView.as_view(template_name='info.html'),  name='info'),

    # CRUD Artista
    path('artistas/',               ArtistaListView.as_view(),   name='artista-list'),
    path('artistas/create/',        ArtistaCreateView.as_view(), name='artista-create'),
    path('artistas/<int:pk>/edit/', ArtistaUpdateView.as_view(), name='artista-update'),
    path('artistas/<int:pk>/delete/',ArtistaDeleteView.as_view(), name='artista-delete'),

    # CRUD Cliente
    path('clientes/',               ClienteListView.as_view(),   name='cliente-list'),
    path('clientes/create/',        ClienteCreateView.as_view(), name='cliente-create'),
    path('clientes/<int:pk>/edit/', ClienteUpdateView.as_view(), name='cliente-update'),
    path('clientes/<int:pk>/delete/',ClienteDeleteView.as_view(), name='cliente-delete'),

    # CRUD Entrada
    path('entradas/',               EntradaListView.as_view(),   name='entrada-list'),
    path('entradas/create/',        EntradaCreateView.as_view(), name='entrada-create'),
    path('entradas/<int:pk>/edit/', EntradaUpdateView.as_view(), name='entrada-update'),
    path('entradas/<int:pk>/delete/',EntradaDeleteView.as_view(), name='entrada-delete'),

    path('exportar_csv/', views.exportar_csv, name='exportar_csv'),
    path('exportar_pdf/', views.exportar_pdf, name='exportar_pdf'),
]
