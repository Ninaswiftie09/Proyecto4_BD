# Backend/api/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import (
    Artista, ArtistaView,
    Cliente, ClienteView,
    Entrada, EntradaView,
)


class ArtistaListView(ListView):
    model = ArtistaView
    template_name = 'api/artista_list.html'
    context_object_name = 'artistas'


class ArtistaCreateView(CreateView):
    model = Artista
    fields = ['nombre', 'alias', 'genero', 'pais', 'biografia']
    template_name = 'api/artista_form.html'
    success_url = reverse_lazy('artista-list')


class ArtistaUpdateView(UpdateView):
    model = Artista
    fields = ['nombre', 'alias', 'genero', 'pais', 'biografia']
    template_name = 'api/artista_form.html'
    success_url = reverse_lazy('artista-list')


class ArtistaDeleteView(DeleteView):
    model = Artista
    template_name = 'api/artista_confirm_delete.html'
    success_url = reverse_lazy('artista-list')


class ClienteListView(ListView):
    model = ClienteView
    template_name = 'api/cliente_list.html'
    context_object_name = 'clientes'


class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nombre', 'email']
    template_name = 'api/cliente_form.html'
    success_url = reverse_lazy('cliente-list')


class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nombre', 'email']
    template_name = 'api/cliente_form.html'
    success_url = reverse_lazy('cliente-list')


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'api/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente-list')


class EntradaListView(ListView):
    model = EntradaView
    template_name = 'api/entrada_list.html'
    context_object_name = 'entradas'


class EntradaCreateView(CreateView):
    model = Entrada
    fields = ['evento', 'tipo_entrada', 'precio', 'cantidad_disponible']
    template_name = 'api/entrada_form.html'
    success_url = reverse_lazy('entrada-list')


class EntradaUpdateView(UpdateView):
    model = Entrada
    fields = ['evento', 'tipo_entrada', 'precio', 'cantidad_disponible']
    template_name = 'api/entrada_form.html'
    success_url = reverse_lazy('entrada-list')


class EntradaDeleteView(DeleteView):
    model = Entrada
    template_name = 'api/entrada_confirm_delete.html'
    success_url = reverse_lazy('entrada-list')
