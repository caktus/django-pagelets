ALTER TABLE pagelets_page ADD COLUMN `tags` varchar(255);
UPDATE pagelets_page SET tags = '';
ALTER TABLE pagelets_page MODIFY tags varchar(255) NOT NULL;
