import pandas as pd

# Load datasets
tmdb = pd.read_csv("TMDB  IMDB Movies Dataset.csv", encoding="utf-8", low_memory=False)
letterboxd = pd.read_csv("letterboxd_movies_dataset.csv", encoding="utf-8", low_memory=False)

# Extract year from TMDB release_date
tmdb["year"] = pd.to_datetime(tmdb["release_date"], errors="coerce").dt.year

# Standardize column names
tmdb.rename(columns={"title": "movie_title"}, inplace=True)
letterboxd.rename(columns={"title": "movie_title"}, inplace=True)

# Merge the two datasets
combined = pd.merge(
    tmdb,
    letterboxd,
    on=["movie_title", "year"],
    how="inner"   # change to "left" if you want ALL TMDB movies even if no match
)

# Save merged dataset
combined.to_csv("combined_movies.csv", index=False)

print("MERGE COMPLETE")
print("Rows after merge:", combined.shape[0])