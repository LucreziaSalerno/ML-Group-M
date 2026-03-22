import pandas as pd

league_name_map = {
    # Portugal
    "Betclic 1 Liga": "Liga Portugal",
    "Betclic 2 Liga": "Liga Portugal 2",

    # Germany
    "1. Bundesliga": "Bundesliga",

    # Belgium
    "Jupiler Pro League": "Pro League",
    "Challenger Pro League": "Pro League 2",

    # Turkey
    "1.Lig": "Süper Lig 2",
    "2.Lig Kirmizi": "Süper Lig 3",
    "2.Lig Beyaz": "Süper Lig 3",

}

def data_cleaning(df):
    # Copy the Dataframe
    df = df.copy()

    # Rename columns and normalize columns content
    df.rename(columns={"value_latest": "current_market_value"}, inplace=True)
    df["competition_name"] = df["competition_name"].replace(league_name_map)

    # Fill missing performance stats with 0
    performance_cols = ['goals', 'assists', 'minutes_played', 'matches', 
                        'yellow_cards', 'red_cards']

    for col in performance_cols:
        if col in df.columns:
             df[col] = df[col].fillna(0)

    # Players with 0 minutes are assumed to have 0 stats
    zero_minutes_mask = df["minutes_played"] == 0
    df.loc[zero_minutes_mask, [
    "goals", 
    "assists", 
    "yellow_cards", 
    "red_cards"
    ]] = 0
   
    # Converting variables to right type
    date_cols = ['joined', 'contract_expires','date_of_birth']
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors='coerce')

    df["main_position"] = pd.Categorical(df["main_position"], 
                                         categories=["Goalkeeper", "Defender", "Midfield", "Attack"], 
                                         ordered=False)

    # Remove players with zero market value
    df = df[df['current_market_value'] > 0]

    # We drop columns that are not useful for modeling
    cols_to_drop = [
    'player_slug',
    'player_image_url',
    'place_of_birth',
    'country_of_birth',
    'name_in_home_country',
    'social_media_url',
    'second_club_url',
    'third_club_url',
    'fourth_club_url',
    'player_agent_id',
    'player_agent_name',
    'club_id',
    ]

    df = df.drop(columns = cols_to_drop)

    return df
