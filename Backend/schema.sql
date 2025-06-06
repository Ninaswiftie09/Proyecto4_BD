-- TIPOS PERSONALIZADOS

CREATE TYPE metodo_pago_enum AS ENUM ('Efectivo', 'Tarjeta', 'Transferencia', 'Criptomoneda');

CREATE TYPE tipo_entrada_enum AS ENUM ('General', 'VIP', 'Preferencial', 'Backstage');

CREATE TYPE genero_musical_enum AS ENUM (
  'Rock', 'Pop', 'Jazz', 'Reggaeton', 'Electronica', 'Indie', 'Clásica', 'Metal');

CREATE TYPE rol_staff_enum AS ENUM ('Seguridad', 'Sonidista', 'Iluminación', 'Logística', 'Producción');

CREATE TYPE pais_codigo_enum AS ENUM ('GT', 'MX', 'US', 'AR', 'CO', 'ES'); 
