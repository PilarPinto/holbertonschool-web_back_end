-- Ranked and select
SELECT band_name, COALESCE(split, 2020) - formed AS 'lifespan'
FROM metal_bands WHERE FIND_IN_SET('Glam rock', style) ORDER BY lifespan DESC;
