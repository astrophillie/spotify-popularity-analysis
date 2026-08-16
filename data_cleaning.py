import pandas as pd


def inspect_dataset(spotify_df):
    print(spotify_df.head())
    print(spotify_df.shape)
    print(spotify_df.columns.tolist())
    spotify_df.info()


def inspect_missing_values(spotify_df):
    missing_values = spotify_df.isna().sum()
    print(missing_values[missing_values > 0])


def inspect_duplicates(spotify_df):
    duplicate_mask = spotify_df.duplicated(keep=False)
    print("EXACT DUPLICATE ROWS:", duplicate_mask.sum())

    track_id_duplicate_mask = spotify_df.duplicated(
        subset=["track_id"],
        keep=False,
    )
    print("DUPLICATE TRACK IDs:", track_id_duplicate_mask.sum())

    return duplicate_mask, track_id_duplicate_mask



def inspect_categories(spotify_df):
    text_columns = [
        "artists",
        "album_name",
        "track_name",
        "track_genre",
    ]

    genre_count = spotify_df["track_genre"].nunique()
    common_genres = spotify_df["track_genre"].value_counts().head(10)
    artist_count = spotify_df["artists"].nunique()
    explicit_counts = spotify_df["explicit"].value_counts(dropna=False)

    print("UNIQUE GENRES:", genre_count)
    print("MOST COMMON GENRES:")
    print(common_genres)
    print("UNIQUE ARTISTS:", artist_count)
    print("EXPLICIT TRACK COUNTS:")
    print(explicit_counts)

    print("MISSING TEXT VALUES:")
    print(spotify_df[text_columns].isna().sum())

    whitespace_counts = {
        column: spotify_df[column]
        .astype("string")
        .str.strip()
        .ne(spotify_df[column].astype("string"))
        .sum()
        for column in text_columns
    }
    print("TEXT VALUES WITH EXTRA SPACES:")
    print(pd.Series(whitespace_counts))


def inspect_numeric_ranges(spotify_df):

    numeric_columns = [
        "popularity",
        "duration_ms",
        "danceability",
        "energy",
        "loudness",
        "speechiness",
        "acousticness",
        "instrumentalness",
        "liveness",
        "valence",
        "tempo",
    ]

    numeric_columns_df = spotify_df[numeric_columns]
    print(numeric_columns_df.describe())

    valid_rules = {
        "popularity": lambda values: values.between(0, 100),
        "duration_ms": lambda values: values.gt(0),
        "danceability": lambda values: values.between(0, 1),
        "energy": lambda values: values.between(0, 1),
        "loudness": lambda values: values.between(-60, 0),
        "speechiness": lambda values: values.between(0, 1),
        "acousticness": lambda values: values.between(0, 1),
        "instrumentalness": lambda values: values.between(0, 1),
        "liveness": lambda values: values.between(0, 1),
        "valence": lambda values: values.between(0, 1),
        "tempo": lambda values: values.between(0, 250),
    }

    invalid_values = {
        column: values[~is_valid(values)]
        for column, is_valid in valid_rules.items()
        for values in [numeric_columns_df[column].dropna()]
    }

    for column, values in invalid_values.items():
        if not values.empty:
            print(f"INVALID {column.upper()} VALUES:")
            print(values)

    popularity_groups = pd.cut(
        spotify_df["popularity"],
        bins=[-1, 20, 40, 60, 80, 100],
        labels=["0-20", "21-40", "41-60", "61-80", "81-100"],
    )
    print("POPULARITY GROUPS:")
    print(popularity_groups.value_counts().sort_index())


def clean_dataset(spotify_df):

    spotify_df_clean = spotify_df.copy()

    rows_before = len(spotify_df_clean)
    spotify_df_clean = spotify_df_clean.drop_duplicates()
    duplicate_rows_removed = rows_before - len(spotify_df_clean)

    invalid_duration_mask = spotify_df_clean["duration_ms"] <= 0
    invalid_duration_count = invalid_duration_mask.sum()
    spotify_df_clean = spotify_df_clean.loc[~invalid_duration_mask].copy()

    text_columns = [
        "artists",
        "album_name",
        "track_name",
        "track_genre",
    ]
    for column in text_columns:
        spotify_df_clean[column] = (
            spotify_df_clean[column]
            .astype("string")
            .str.strip()
        )

    print("EXACT DUPLICATE ROWS REMOVED:", duplicate_rows_removed)
    print("INVALID DURATION ROWS REMOVED:", invalid_duration_count)
    print("CLEANED SHAPE:", spotify_df_clean.shape)

    return spotify_df_clean


