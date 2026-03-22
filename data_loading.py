import pandas as pd

PLAYER_ID = 'player_id'

def extract_start_year(season):
    if '/' in season:
        year = season.split('/')[0]
        year = int(year)
        
        if year <= 30:   
            return 2000 + year
        else:            
            return 1900 + year
    
    elif season.isdigit():
        return int(season)
    
    else:
        return None
    
def data_loading():
    # Copy the Dataframes
    df = pd.read_csv("../data/player_profiles.csv", low_memory=False)
    df_perf = pd.read_csv("../data/player_performances.zip", compression='zip')
    df_market = pd.read_csv("../data/player_market_value.csv")
    df_injuries = pd.read_csv("../data/player_injuries.csv")
    df_teams = pd.read_csv("../data/team_details.csv")
    
    # Applying the filter of 2010 onwards
    # Create a new local dataframe
    df_perf['season_start_year'] = df_perf['season_name'].apply(extract_start_year)
    df_perf = df_perf[df_perf['season_start_year'] >= 2010]

    # GET LATEST MARKET VALUE
    df_market['date'] = pd.to_datetime(df_market['date_unix'])
    df_market.sort_values('date',inplace=True)

    # Get latest valuation per player
    latest_values = (df_market.groupby(PLAYER_ID).tail(1))

    # Get first valuation per player
    first_values = (df_market.groupby(PLAYER_ID).head(1))

    values = latest_values.merge(
    first_values[[PLAYER_ID, 'value']],
    on=PLAYER_ID,
    suffixes=('_latest', '_first'),
    how='left'
    )   
    
    # Aggregate the Performances Dataframe
    performance_agg = df_perf.groupby(PLAYER_ID).agg({
    'nb_on_pitch': 'sum',
    'goals': 'sum',
    'assists': 'sum',
    'minutes_played': 'sum',
    'yellow_cards': 'sum',
    'direct_red_cards': 'sum',
    }).reset_index()
    
    # We rename columns for clarity
    performance_agg.rename(columns={
    'nb_on_pitch': 'matches',
    'direct_red_cards': 'red_cards'
    },inplace=True)

    # Aggregate the Injuries Dataframe
    injury_agg = df_injuries.groupby(PLAYER_ID).agg({
    'days_missed': 'sum',
    'injury_reason': 'count'
    }).reset_index()

    injury_agg.rename(columns={
    'days_missed': 'total_days_injured',
    'injury_reason': 'total_injuries'
    },inplace=True)

    # Join performance stats
    df = df.merge(performance_agg, on=PLAYER_ID, how='left')

    # Join market values (INNER JOIN - only keep players with valuations)
    df = df.merge(
    values[[PLAYER_ID, 'value_first','value_latest']], 
    on=PLAYER_ID, 
    how='inner')

    # Join injury data
    df = df.merge(injury_agg, on=PLAYER_ID, how='left')


    # Join team details
    df = df.merge(
    df_teams[['club_id', 'competition_name', 'club_division']],
    left_on='current_club_id',
    right_on='club_id',
    how='left'
    )
    return df