from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns


def create_output_directory():
    """
    Create the folder used for generated charts.
    """

    output_directory = Path(__file__).parent / "output" / "charts"

    output_directory.mkdir(parents=True, exist_ok=True)
    return output_directory


def plot_popularity_distribution(clean_df, output_directory):
    """
    Create a histogram showing the distribution of popularity.

    Questions:
    - Where are most popularity values concentrated?
    - Is the distribution symmetrical or skewed?
    - Are very popular tracks uncommon?
    """

    plt.figure(figsize=(10, 6))
    sns.histplot(data=clean_df, x="popularity", bins=20, kde=True)
    plt.title("Distribution of Track Popularity")
    plt.xlabel("Popularity")
    plt.ylabel("Number of Tracks")
    plt.grid(axis="y")
    plt.tight_layout()
    plt.savefig(output_directory / "popularity_distribution.png", dpi=150)
    plt.show()
    plt.close()


def plot_explicit_popularity(clean_df, output_directory):
    """
    Create a boxplot comparing popularity for:
    - non-explicit tracks;
    - explicit tracks.

    Questions:
    - Which group has the higher median?
    - Which group has the wider range?
    - Are there outliers?
    """

    plt.figure(figsize=(10, 6))
    sns.boxplot(data=clean_df, x="explicit", y="popularity")
    plt.title("Popularity by Explicit Status")
    plt.xlabel("Explicit")
    plt.ylabel("Popularity")
    plt.grid(axis="y")
    plt.tight_layout()
    plt.savefig(output_directory / "explicit_popularity_boxplot.png", dpi=150)
    plt.show()
    plt.close()


def plot_top_genres(top_genre_popularity, output_directory):
    """
    Create a bar chart showing the genres with the
    highest average popularity.

    The function receives the Series previously created by:
    inspect_genre_statistics().
    """

    plt.figure(figsize=(10, 6))
    sns.barplot(
        x=top_genre_popularity.values,
        y=top_genre_popularity.index,
    )
    plt.title("Top Genres by Average Popularity")
    plt.xlabel("Average Popularity")
    plt.ylabel("Genre")
    plt.tight_layout()
    plt.savefig(output_directory / "top_genres_by_popularity.png", dpi=150)
    plt.show()
    plt.close()


def plot_energy_and_loudness(energy_loudness_df, output_directory):
    """
    Create a scatter plot showing the relationship
    between energy and loudness.

    Each point represents one track.

    Questions:
    - Does loudness increase together with energy?
    - Is the relationship positive, negative, or weak?
    - Are there unusual values?
    """

    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=energy_loudness_df,
        x="energy",
        y="loudness",
        alpha=0.2,
    )
    plt.title("Energy and Loudness")
    plt.xlabel("Energy")
    plt.ylabel("Loudness")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_directory / "energy_and_loudness.png", dpi=150)
    plt.show()
    plt.close()


def plot_correlation_heatmap(correlation_matrix, output_directory):
    """
    Create a heatmap of the audio-feature correlations.

    Interpretation:
    - values near 1 indicate a strong positive relationship;
    - values near -1 indicate a strong negative relationship;
    - values near 0 indicate a weak linear relationship.
    """

    plt.figure(figsize=(12, 10))
    sns.heatmap(
        correlation_matrix,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        center=0,
    )
    plt.title("Audio Feature Correlations")
    plt.tight_layout()
    plt.savefig(
        output_directory / "audio_feature_correlation_heatmap.png",
        dpi=150,
    )
    plt.show()
    plt.close()