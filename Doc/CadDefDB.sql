-- Convenio --
CREATE TABLE TCADCONV0 (
    id_conv INTEGER   PRIMARY KEY AUTOINCREMENT,
    nm_conv TEXT (50) 
);

CREATE INDEX ICADCONV0 ON TCADCONV0 (
    nm_conv
);


-- Local --
CREATE TABLE TCADLOC0 (
    id_local INTEGER   PRIMARY KEY ASC AUTOINCREMENT
                       NOT NULL,
    nm_local TEXT (50) 
);

CREATE INDEX ICADLOC0 ON TCADLOC0 (
    nm_local
);


-- Medico --
CREATE TABLE TCADMED0 (
    id_med INTEGER   PRIMARY KEY ASC AUTOINCREMENT
                     NOT NULL,
    nm_med TEXT (50) NOT NULL,
    nu_crm TEXT
);
DROP INDEX ICADMED;
CREATE INDEX ICADMED0 ON TCADMED0 (
    id_med
);


-- Endereço --
CREATE TABLE TCADMEDEND0 (
    id_med    INTEGER   REFERENCES TCADMED0 (id_med) ON DELETE CASCADE
                                                     ON UPDATE NO ACTION,
    id_local  INTEGER   REFERENCES TCADLOC0 (id_local) ON DELETE NO ACTION
                                                       ON UPDATE NO ACTION,
    id_end    INTEGER   UNIQUE
                        PRIMARY KEY AUTOINCREMENT,
    nm_end    TEXT,
    nu_end    TEXT,
    de_compl  TEXT,
    nm_cidade TEXT,
    nm_bairro TEXT,
    nm_estado TEXT,
    nu_cep    TEXT,
    nu_tel1   TEXT (20),
    nu_tel2   TEXT (20),
    nu_tel3   TEXT (20),
    de_obs
);

CREATE INDEX ICADMEDEND0 ON TCADMEDEND0 (
    id_med,
    id_local,
    id_end
);

CREATE INDEX ICADMEDEND1 ON TCADMEDEND0 (
    nm_end,
    nu_end,
    de_compl
);


-- Agenda --
CREATE TABLE TCADMEDAGEN0 (
    id_med  INTEGER     REFERENCES TCADMED0 (id_med) ON DELETE CASCADE
                                                     ON UPDATE NO ACTION,
    id_end  INTEGER     REFERENCES TCADMEDEND0 (id_end) ON DELETE CASCADE
                                                        ON UPDATE NO ACTION,
    id_agen INTEGER     PRIMARY KEY AUTOINCREMENT,
    de_ag0  BOOLEAN (1),
    de_ag1  BOOLEAN (1),
    de_ag2  BOOLEAN (1),
    de_ag3  BOOLEAN (1),
    de_ag4  BOOLEAN (1),
    de_ag5  BOOLEAN (1),
    de_ag6  BOOLEAN (1),
    de_ag7  BOOLEAN (1),
    de_ag8  BOOLEAN (1),
    de_ag9  BOOLEAN (1),
    de_ag10 BOOLEAN (1),
    de_ag11 BOOLEAN (1),
    de_ag12 BOOLEAN (1),
    de_ag13 BOOLEAN (1),
    de_ag14 BOOLEAN (1) 
);

DROP INDEX ICADMEDAGEN0;
CREATE INDEX ICADMEDAGEN0 ON TCADMEDAGEN0 (
    id_med ASC,
    id_end ASC
);


-- Contato --
CREATE TABLE TCADMEDCONT0 (
    id_med    INTEGER REFERENCES TCADMED0 (id_med) ON DELETE CASCADE
                                                   ON UPDATE NO ACTION,
    id_cont   INTEGER PRIMARY KEY AUTOINCREMENT,
    id_conv   INTEGER REFERENCES TCADCONV0 (id_conv) ON DELETE NO ACTION
                                                     ON UPDATE NO ACTION,
    de_email1 TEXT,
    de_email2 TEXT,
    nu_cel1   TEXT,
    nu_cel2   TEXT,
    nu_cel3   TEXT,
    de_obs    TEXT
);

CREATE INDEX ICADMEDCONT0 ON TCADMEDCONT0 (
    id_med,
    id_cont,
    id_conv
);

-- Medico Local--
CREATE TABLE TCADMEDLOC0 (
    id_med   INTEGER REFERENCES TCADMED0 (id_med) ON DELETE CASCADE
                                                  ON UPDATE NO ACTION,
    id_local INTEGER
);

CREATE INDEX ICADMEDLOC0 ON TCADMEDLOC0 (
    id_med,
    id_local
);


-- Medico Convenio --
CREATE TABLE TCADMEDCONV0 (
    id_med  INTEGER REFERENCES TCADMED0 (id_med) ON DELETE NO ACTION
                                                 ON UPDATE NO ACTION,
    id_conv INTEGER
);

CREATE INDEX ICADMEDCON0 ON TCADMEDCONV0 (
    id_med,
    id_conv
);




