BEGIN;
ALTER TABLE pagelets_pageattachment ALTER COLUMN "order" DROP NOT NULL;
COMMIT;
