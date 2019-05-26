--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.10
-- Dumped by pg_dump version 9.6.10

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: _dogodek; Type: TABLE; Schema: public; Owner: rebasedata
--

CREATE TABLE public._dogodek (
    id integer,
    ime character varying(7) DEFAULT NULL::character varying,
    datum character varying(10) DEFAULT NULL::character varying,
    organizator character varying(4) DEFAULT NULL::character varying,
    opis character varying(41) DEFAULT NULL::character varying
);


ALTER TABLE public._dogodek OWNER TO rebasedata;

--
-- Name: _uporabnik; Type: TABLE; Schema: public; Owner: rebasedata
--

CREATE TABLE public._uporabnik (
    id integer,
    mail character varying(17) DEFAULT NULL::character varying,
    geslo character varying(12) DEFAULT NULL::character varying,
    status integer,
    potrjen integer
);


ALTER TABLE public._uporabnik OWNER TO rebasedata;

--
-- Name: _vnoskoledar; Type: TABLE; Schema: public; Owner: rebasedata
--

CREATE TABLE public._vnoskoledar (
    id integer,
    naziv character varying(12) DEFAULT NULL::character varying,
    opis character varying(25) DEFAULT NULL::character varying,
    trajanje integer,
    zacetek character varying(19) DEFAULT NULL::character varying,
    idu integer
);


ALTER TABLE public._vnoskoledar OWNER TO rebasedata;

--
-- Name: _vnostodo; Type: TABLE; Schema: public; Owner: rebasedata
--

CREATE TABLE public._vnostodo (
    id integer,
    vsebina character varying(61) DEFAULT NULL::character varying,
    idu integer
);


ALTER TABLE public._vnostodo OWNER TO rebasedata;

--
-- Name: _vnosurnik; Type: TABLE; Schema: public; Owner: rebasedata
--

CREATE TABLE public._vnosurnik (
    id integer,
    naziv character varying(3) DEFAULT NULL::character varying,
    barva integer,
    trajanje integer,
    zacetek character varying(8) DEFAULT NULL::character varying,
    dan character varying(3) DEFAULT NULL::character varying,
    idu integer
);


ALTER TABLE public._vnosurnik OWNER TO rebasedata;

--
-- Data for Name: _dogodek; Type: TABLE DATA; Schema: public; Owner: rebasedata
--

COPY public._dogodek (id, ime, datum, organizator, opis) FROM stdin;
1	Škisova	2019-05-09	Škis	Škisova tržnica na temni strani Ljubljane
\.


--
-- Data for Name: _uporabnik; Type: TABLE DATA; Schema: public; Owner: rebasedata
--

COPY public._uporabnik (id, mail, geslo, status, potrjen) FROM stdin;
0	andreja@gmail.com	MojeGeslo	0	0
1	blaz@gmail.com	NjegovoGeslo	1	1
2	katja@gmail.com	NjenoGeslo	2	1
3	regina@gmail.com	NjenoGeslo2	0	1
\.


--
-- Data for Name: _vnoskoledar; Type: TABLE DATA; Schema: public; Owner: rebasedata
--

COPY public._vnoskoledar (id, naziv, opis, trajanje, zacetek, idu) FROM stdin;
1	Kolokvij PUI	Kolokvij iz predmeta PUI	1	2019-06-09 14:00:00	3
2	PZ TPO	Preverjanje znanja iz TPO	1	2019-05-23 09:00:00	3
\.


--
-- Data for Name: _vnostodo; Type: TABLE DATA; Schema: public; Owner: rebasedata
--

COPY public._vnostodo (id, vsebina, idu) FROM stdin;
1	To bojo sedaj moji zapiski.	3
2	V ?etrtek ne smem pozabiti narediti doma?e naloge za v petek.	3
3	Ta link mi pomaga pri dn za MAT: www.nekajnekaj.si	3
\.


--
-- Data for Name: _vnosurnik; Type: TABLE DATA; Schema: public; Owner: rebasedata
--

COPY public._vnosurnik (id, naziv, barva, trajanje, zacetek, dan, idu) FROM stdin;
1	PUI	2	3	12:00:00	CET	3
2	TPO	3	3	09:00:00	CET	3
3	BMO	7	3	11:00:00	PON	3
\.


--
-- PostgreSQL database dump complete
--

