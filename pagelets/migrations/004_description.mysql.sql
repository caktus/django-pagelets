BEGIN;
ALTER TABLE pagelets_page ADD COLUMN description longtext;
UPDATE pagelets_page SET description = '';
ALTER TABLE pagelets_page MODIFY description longtext NOT NULL;
COMMIT;
