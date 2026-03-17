"""
Provides a file that stores the feature engineering function
"""
import pandas as pd


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function compacts all the feature engineering process
    so that the models can be reproduced safely through a pickle file.
    """
    