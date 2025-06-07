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

        2. Abre el archivo index.html 

        3. ¡Listo! Ya puedes ver los conciertos disponibles, leer reseñas y adquirir entradas 




### Descripción de los trigger y funciones 

    Validaciones y Reglas del Proyecto
    Este sistema incluye validaciones tanto a nivel de aplicación (usando Django ORM) como a nivel de base de datos (usando SQL puro con PostgreSQL). A continuación, se detallan:

    ✅ Validaciones en la Aplicación (Django ORM)
        1. Restricciones NOT NULL y UNIQUE: definidas en modelos como Cliente, Artista, Entrada, etc.

        2. Valores por defecto (DEFAULT): por ejemplo, el campo precio en Entrada tiene un valor por defecto de 50.

        3. Restricciones por validadores: la calificación de una Reseña está limitada a valores entre 1 y 5.

        4. Relaciones entre tablas: gestionadas con claves foráneas (ForeignKey) y restricciones on_delete.

    ⚙️ Validaciones en la Base de Datos (SQL)
        - Se implementaron 5 funciones y 5 triggers en SQL para reforzar la integridad de los datos.

    📄 Archivo SQL: 02-triggers.sql, ejecutado automáticamente al iniciar el contenedor PostgreSQL.

    🧠 Funciones SQL definidas por el usuario
        1. verificar_stock_entrada()	Verifica que haya entradas disponibles antes de una venta.
        2. reducir_stock_entrada()	Resta una entrada disponible tras una venta exitosa.
        3. validar_pago_monto()	Asegura que el pago coincide con el precio de la entrada.
        4. cliente_tiene_venta_para_evento()	Verifica que el cliente haya comprado entrada antes de dejar una reseña.
        5. staff_ya_asignado()	Impide que el mismo staff sea asignado más de una vez al mismo evento.

    Triggers SQL implementados

        1. trg_verificar_stock	BEFORE INSERT	venta	    Llama a verificar_stock_entrada()
        2. trg_reducir_stock	AFTER INSERT	venta	    Llama a reducir_stock_entrada()
        3. trg_validar_pago	    BEFORE INSERT	pago	    Llama a validar_pago_monto()
        4. trg_validar_resena	BEFORE INSERT	resena	    Llama a cliente_tiene_venta_para_evento()
        5. trg_validar_staff	BEFORE INSERT	staffevento	Llama a staff_ya_asignado()




