-- ========================
-- FUNCIONES
-- ========================

-- 1. Verificar que haya entradas disponibles
CREATE OR REPLACE FUNCTION verificar_stock_entrada()
RETURNS TRIGGER AS $$
DECLARE
    disponibles INTEGER;
BEGIN
    SELECT cantidad_disponible INTO disponibles
    FROM entrada
    WHERE id = NEW.entrada_id;

    IF disponibles IS NULL THEN
        RAISE EXCEPTION 'Entrada no encontrada.';
    ELSIF disponibles <= 0 THEN
        RAISE EXCEPTION 'No hay entradas disponibles.';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


-- 2. Reducir cantidad disponible de entradas después de venta
CREATE OR REPLACE FUNCTION reducir_stock_entrada()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE entrada
    SET cantidad_disponible = cantidad_disponible - 1
    WHERE id = NEW.entrada_id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


-- 3. Validar que el monto pagado sea igual al precio de la entrada
CREATE OR REPLACE FUNCTION validar_pago_monto()
RETURNS TRIGGER AS $$
DECLARE
    precio NUMERIC;
BEGIN
    SELECT e.precio INTO precio
    FROM entrada e
    JOIN venta v ON v.id = NEW.venta_id
    WHERE v.entrada_id = e.id;

    IF NEW.monto != precio THEN
        RAISE EXCEPTION 'El monto pagado (%.2f) no coincide con el precio de la entrada (%.2f).', NEW.monto, precio;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;



-- ========================
-- TRIGGERS
-- ========================

-- 1. Verificar entradas disponibles antes de venta
CREATE TRIGGER trg_verificar_stock
BEFORE INSERT ON venta
FOR EACH ROW
EXECUTE FUNCTION verificar_stock_entrada();

-- 2. Reducir stock después de venta
CREATE TRIGGER trg_reducir_stock
AFTER INSERT ON venta
FOR EACH ROW
EXECUTE FUNCTION reducir_stock_entrada();

-- 3. Validar monto pagado en pago
CREATE TRIGGER trg_validar_pago
BEFORE INSERT ON pago
FOR EACH ROW
EXECUTE FUNCTION validar_pago_monto();

