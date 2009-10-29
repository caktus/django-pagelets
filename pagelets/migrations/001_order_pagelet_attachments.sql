ALTER TABLE pagelets_pageattachment ADD COLUMN "order" SMALLINT;
UPDATE pagelets_pageattachment SET "order" = 0;
ALTER TABLE pagelets_pageattachment ALTER COLUMN "order" SET NOT NULL;
