BEGIN;
CREATE TABLE "pagelets_inlinepagelet" (
    "pagelet_ptr_id" integer NOT NULL PRIMARY KEY REFERENCES "pagelets_pagelet" ("pageletbase_ptr_id") DEFERRABLE INITIALLY DEFERRED,
    "order" smallint,
    "area" varchar(32) NOT NULL,
    "page_id" integer NOT NULL REFERENCES "pagelets_page" ("pageletbase_ptr_id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE "pagelets_sharedpagelet" (
    "id" serial NOT NULL PRIMARY KEY,
    "order" smallint,
    "area" varchar(32) NOT NULL,
    "pagelet_id" integer NOT NULL REFERENCES "pagelets_pagelet" ("pageletbase_ptr_id") DEFERRABLE INITIALLY DEFERRED,
    "page_id" integer NOT NULL REFERENCES "pagelets_page" ("pageletbase_ptr_id") DEFERRABLE INITIALLY DEFERRED,
    UNIQUE ("pagelet_id", "page_id")
);
INSERT INTO pagelets_inlinepagelet SELECT pageletbase_ptr_id, "order", 'main', page_id FROM pagelets_pagelet WHERE page_id IS NOT NULL;
ALTER TABLE pagelets_pagelet DROP COLUMN page_id;
ALTER TABLE pagelets_pagelet DROP COLUMN "order";
COMMIT;
