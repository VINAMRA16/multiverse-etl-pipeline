import config
from extract import fetch_characters
from transform import clean_character_data
from load import load_to_db

def run_pipeline():

    raw_data = fetch_characters()
    clean_df = clean_character_data(raw_data)
    load_to_db(clean_df)

    print("PIPELINE WORKS PERFECTLY FINE 🦁")


if __name__ == "__main__":
    run_pipeline()