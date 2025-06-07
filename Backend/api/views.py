# Backend/api/views.py

import psycopg2
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
import csv
from reportlab.pdfgen import canvas
from io import BytesIO
from django.db import connection

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



def index(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
              AND table_type = 'BASE TABLE';
        """)
        tablas = [row[0] for row in cursor.fetchall()]
    return render(request, 'index.html', {'tablas': tablas})

def obtener_tablas():
    conn = psycopg2.connect(
        dbname=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
        port=settings.DATABASES['default']['PORT']
    )
    cursor = conn.cursor()
    cursor.execute("""
        SELECT table_name FROM information_schema.tables
        WHERE table_schema = 'public' AND table_type='BASE TABLE'
        ORDER BY table_name;
    """)
    tablas = [fila[0] for fila in cursor.fetchall()]
    cursor.close()
    conn.close()
    return tablas


def index(request):
    tablas = obtener_tablas()
    return render(request, 'index.html', {'tablas': tablas})


def exportar_csv(request):
    if request.method == "POST":
        tabla = request.POST.get('tabla')
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {tabla}")
        filas = cursor.fetchall()
        columnas = [desc[0] for desc in cursor.description]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{tabla}.csv"'

        writer = csv.writer(response)
        writer.writerow(columnas)
        writer.writerows(filas)

        cursor.close()
        conn.close()
        return response


def exportar_pdf(request):
    if request.method == "POST":
        tabla = request.POST.get('tabla')
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {tabla}")
        filas = cursor.fetchall()
        columnas = [desc[0] for desc in cursor.description]

        buffer = BytesIO()
        p = canvas.Canvas(buffer)
        p.setFont("Helvetica", 10)

        y = 800
        p.drawString(100, y, f"Tabla: {tabla}")
        y -= 20
        p.drawString(100, y, ", ".join(columnas))
        y -= 20

        for fila in filas:
            p.drawString(100, y, ", ".join(str(item) for item in fila))
            y -= 15
            if y < 50:
                p.showPage()
                y = 800

        p.save()
        buffer.seek(0)

        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{tabla}.pdf"'
        return response
