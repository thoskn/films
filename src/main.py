from src.augment_data import augment
from src.top_films import get_top_films_by_budget_revenue_ratio

top_films = get_top_films_by_budget_revenue_ratio("data/archive/movies_metadata.csv")
augmented_data = augment(top_films)
