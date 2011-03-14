BEGIN;
ALTER TABLE pagelets_page ADD COLUMN meta_description text;
ALTER TABLE pagelets_page ADD COLUMN meta_keywords varchar(200);
ALTER TABLE pagelets_page ADD COLUMN meta_robots varchar(20);
UPDATE pagelets_page SET meta_description='', meta_keywords='', meta_robots='';
ALTER TABLE pagelets_page ALTER COLUMN meta_description set NOT NULL;
ALTER TABLE pagelets_page ALTER COLUMN meta_keywords set NOT NULL;
ALTER TABLE pagelets_page ALTER COLUMN meta_robots set NOT NULL;
COMMIT;
