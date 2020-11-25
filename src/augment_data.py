import pandas as pd


def join_with_ids(df: pd.DataFrame, id_link_csv_path: str) -> pd.DataFrame:
    id_link_df = pd.read_csv(id_link_csv_path)
    df = df.join(id_link_df.set_index("imdbId"), on="imdb_id")
    return df


def aggregate_ratings(ratings_csv_path: str) -> pd.DataFrame:
    ratings_df = pd.read_csv(ratings_csv_path)
    return ratings_df.groupby("movieId")["rating"].mean()


def join_with_ratings(df: pd.DataFrame, ratings_csv_path: str) -> pd.DataFrame:
    # TODO check joining correctly (movies get their correct ratings)
    ratings_df = aggregate_ratings(ratings_csv_path)
    df = df.join(ratings_df, on="movieId")
    return df


def join_with_wiki(df: pd.DataFrame) -> pd.DataFrame:
    pass


def augment(df: pd.DataFrame) -> pd.DataFrame:
    df = join_with_ids(df, "../data/archive/links.csv")
    df = join_with_ratings(df, "../data/archive/ratings.csv")
    return df
