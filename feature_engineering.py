"""
Provides a file that stores the feature engineering function
"""
import pandas as pd
import numpy as np

position_age_bins = {
    "Goalkeeper": [0, 23, 32, np.inf],
    "Defender":   [0, 22, 30, np.inf],
    "Midfield":   [0, 23, 29, np.inf],
    "Attack":     [0, 22, 28, np.inf],
}

def assign_career_phase(row):
    """
    Assigns players their corresponding
    career phase, based on position.
    """
    position = row["main_position"]
    age = row["age"]
    
    if pd.isna(position) or pd.isna(age):
        return None
    
    bins = position_age_bins.get(position)
    if bins is None:
        return None
    
    if age <= bins[1]:
        return "Youth"
    elif age <= bins[2]:
        return "Prime"
    else:
        return "Veteran"
    
league_quality_map = {
    # Tier 5 - Elite
    "Premier League": 5,
    "Serie A": 5,
    "LaLiga": 5,
    "Bundesliga": 5,
    "Ligue 1": 5,
    
    # Tier 4 - Very Strong
    "Pro League": 4,
    "Liga Portugal": 4,
    "Championship": 4,
    "Eredivisie": 4,
    "Scottish Premiership": 4,
    "Jupiler Pro League": 4,
    "Süper Lig": 4,
    "PKO BP Ekstraklasa": 4,
    "Eliteserien": 4,
    "Allsvenskan": 4,
    "Superliga": 4,
    "K League 1": 4,
    "Major League Soccer": 4,
    "Campeonato Brasileiro Série A": 4,
    "Chinese Super League": 4,
    "Qatar Stars League": 4,
    "Super Lig": 4,
    "Super League 1": 4,
    "Première Liga": 4,

    # Tier 3 - Strong (second divisions + strong regional)
    "Süper Lig 2": 3,
    "Pro League 2": 3,
    "2. Bundesliga": 3,
    "LaLiga2": 3,
    "Serie B": 3,
    "Ligue 2": 3,
    "Liga Portugal 2": 3,
    "League One": 3,
    "Scottish Championship": 3,
    "Keuken Kampioen Divisie": 3,
    "Superettan": 3,
    "OBOS-ligaen": 3,
    "1.Lig": 3,
    "Chance Liga": 3,
    "Niké Liga": 3,
    "Nemzeti Bajnokság": 3,
    "J1 League": 3,
    "J2 League": 3,
    "Liga MX Apertura": 3,
    "MLS Next Pro": 3,
    "A-League Men": 3,
    "Campeonato Brasileiro Série B": 3,
    "Primera Nacional": 3,
    "Torneo Clausura": 3,
    "SuperSport HNL": 3,
    "Prva Nogometna Liga": 3,
    "Challenger Pro League": 3,
    "Super League": 3,
    "Betclic 1 Liga": 3,
    "Persha Liga": 3,
    "Premier Liga": 3,
    "Challenge League": 3,
    "2. Liga": 3,
    "1.Division": 3,

    # Tier 2 - Average (third divisions + weaker national leagues)
    "Süper Lig 3": 2,
    "3. Liga": 2,
    "League Two": 2,
    "Scottish League One": 2,
    "Serie C - Girone A": 2,
    "Serie C - Girone B": 2,
    "Serie C - Girone C": 2,
    "Championnat National": 2,
    "Championnat National 2 - Groupe A": 2,
    "Championnat National 2 - Groupe B": 2,
    "Championnat National 2 - Groupe C": 2,
    "Primera Federación - Grupo I": 2,
    "Primera Federación - Grupo II": 2,
    "Regionalliga Bayern": 2,
    "Regionalliga West": 2,
    "Regionalliga Südwest": 2,
    "Regionalliga Nord": 2,
    "Regionalliga Northeast": 2,
    "USL Championship": 2,
    "Liga de Expansión MX Clausura": 2,
    "China League One": 2,
    "J3 League": 2,
    "Nemzeti Bajnokság II.": 2,
    "Super League 2": 2,
    "Betclic 2 Liga": 2,
    "2.Lig Kirmizi": 2,
    "2.Lig Beyaz": 2,
    "Chance Narodni Liga": 2,
    "MONACObet liga": 2,
    "Promotion League": 2,
    "National League": 2,
    "K League 2": 2,
    "Qatari Second Division": 2,
    "USL League One": 2,
    "1ste Nationale VV": 2,
    "1ste Nationale ACFF": 2,
    "2de Nationale VV A": 2,
    "2de Nationale VV B": 2,
    "Ettan Norra": 2,
    "2.Division": 2,

    # Tier 1 - Weak (fourth divisions and below, youth, amateur)
    "Serie D - Girone A": 1,
    "Serie D - Girone B": 1,
    "Serie D - Girone C": 1,
    "Serie D - Girone D": 1,
    "Serie D - Girone E": 1,
    "Serie D - Girone F": 1,
    "Serie D - Girone G": 1,
    "Serie D - Girone H": 1,
    "Serie D - Girone I": 1,
    "Championnat National 3 - Groupe A": 1,
    "Championnat National 3 - Groupe B": 1,
    "Championnat National 3 - Groupe C": 1,
    "Championnat National 3 - Groupe E": 1,
    "Championnat National 3 - Groupe F": 1,
    "Championnat National 3 - Groupe G": 1,
    "Championnat National 3 - Groupe H": 1,
    "Segunda Federación - Grupo I": 1,
    "Segunda Federación - Grupo II": 1,
    "Segunda Federación - Grupo III": 1,
    "Segunda Federación - Grupo IV": 1,
    "Segunda Federación - Grupo V": 1,
    "Primavera 1": 1,
    "Primavera 2 - A": 1,
    "Primavera 2 - B": 1,
    "Premier League 2": 1,
    "Liga Revelação U23": 1,
    "U21 Division 1 Fall": 1,
    "U21 Division 2 Fall": 1,
    "1. Liga Classic group 2": 1,
    "3.Lig Grup 1": 1,
    "3.Lig Grup 2": 1,
    "3.Lig Grup 3": 1,
    "3.Lig Grup 4": 1,
    "Liga 3": 1,
    "National League South": 1,
    "Federal A - Fase Reválida": 1,
    "Federal A - Fase Campeonato": 1,
    "Campeonato de Portugal - Série A": 1,
    "Campeonato de Portugal - Série B": 1,
    "Campeonato Paulista": 1,
}

def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function compacts all the feature engineering process
    so that the models can be reproduced safely through a pickle file.
    """
    df = df.copy()

    # ---Age-related features---
    today = pd.Timestamp.today()

    # Age Feature
    df['age'] = (
    today.year - df['date_of_birth'].dt.year
    - (
        (today.month < df['date_of_birth'].dt.month) |
        (
            (today.month == df['date_of_birth'].dt.month) &
            (today.day < df['date_of_birth'].dt.day)
        )
    )
    ).astype('Int64')

    # Define critical columns
    critical_columns = ['current_market_value']
    if 'age' in df.columns:
        critical_columns.append('age')
    if 'position' in df.columns:
        critical_columns.append('position')

    # Remove rows with missing critical data
    df = df.dropna(subset=critical_columns)

    # Age squared
    df["age_squared"] = df["age"]**2

    # Career Phase (Prime, Youth, Veteran)
    df["career_phase"] = df.apply(assign_career_phase, axis=1)
    df["career_phase"] = pd.Categorical(df["career_phase"],
                                        categories=["Veteran", "Youth", "Prime"],
                                        ordered=False)
    
    # Contract features
    df['days_since_joined'] = (today - df['joined']).dt.days
    df['days_until_contract_expires'] = (df['contract_expires'] - today).dt.days
    df["free_agent"] = df["days_until_contract_expires"] <= 0

    # Adjustments to be in line with the assumptions made in the notebook
    ambiguous= (
    df["competition_name"].isnull() & 
    df["contract_expires"].isnull() & 
    (df["free_agent"] == False)
    )

    df.loc[ambiguous, "free_agent"] = True
    df.loc[ambiguous, "days_until_contract_expires"] = 0

    # ---League Quality---
    df["league_quality"] = df["competition_name"].map(league_quality_map).fillna(1)
    df.loc[df["free_agent"], "league_quality"] = 0

    # ---Market Value Features---
    # Value Percentage Change
    df['value_change_pct'] = (
    (df['current_market_value'] - df['value_first']) /
    df['value_first'] * 100
    ).round(2)

    # Dropping value_first which is no longer necessary
    df.drop(columns="value_first",inplace=True)

    # Relative Market Value
    club_totals = df.groupby("current_club_name")["current_market_value"].transform("sum")
    df["relative_market_value"] = df["current_market_value"] / club_totals
    df.loc[df["free_agent"], "relative_market_value"] = 0

    # ---Stats Features---
    # Goals per 90
    df['goals_per_90'] = (df['goals'] / df['minutes_played'] * 90).round(2)

    # Assists per 90
    df['assists_per_90'] = (df['assists'] / df['minutes_played'] * 90).round(2)

    # G/A (Goal Contributions)
    df['goal_contributions'] = df['goals'] + df['assists']

    # G/A (Goal Contributions) per 90
    df["G/A_per_90"] = df["goals_per_90"] + df["assists_per_90"]

    # Cards per 90
    df["cards_per_90"] = (df["yellow_cards"] + 2 * df["red_cards"]) / (df["minutes_played"] * 90)

    # Net Performance per 90
    df["net_per_90"] = df["G/A_per_90"] - df["cards_per_90"]

    # Net Performance per 90 Normalized
    df["net_per_90_normalized"] = df.groupby("main_position")["net_per_90"].transform(
        lambda x: (x - x.mean()) / x.std())
    
    # Health-related Features
    # Proneness Score
    df['injury_proneness'] = (df['total_injuries'] / 3).round(2)

    # ---Interaction Terms---
    # G/A Normalized X League Quality
    df["goal_contributions_normalized"] = df.groupby("main_position")["goal_contributions"].transform(
    lambda x: (x - x.mean()) / x.std())
    df["G/A_normalized_X_league_quality"] = df["goal_contributions_normalized"] * df["league_quality"]

    # Age X Position
    df["age_X_position"] = (
    df["career_phase"].astype(object) + "_" + df["main_position"].astype(object)
    )
    df["age_X_position"] = pd.Categorical(df["age_X_position"])
    
    return df
