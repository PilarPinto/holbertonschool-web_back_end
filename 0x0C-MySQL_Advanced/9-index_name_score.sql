-- Creates an index with 3 params
CREATE INDEX idx_name_first_score ON names(name(1), score);
