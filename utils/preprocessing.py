import pandas as pd
from sklearn.preprocessing import StandardScaler


def clean_data(df):

    df = df.copy()

    numeric = df.select_dtypes(
        include=["int64", "float64"]
    ).columns

    categorical = df.select_dtypes(
        include=["object"]
    ).columns


    for col in numeric:
        df[col] = df[col].fillna(
            df[col].median()
        )


    for col in categorical:
        df[col] = df[col].fillna(
            df[col].mode()[0]
        )

    return df


def prepare_features(df):

    numeric = df.select_dtypes(
        include=["int64", "float64"]
    )

    scaler = StandardScaler()

    scaled = scaler.fit_transform(
        numeric
    )

    return scaled, numeric.columns