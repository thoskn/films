import os

from augment_data import augment
from load import load
from top_films import get_top_films_by_budget_revenue_ratio

top_films = get_top_films_by_budget_revenue_ratio("movies_metadata.csv")
augmented_data = augment(top_films, "links.csv", "ratings.csv")
load(augmented_data, os.environ["POSTGRES_HOST"], "films")
