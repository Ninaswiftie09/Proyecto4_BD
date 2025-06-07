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


-- ========================
-- TRIGGERS
-- ========================

-- 1. Verificar entradas disponibles antes de venta
CREATE TRIGGER trg_verificar_stock
BEFORE INSERT ON venta
FOR EACH ROW
EXECUTE FUNCTION verificar_stock_entrada();


