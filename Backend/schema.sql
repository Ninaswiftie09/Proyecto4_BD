-- TIPOS PERSONALIZADOS

CREATE TYPE metodo_pago_enum AS ENUM ('Efectivo', 'Tarjeta', 'Transferencia', 'Criptomoneda');

CREATE TYPE tipo_entrada_enum AS ENUM ('General', 'VIP', 'Preferencial', 'Backstage');

CREATE TYPE genero_musical_enum AS ENUM (
  'Rock', 'Pop', 'Jazz', 'Reggaeton', 'Electronica', 'Indie', 'Clásica', 'Metal'
);

CREATE TYPE rol_staff_enum AS ENUM ('Seguridad', 'Sonidista', 'Iluminación', 'Logística', 'Producción');

CREATE TYPE pais_codigo_enum AS ENUM ('GT', 'MX', 'US', 'AR', 'CO', 'ES');

CREATE TABLE artista (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    alias TEXT UNIQUE,
    genero genero_musical_enum,
    pais VARCHAR(50),
    biografia TEXT
);

CREATE TABLE banda (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    anio_formacion INT,
    genero_principal genero_musical_enum
);

CREATE TABLE miembrobanda (
    id SERIAL PRIMARY KEY,
    artista_id INT REFERENCES artista(id) ON DELETE CASCADE,
    banda_id INT REFERENCES banda(id) ON DELETE CASCADE
);

CREATE TABLE ubicacion (
    id SERIAL PRIMARY KEY,
    ciudad VARCHAR(100),
    pais pais_codigo_enum,
    direccion VARCHAR(200)
);

CREATE TABLE evento (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    fecha DATE,
    ubicacion_id INT REFERENCES ubicacion(id) ON DELETE CASCADE,
    descripcion TEXT
);

CREATE TABLE concierto (
    id INT PRIMARY KEY REFERENCES evento(id) ON DELETE CASCADE,
    hora_inicio TIME
);

CREATE TABLE festival (
    id INT PRIMARY KEY REFERENCES evento(id) ON DELETE CASCADE,
    duracion_dias INT
);

CREATE TABLE escenario (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    capacidad INT,
    ubicacion_id INT REFERENCES ubicacion(id) ON DELETE CASCADE
);

CREATE TABLE patrocinador (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    tipo VARCHAR(50)
);

CREATE TABLE patrocinio (
    id SERIAL PRIMARY KEY,
    patrocinador_id INT REFERENCES patrocinador(id) ON DELETE CASCADE,
    evento_id INT REFERENCES evento(id) ON DELETE CASCADE
);

CREATE TABLE entrada (
    id SERIAL PRIMARY KEY,
    evento_id INT REFERENCES evento(id) ON DELETE CASCADE,
    tipo tipo_entrada_enum DEFAULT 'General',
    precio NUMERIC DEFAULT 50,
    cantidad_disponible INTEGER
);



CREATE TABLE Cliente (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL
);


-- Atributo multivariado para teléfonos
CREATE TABLE telefonocliente (
    id SERIAL PRIMARY KEY,
    cliente_id INT REFERENCES cliente(id) ON DELETE CASCADE,
    numero VARCHAR(20)
);

CREATE TABLE venta (
    id SERIAL PRIMARY KEY,
    entrada_id INT REFERENCES entrada(id) ON DELETE CASCADE,
    cliente_id INT REFERENCES cliente(id) ON DELETE CASCADE,
    fecha_venta DATE
);

CREATE TABLE pago (
    id SERIAL PRIMARY KEY,
    metodo_pago metodo_pago_enum,
    monto DECIMAL(8, 2),
    venta_id INT REFERENCES venta(id) ON DELETE CASCADE
);

CREATE TABLE equipamiento (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion TEXT
);

CREATE TABLE equipamientoevento (
    id SERIAL PRIMARY KEY,
    evento_id INT REFERENCES evento(id) ON DELETE CASCADE,
    equipamiento_id INT REFERENCES equipamiento(id) ON DELETE CASCADE
);

CREATE TABLE staff (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    rol rol_staff_enum,
    contacto VARCHAR(100)
);

CREATE TABLE staffevento (
    id SERIAL PRIMARY KEY,
    evento_id INT REFERENCES evento(id) ON DELETE CASCADE,
    staff_id INT REFERENCES staff(id) ON DELETE CASCADE
);

CREATE TABLE resena (
    id SERIAL PRIMARY KEY,
    calificacion INTEGER CHECK (calificacion BETWEEN 1 AND 5),
    comentario TEXT,
    venta_id INTEGER REFERENCES Venta(id)
);


CREATE TABLE participacionevento (
    id SERIAL PRIMARY KEY,
    artista_id INT REFERENCES artista(id) ON DELETE CASCADE,
    evento_id INT REFERENCES evento(id) ON DELETE CASCADE
);


