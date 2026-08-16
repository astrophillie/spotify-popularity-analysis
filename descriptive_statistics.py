import pandas as pd


def inspect_numeric_summary(clean_df):

    numeric_df = clean_df.select_dtypes(include="number")
    print("NUMERIC SUMMARY:")
    print(numeric_df.describe())


def inspect_popularity_statistics(clean_df):
    popularity_values = clean_df["popularity"]
    statistic_names = ["mean", "median", "min", "max"]

    popularity_statistics = {
        name: getattr(popularity_values, name)()
        for name in statistic_names
    }

    print("POPULARITY STATISTICS:")
    for name, value in popularity_statistics.items():
        print(f"{name.upper()}:", value)

    return popularity_statistics


def inspect_duration_statistics(clean_df):

    duration_df = clean_df.copy()
    duration_df["duration_minutes"] = (
        duration_df["duration_ms"] / 1000 / 60
    )

    duration_values = duration_df["duration_minutes"]
    statistic_names = ["mean", "median", "min", "max"]
    duration_statistics = {
        name: getattr(duration_values, name)()
        for name in statistic_names
    }

    print("DURATION STATISTICS IN MINUTES:")
    for name, value in duration_statistics.items():
        print(f"{name.upper()}:", value)

    return duration_df, duration_statistics


def find_most_popular_tracks(clean_df):

    report_columns = [
        "track_name",
        "artists",
        "track_genre",
        "popularity",
    ]

    popular_tracks = clean_df.sort_values(
        by="popularity",
        ascending=False,
    ).drop_duplicates(subset="track_id")

    popular_tracks = popular_tracks[report_columns].head(10)
    print("10 MOST POPULAR UNIQUE TRACKS:")
    print(popular_tracks)
    return popular_tracks


def inspect_genre_statistics(clean_df):

    genre_counts = clean_df["track_genre"].value_counts()
    genre_popularity = clean_df.groupby("track_genre")["popularity"].mean()
    genre_median_popularity = clean_df.groupby("track_genre")["popularity"].median()

    top_genre_counts = genre_counts.head(10)
    top_genre_popularity = genre_popularity.sort_values(
        ascending=False
    ).head(10)
    top_genre_median_popularity = genre_median_popularity.sort_values(
        ascending=False
    ).head(10)

    print("TOP 10 GENRE COUNTS:")
    print(top_genre_counts)
    print("TOP 10 AVERAGE POPULARITY BY GENRE:")
    print(top_genre_popularity)
    print("TOP 10 MEDIAN POPULARITY BY GENRE:")
    print(top_genre_median_popularity)

    return (
        top_genre_counts,
        top_genre_popularity,
        top_genre_median_popularity,
    )


def compare_explicit_tracks(clean_df):
    explicit_counts = clean_df["explicit"].value_counts(dropna=False)
    print("EXPLICIT TRACK COUNTS:")
    print(explicit_counts)

    explicit_popularity = clean_df.groupby(
        "explicit",
        dropna=False,
    )["popularity"].mean()
    print("AVERAGE POPULARITY BY EXPLICIT STATUS:")
    print(explicit_popularity)
    return explicit_counts, explicit_popularity


def inspect_audio_feature_correlations(clean_df):
    correlation_columns = [
        "popularity",
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

    clean_df = clean_df[correlation_columns]
    
    correlation_matrix = clean_df.corr()

    popularity_correlations = correlation_matrix["popularity"].sort_values(ascending=False)
    print("CORRELATIONS WITH POPULARITY:")
    print(popularity_correlations)

    return correlation_matrix


def compare_energy_and_loudness(clean_df):

    selected_columns = [
        "track_name",
        "artists",
        "energy",
        "loudness",
    ]
    
    comparison_df = clean_df[selected_columns].dropna(
        subset=["energy", "loudness"]
    )

    correlation = comparison_df["energy"].corr(
        comparison_df["loudness"]
    )
    print("CORRELATION BETWEEN ENERGY AND LOUDNESS:", correlation)

    return comparison_df
