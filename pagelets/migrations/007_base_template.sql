BEGIN;
ALTER TABLE pagelets_page ADD COLUMN base_template varchar(255);
UPDATE pagelets_page SET base_template='';
ALTER TABLE pagelets_page ALTER COLUMN base_template SET NOT NULL;
COMMIT;
