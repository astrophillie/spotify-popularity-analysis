from pathlib import Path


def interpret_correlation(value):
    """Return a short interpretation of a correlation value."""
    strength_value = abs(value)

    if strength_value < 0.30:
        strength = "weak"
    elif strength_value < 0.70:
        strength = "moderate"
    else:
        strength = "strong"

    if value > 0:
        direction = "positive"
    elif value < 0:
        direction = "negative"
    else:
        return "This suggests no linear relationship."

    return f"This suggests a {strength} {direction} linear relationship."


def create_insights_report(
    clean_df,
    popularity_statistics,
    duration_statistics,
    popular_tracks,
    top_genre_popularity,
    explicit_counts,
    explicit_popularity,
    correlation_matrix,
    energy_loudness_df,
):
    """Create and save a text report from the Spotify analysis results."""
    energy_loudness_correlation = energy_loudness_df["energy"].corr(
        energy_loudness_df["loudness"]
    )
    popularity_correlations = (
        correlation_matrix["popularity"]
        .drop("popularity")
        .dropna()
    )
    strongest_feature = popularity_correlations.abs().idxmax()
    strongest_value = popularity_correlations[strongest_feature]
    explicit_means = explicit_popularity

    lines = [
        "SPOTIFY TRACK ANALYSIS",
        "=" * 60,
        "",
        "1. DATASET OVERVIEW",
        f"Cleaned tracks: {len(clean_df):,}",
        f"Columns: {clean_df.shape[1]}",
        "",
        "2. POPULARITY",
        f"Mean: {popularity_statistics['mean']:.2f}",
        f"Median: {popularity_statistics['median']:.2f}",
        f"Minimum: {popularity_statistics['min']:.2f}",
        f"Maximum: {popularity_statistics['max']:.2f}",
        "",
        "3. TRACK DURATION",
        f"Mean minutes: {duration_statistics['mean']:.2f}",
        f"Median minutes: {duration_statistics['median']:.2f}",
        f"Minimum minutes: {duration_statistics['min']:.2f}",
        f"Maximum minutes: {duration_statistics['max']:.2f}",
        "",
        "4. MOST POPULAR TRACKS",
    ]

    for _, track in popular_tracks.iterrows():
        lines.append(
            f"{track['track_name']} | {track['artists']} | "
            f"{track['track_genre']} | popularity {track['popularity']}"
        )

    lines.extend([
        "",
        "5. GENRES BY AVERAGE POPULARITY",
    ])
    for genre, average in top_genre_popularity.items():
        lines.append(f"{genre}: {average:.2f}")

    false_count = explicit_counts.get(False, 0)
    true_count = explicit_counts.get(True, 0)
    false_mean = explicit_means.get(False, float("nan"))
    true_mean = explicit_means.get(True, float("nan"))

    lines.extend([
        "",
        "6. EXPLICIT VERSUS NON-EXPLICIT TRACKS",
        f"Non-explicit tracks: {false_count}",
        f"Explicit tracks: {true_count}",
        f"Non-explicit average popularity: {false_mean:.2f}",
        f"Explicit average popularity: {true_mean:.2f}",
    ])

    if true_mean > false_mean:
        lines.append("Explicit tracks have the higher average popularity.")
    elif true_mean < false_mean:
        lines.append("Non-explicit tracks have the higher average popularity.")
    else:
        lines.append("Both groups have the same average popularity.")

    lines.extend([
        "",
        "7. AUDIO-FEATURE CORRELATIONS",
        f"Energy/loudness correlation: {energy_loudness_correlation:.2f}",
        interpret_correlation(energy_loudness_correlation),
        f"Strongest feature relationship with popularity: {strongest_feature} "
        f"({strongest_value:.2f})",
        interpret_correlation(strongest_value),
        "",
        "8. INTERPRETATION NOTE",
        "Correlation describes association, but it does not prove causation.",
        "The results describe this dataset and may not represent all Spotify tracks.",
    ])

    report_text = "\n".join(lines)
    output_directory = Path(__file__).parent / "output"
    output_directory.mkdir(parents=True, exist_ok=True)
    report_path = output_directory / "spotify_insights_report.txt"
    report_path.write_text(report_text, encoding="utf-8")

    print(report_text)
    print(f"Report saved to: {report_path}")
    return report_text
