import pandas as pd
import numpy as np


def load_data(data_path: str) -> pd.DataFrame:
    """Load the data from the csv file at the provided path.

    Loads the data from the provided csv file. Only the columns required for this stage are loaded.
    These are:
        budget
        revenue
        imdb_id
    The budget and revenue values are cast to floats, or set to NaN if this is not possible due to faulty data.

    Parameters
    ----------
    data_path : str
        A string specifying the path to where the required csv is.

    Returns
    -------
    pd.DataFrame
        The loaded data with only the required columns.
    """
    df = pd.read_csv(
        data_path,
        usecols=[
            "budget",
            "revenue",
            "imdb_id",
            "title",
            "production_companies",
            "release_date",
        ],
        # TODO don't do this, make the links.csv match with this
        converters={"imdb_id": lambda x: x[2:]}
    )
    df["budget"] = pd.to_numeric(df["budget"], errors="coerce")
    df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
    df["imdb_id"] = pd.to_numeric(df["imdb_id"], errors="coerce")
    df["year"] = pd.to_datetime(df["release_date"], errors="coerce").apply(
        lambda x: x.year
    )
    df.drop(columns=["release_date"], inplace=True)
    # TODO process production companies
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans the data.

    Remove rows with NaNs in the required columns, or where the budget or revenue is 0.
    A budget of 0 is unrealistic and so is surely an incorrect value.
    A revenue of zero is also probably a mistake, but if not then it is useless to us anyway
    and will result in inf for the ratio.

    Parameters
    ----------
    df : pd.DataFrame
        The dataframe to clean.

    Returns
    -------
    pd.DataFrame
        The cleaned dataframe.
    """
    initial_rows = df.shape[0]
    df["budget"] = df["budget"].replace(0, np.nan)
    df["revenue"] = df["revenue"].replace(0, np.nan)
    # If budget or revenue is NaN then the row is useless because we can't calculate its ratio
    df = df[~df[["budget", "revenue"]].isna().any(axis=1)]
    dropped_rows = initial_rows - df.shape[0]
    # TODO replace ALL prints with logger
    print(
        f"Dropped {dropped_rows} ({100*dropped_rows/initial_rows:.3}%) rows due to missing/dirty/0 values"
    )
    return df


def get_top_films_by_budget_revenue_ratio(data_path: str) -> pd.DataFrame:
    """ Returns the 1000 films with the best budget to revenue ratio.

    Loads the csv file at the given location, calculates the ratio of budget
    to revenue and

    Parameters
    ----------
    data_path : str
        Path to csv file of films to load and process.

    Returns
    -------
    pd.DataFrame
        The 1000 films with the best budget to revenue ratio.
        Columns:
            title
            imdb_id
            budget
            revenue
            budget_revenue_ratio
            year
            production_companies
    """
    film_metadata_df = clean_data(load_data(data_path))
    film_metadata_df["budget_revenue_ratio"] = (
        film_metadata_df["budget"] / film_metadata_df["revenue"]
    )
    top_films = film_metadata_df.sort_values(by=["budget_revenue_ratio"])[:1000]
    return top_films
