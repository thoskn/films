import pandas as pd
from sqlalchemy import create_engine


def load(df: pd.DataFrame, host: str, database_name: str, user: str, password: str):
    engine = create_engine(f"postgresql://{host}:5432/{database_name}?user={user}&password={password}")
    df.to_sql("top_films", con=engine)
