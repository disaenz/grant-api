-- 1) Create the schema
CREATE SCHEMA IF NOT EXISTS grant_schema;

-- 2) Switch into that schema
SET search_path TO grant_schema;

-- 3) Create the grants table
CREATE TABLE IF NOT EXISTS grants (
  id             SERIAL PRIMARY KEY,
  name           VARCHAR(255)   NOT NULL,
  program        VARCHAR(255)   NOT NULL,
  type           VARCHAR(100)   NOT NULL,
  status         VARCHAR(50)    NOT NULL,
  start_date     DATE           NOT NULL,
  deadline       DATE           NOT NULL,
  budget_range   VARCHAR(50)    NOT NULL,
  created_at     TIMESTAMPTZ    NOT NULL DEFAULT NOW(),
  updated_at     TIMESTAMPTZ    NOT NULL DEFAULT NOW(),
  notes          TEXT
);

-- 4) Trigger function for updated_at
CREATE OR REPLACE FUNCTION grant_schema.update_timestamp()
  RETURNS TRIGGER
  LANGUAGE plpgsql
AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$;

-- 5) Attach trigger to auto‐update updated_at on modifications
DROP TRIGGER IF EXISTS set_updated_at ON grant_schema.grants;
CREATE TRIGGER set_updated_at
  BEFORE UPDATE ON grant_schema.grants
  FOR EACH ROW
  EXECUTE PROCEDURE grant_schema.update_timestamp();