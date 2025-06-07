import psycopg2
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
import csv
from reportlab.pdfgen import canvas
from io import BytesIO
from django.db import connection

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
