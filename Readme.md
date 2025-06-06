## Proyecto 4 – Base de Datos: Sistema de Eventos Musicales

## Integrantes
Ciprian Jimenez, Mishell Rosa Elvira - 231169 

Mejicanos Hernandez, Abner Gabriel - 231134  

Nájera Marakovits, Ingrid Nina Alessandra - 231088 

Ramírez Velásquez, Diego Alejandro - 23601  

Rivera Rodriguez, Alejandro - 23674 

Yee Vidal, María José - 231193 

## ¿Qué es?
Creamos un sistema para poder ver y adquirir entradas para diferentes conciertos y festivales.

## Requisitos cumplidos
- 21 tablas creadas con ORM (con tablas de cruce, relaciones 1:N y N:M, atributos multivaluados, datos personalizados, normalización hasta 3FN) 
- Cruds para ver, crear y editar y eliminar regristros ⛔
- Validaciones mediante restricciones, triggers y funciones SQL ⛔
- 2 vistas con html, css y js ** (falta el javascript) ** 
- Exportación de datos a CSV y PDF ⛔
- 1000 inserts ⛔
- Desarrollo de 3 reportes distintos ( Cada uno debe tener al menos 5 filtros significativos) ⛔

## Como correrlo

Antes de realizar algún paso, debes clonar el repositorio.

```bash
    git clone https://github.com/Ninaswiftie09/Proyecto4_BD
```

### 1. Construir y levantar los servicios

Desde la carpeta del proyecto ejecuta el siguiente comando: 

```bash
    docker-compose up --build
```

### 2. Acceder a pgAdmin

    URL: http://localhost:5050

    Credenciales:

    Usuario: admin@admin.com

    Contraseña: admin

### 2. Registrar el servidor en pgAdmin

    1. Click derecho en Servers > Register > Server

    2. En la pestaña General:

        Name: Proyecto4_BD

    3. En la pestaña Connection:

        Host: db

        Port: 5432

        Username: user

        Password: pass

### 3. Verifica la base de datos

    Si las tablas no se han creado automáticamente, entra al contenedor de Django y ejecuta las migraciones:

 ```bash
    docker exec -it evento_musical_backend bash
    python manage.py makemigrations
    python manage.py migrate
```

### 4. Insertar datos de prueba

    Abre Query Tool en pgAdmin y copia el contenido del archivo data.sql (dentro de la carpeta Backend).
    ¡Esto insertará los datos necesarios para probar el sistema!

### 5. Ver la interfaz web
        1. Navega a la carpeta Views/

        2. Abre el archivo index.html con tu navegador favorito

        3. ¡Listo! Ya puedes ver los conciertos disponibles, leer reseñas y adquirir entradas 


