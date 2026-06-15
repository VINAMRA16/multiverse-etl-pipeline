import pandas as pd 

def clean_character_data(raw_data):

    flat_data = []

    for char in raw_data:
        flat_data.append({
            "id": char["id"],
            "name": char["name"],
            "status": char["status"],
            "species": char["species"],
            "origin": char["origin"]["name"]
        })

    df = pd.DataFrame(flat_data)

    # Defensive Sanitization
    df["name"] = df["name"].str.strip().str.title()
    df["status"] = df["status"].str.strip().str.title()
    df["species"] = df["species"].str.strip().str.title()
    df["origin"] = df["origin"].str.strip().str.title()

    return df

