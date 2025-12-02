CREATE TYPE layer_enum AS ENUM ('python', 'db');
CREATE TYPE status_enum AS ENUM ('new', 'sent');

CREATE TABLE IF NOT EXISTS alerts (
    id SERIAL PRIMARY KEY,
    layer layer_enum,
    service VARCHAR(50),
    function VARCHAR(50),
    error TEXT,
    comment TEXT,
    datetime TIMESTAMP,
    status status_enum DEFAULT 'new'
);

CREATE OR REPLACE PROCEDURE add_alert(
    p_layer layer_enum,
    p_service VARCHAR,
    p_function VARCHAR,
    p_error TEXT,
    p_comment TEXT,
    p_datetime TIMESTAMP
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO alerts (layer, service, function, error, comment, datetime, status)
    VALUES (p_layer, p_service, p_function, p_error, p_comment, p_datetime, 'new');
END;
$$;
