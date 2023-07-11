
CREATE TABLE public.employees(
  employee_id integer NOT NULL,
  first_name character varying(128) NOT NULL,
  last_name character varying(128) NOT NULL
  );


CREATE TABLE public.entries (
  entry_id integer NOT NULL,
  employee_id integer NOT NULL,
  entry_date timestamp without time zone DEFAULT now(),
  hours double precision
);
