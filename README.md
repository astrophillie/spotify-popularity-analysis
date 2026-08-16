# Spotify Popularity Analysis

A Python data-analysis project exploring what the Spotify tracks dataset shows about track popularity, duration, genres, explicit content, and audio features.

The project is an exercise in building a complete pandas workflow from a raw CSV file to cleaned data, descriptive statistics, visualizations, and a short written report.

## Table of Contents

- [Project Description](#project-description)
- [Motivation](#motivation)
- [Features](#features)
- [What I Learned](#what-i-learned)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [How To Use](#how-to-use)
- [Current Results](#current-results)
- [Data Source and Credits](#data-source-and-credits)
- [Future Improvements](#future-improvements)
- [License](#license)

## Project Description

The project loads a Spotify tracks dataset and investigates a few questions:

- How is popularity distributed across the tracks?
- What are the most popular unique tracks?
- Which genres have the highest average and median popularity?
- Do explicit and non-explicit tracks have different average popularity values?
- How are popularity and audio features related?
- How strongly are energy and loudness related?

The analysis creates five charts and a text report from the cleaned data.

## Motivation

I built this project to practice the steps involved in a small data-analysis project rather than only working with isolated pandas exercises. It gave me a dataset with repeated track IDs, missing values, numeric ranges to inspect, categorical columns to compare, and enough audio features to practice correlations and visualizations.

The project does not try to predict popularity or explain why a track becomes popular. It is an exploratory analysis of the records available in this dataset.

## Features

- Inspects dataset shape, columns, data types, missing values, and duplicates.
- Separates complete duplicate rows from repeated `track_id` values.
- Counts genres, artists, and explicit/non-explicit tracks.
- Checks practical numeric ranges for popularity and audio features.
- Removes exact duplicate rows and tracks with non-positive duration.
- Strips unnecessary surrounding spaces from text columns.
- Calculates popularity and duration statistics.
- Finds the most popular tracks without repeating the same `track_id`.
- Compares genre popularity using both mean and median values.
- Compares explicit and non-explicit tracks.
- Calculates correlations between popularity and audio features.
- Generates a histogram, boxplot, bar chart, scatter plot, and correlation heatmap.
- Saves an insights report as a text file.

## What I Learned

- How to separate inspection from cleaning decisions.
- How to use `select_dtypes()`, `describe()`, `groupby()`, `value_counts()`, and `corr()`.
- How to use dictionaries of validation functions with lambdas.
- Why repeated IDs are not always errors in a dataset.
- How to avoid treating missing values as invalid numeric values automatically.
- How to create reusable plotting functions.
- How to interpret correlation as association rather than causation.
- How to organize a small analysis project for reproducibility.

## Technologies

- Python 3.12+
- pandas
- Matplotlib
- Seaborn

## Project Structure

```text
spotify_popularity_analysis/
|-- data/
|   |-- README.md
|   `-- spotify-tracks-dataset-detailed.csv  # local input; not committed
|-- output/
|   |-- charts/                              # generated chart images
|   `-- spotify_insights_report.txt         # generated report
|-- data_cleaning.py
|-- descriptive_statistics.py
|-- data_visualisation.py
|-- insights_report.py
|-- main.py
|-- requirements.txt
`-- .gitignore
```

## Installation

Clone the repository and open the project directory:

```powershell
git clone https://github.com/YOUR_USERNAME/spotify-popularity-analysis.git
cd spotify-popularity-analysis
```

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

## How To Use

1. Obtain the dataset described in [data/README.md](data/README.md).
2. Place it at:

   ```text
   data/spotify-tracks-dataset-detailed.csv
   ```

3. Run the main workflow:

   ```powershell
   python main.py
   ```

The script prints the inspection and statistics results in the terminal. It creates these charts in `output/charts/`:

- `popularity_distribution.png`
- `explicit_popularity_boxplot.png`
- `top_genres_by_popularity.png`
- `energy_and_loudness.png`
- `audio_feature_correlation_heatmap.png`

It also creates:

```text
output/spotify_insights_report.txt
```

## Current Results

The current run produced these results after cleaning:

- `113,549` tracks remained after exact duplicates and non-positive durations were removed.
- Mean popularity was `33.32`; median popularity was `35.00`.
- Mean duration was `3.80` minutes; median duration was `3.55` minutes.
- Explicit tracks had average popularity of `36.52`; non-explicit tracks had `33.02`.
- `pop-film` had the highest average popularity among the top genre results, at `59.28`.
- Energy and loudness had a strong positive correlation of `0.76`.
- Instrumentalness had the strongest relationship with popularity by absolute value, but the relationship was weak and negative at `-0.09`.

These results describe the records and choices used in this project. They are not universal conclusions about Spotify tracks. Correlation does not prove causation.

## Analysis Notes

The dataset contains repeated `track_id` values because a track can appear under more than one `track_genre`. The cleaning step removes only completely identical rows and keeps repeated IDs so genre-specific records are not lost.

The most-popular-tracks report removes repeated `track_id` values so the same track does not appear multiple times just because it has several genre labels. Semicolons in artist values, such as `Sam Smith;Kim Petras`, represent multiple artists and are kept as part of the source data.

The numeric validation ranges are practical project checks, not universal absolute limits. Values outside a selected range are inspected as unusual rather than automatically treated as incorrect.

## Data Source and Credits

The project uses the [Spotify Tracks Dataset - Audio Features on Kaggle](https://www.kaggle.com/datasets/saichaitanyareddyai/spotify-tracks-dataset-audio-features).

The CSV is intentionally excluded from GitHub because it is approximately 19 MB. See [data/README.md](data/README.md) for the expected filename, columns, and setup instructions.

## Future Improvements

- Add more focused charts for popularity by genre and audio feature.
- Compare mean and median results more systematically across genres.
- Add tests for cleaning and statistics functions.
- Explore a simple popularity prediction model after completing the descriptive analysis.
- Add a smaller sample dataset so the project can run immediately after cloning.

## License

No project license has been added yet. Check the Kaggle dataset license before redistributing the data or using it outside this analysis project.
