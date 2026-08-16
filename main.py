from pathlib import Path

import pandas as pd

from insights_report import create_insights_report

from data_cleaning import (
    inspect_dataset,
    inspect_missing_values,
    inspect_duplicates,
    inspect_categories,
    inspect_numeric_ranges,
    clean_dataset,
)

from descriptive_statistics import (
    inspect_numeric_summary,
    inspect_popularity_statistics,
    inspect_duration_statistics,
    find_most_popular_tracks,
    inspect_genre_statistics,
    compare_explicit_tracks,
    inspect_audio_feature_correlations,
    compare_energy_and_loudness,
)

from data_visualisation import (
    create_output_directory,
    plot_popularity_distribution,
    plot_explicit_popularity,
    plot_top_genres,
    plot_energy_and_loudness,
    plot_correlation_heatmap,
)

base_dir = Path(__file__).parent
dataset_path = base_dir / "data" / "spotify-tracks-dataset-detailed.csv"

spotify_df = pd.read_csv(
    dataset_path,
    encoding="utf-8"
)

# inspect_dataset(spotify_df)

# inspect_missing_values(spotify_df)
inspect_duplicates(spotify_df)
# inspect_categories(spotify_df)
# inspect_numeric_ranges(spotify_df)

clean_df = clean_dataset(spotify_df)
inspect_numeric_summary(clean_df)

popularity_statistics = inspect_popularity_statistics(clean_df)
duration_df, duration_statistics = inspect_duration_statistics(clean_df)
popular_tracks = find_most_popular_tracks(clean_df)
(
    top_genre_counts,
    top_genre_popularity,
    top_genre_median_popularity,
) = inspect_genre_statistics(clean_df)
explicit_counts, explicit_popularity = compare_explicit_tracks(clean_df)
correlation_matrix = inspect_audio_feature_correlations(clean_df)
energy_loudness_df = compare_energy_and_loudness(clean_df)

output_directory = create_output_directory()

create_insights_report(
    clean_df,
    popularity_statistics,
    duration_statistics,
    popular_tracks,
    top_genre_popularity,
    explicit_counts,
    explicit_popularity,
    correlation_matrix,
    energy_loudness_df,
)

plot_popularity_distribution(
    clean_df,
    output_directory,
)

plot_explicit_popularity(
    clean_df,
    output_directory,
)

plot_top_genres(
    top_genre_popularity,
    output_directory,
)

plot_energy_and_loudness(
    energy_loudness_df,
    output_directory,
)

plot_correlation_heatmap(
    correlation_matrix,
    output_directory,
)