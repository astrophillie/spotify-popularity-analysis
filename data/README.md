# Data

The project expects this local input file:

```text
data/spotify-tracks-dataset-detailed.csv
```

The current CSV is approximately 19 MB, so it is not committed to GitHub. This keeps the repository smaller and makes it easier to clone. The source used for this project is the [Spotify Tracks Dataset - Audio Features on Kaggle](https://www.kaggle.com/datasets/saichaitanyareddyai/spotify-tracks-dataset-audio-features). Obtain the dataset separately, then place the file at the path above.

The analysis expects columns including:

- `track_id`
- `artists`
- `album_name`
- `track_name`
- `popularity`
- `duration_ms`
- `explicit`
- `danceability`
- `energy`
- `loudness`
- `speechiness`
- `acousticness`
- `instrumentalness`
- `liveness`
- `valence`
- `tempo`
- `track_genre`

The dataset contains repeated track IDs because tracks can appear in multiple genre records. The cleaning code removes exact duplicate rows but does not remove every repeated track ID.

After placing the file, run the project from the `spotify_popularity_analysis` directory:

```powershell
python main.py
```
