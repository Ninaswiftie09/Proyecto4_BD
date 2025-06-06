from django.db import models

GENERO_MUSICAL = [
    ('Rock', 'Rock'),
    ('Pop', 'Pop'),
    ('Jazz', 'Jazz'),
    ('Reggaeton', 'Reggaeton'),
    ('Electronica', 'Electronica'),
    ('Indie', 'Indie'),
    ('Metal', 'Metal'),
]

# 1. tabla para artistas
class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=30, choices=GENERO_MUSICAL)
    pais = models.CharField(max_length=50)
    biografia = models.TextField()

# 2. tabla para bandas
class Banda(models.Model):
    nombre = models.CharField(max_length=100)
    anio_formacion = models.IntegerField()
    genero_principal = models.CharField(max_length=30, choices=GENERO_MUSICAL)
    miembros = models.ManyToManyField(Artista, through='MiembroBanda')

# 3. tablas para los miembros de las bandas
class MiembroBanda(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)

# 4. tabla para la ubicación 
PAISES = [
    ('GT', 'Guatemala'),
    ('MX', 'México'),
    ('US', 'Estados Unidos'),
    ('AR', 'Argentina'),
    ('CO', 'Colombia'),
    ('ES', 'España'),
]

class Ubicacion(models.Model):
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=3, choices=PAISES)
    direccion = models.CharField(max_length=200)


# 5. tabla para los eventos
class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    descripcion = models.TextField()

    class Meta:
        abstract = True

# 6. tabla para conciertos 
class Concierto(Evento):
    hora_inicio = models.TimeField()

# 7. tabla para el festival
class Festival(Evento):
    duracion_dias = models.PositiveIntegerField()

# 8. tabla para escenario
class Escenario(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)

# 9. tabla para los patrocinadores
class Patrocinador(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)

# 10. taabla para que estan patrocinando los patrocinadores xd
class Patrocinio(models.Model):
    patrocinador = models.ForeignKey(Patrocinador, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

# 11. tabla para las entrada
class Entrada(models.Model):
    TIPOS_ENTRADA = [
        ('General', 'General'),
        ('VIP', 'VIP'),
        ('Preferencial', 'Preferencial'),
        ('Backstage', 'Backstage'),
    ]
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    tipo_entrada = models.CharField(max_length=20, choices=TIPOS_ENTRADA)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    cantidad_disponible = models.IntegerField()


# 12. tabla para clientes
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

# 13. tabla para ventas
class Venta(models.Model):
    entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_venta = models.DateField()

# 14. tabla para los pagos
class Pago(models.Model):
    METODOS = [
        ('Efectivo', 'Efectivo'),
        ('Tarjeta', 'Tarjeta'),
        ('Transferencia', 'Transferencia'),
    ]
    metodo_pago = models.CharField(max_length=20, choices=METODOS)
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    venta = models.ForeignKey('Venta', on_delete=models.CASCADE)


# 15. tabla para el equipamiento
class Equipamiento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

# 16. tabla para que equipamiento tendra cada evento
class EquipamientoEvento(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    equipamiento = models.ForeignKey(Equipamiento, on_delete=models.CASCADE)

# 17. tabla para el staff
class Staff(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)
    contacto = models.CharField(max_length=100)

# 18. tabla para que staff estará en cada evento
class StaffEvento(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

# 19. tabla de reseñas de los clientes
class Reseña(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    calificacion = models.IntegerField()
    comentario = models.TextField()

# 20. artista-evento
class ParticipacionEvento(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
