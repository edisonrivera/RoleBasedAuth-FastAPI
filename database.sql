CREATE SEQUENCE rol_id_seq;
CREATE TABLE IF NOT EXISTS rol
(
    id integer NOT NULL DEFAULT nextval('rol_id_seq'::regclass),
    name character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT rol_pk PRIMARY KEY (id),
    CONSTRAINT rol_unique UNIQUE (name)
);

CREATE SEQUENCE rol_usuario_id_seq;
CREATE SEQUENCE rol_usuario_fk_rol_id_seq;
CREATE SEQUENCE rol_usuario_fk_usuario_id_seq;
CREATE TABLE IF NOT EXISTS rol_usuario
(
    id bigint NOT NULL DEFAULT nextval('rol_usuario_id_seq'::regclass),
    rol_id integer DEFAULT nextval('rol_usuario_fk_rol_id_seq'::regclass),
    usuario_id bigint NOT NULL DEFAULT nextval('rol_usuario_fk_usuario_id_seq'::regclass),
    CONSTRAINT rol_usuario_pk PRIMARY KEY (id)
);

CREATE SEQUENCE usuario_id_seq;
CREATE TABLE IF NOT EXISTS usuario
(
    id bigint NOT NULL DEFAULT nextval('usuario_id_seq'::regclass),
    nickname character varying(25) COLLATE pg_catalog."default" NOT NULL,
    password text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT usuario_pk PRIMARY KEY (id),
    CONSTRAINT usuario_unique UNIQUE (nickname)
);


ALTER TABLE IF EXISTS rol_usuario
    ADD CONSTRAINT fk_rol_id FOREIGN KEY (rol_id)
    REFERENCES rol (id) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE SET NULL;

ALTER TABLE IF EXISTS rol_usuario
    ADD CONSTRAINT fk_usuario_id FOREIGN KEY (usuario_id)
    REFERENCES usuario (id) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE CASCADE;

INSERT INTO rol ("name") VALUES
    ('SUPPORT'),
    ('USER'),
    ('ADMIN');

INSERT INTO usuario (nickname,"password") VALUES
    ('User','$2b$12$zZi5aNvNjdZn/wwvPgqXwOMwrYGTsQ9IrybmCUd6L5UpIsS0yNDdW'),
    ('Admin','$2b$12$zZi5aNvNjdZn/wwvPgqXwOMwrYGTsQ9IrybmCUd6L5UpIsS0yNDdW'),
    ('Support','$2b$12$zZi5aNvNjdZn/wwvPgqXwOMwrYGTsQ9IrybmCUd6L5UpIsS0yNDdW'),
    ('SupportUser','$2b$12$zZi5aNvNjdZn/wwvPgqXwOMwrYGTsQ9IrybmCUd6L5UpIsS0yNDdW');

INSERT INTO rol_usuario (rol_id, usuario_id) VALUES
    (2,1),
    (1,2),
    (3,2),
    (2,2),
    (1,3),
    (1,4),
    (2,4);