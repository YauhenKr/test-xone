SELECT brand.title brand, COUNT(brand_id) FROM public.notebooks_notebook notebook
INNER JOIN public.notebooks_brand brand ON notebook.brand_id = brand.id
GROUP BY brand.title
ORDER BY COUNT(brand_id) DESC;

SELECT COUNT(brand_id) count_notebooks, 
	CEIL(width / 5) * 5 width,
	CEIL(depth / 5) * 5 depth,
	CEIL(height / 5) * 5 height,
	CEIL(diagonal / 5) * 5 diagonal
FROM public.notebooks_notebook notebook
GROUP BY width, depth, height, diagonal
ORDER BY width, depth, height, diagonal ASC;
