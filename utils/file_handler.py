import pandas as pd
import os


UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def load_dataset(uploaded_file):

    if uploaded_file is None:
        return None

    path = os.path.join(
        UPLOAD_FOLDER,
        uploaded_file.name
    )

    with open(path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(path)

    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(path)

    else:
        raise Exception("Unsupported File")

    return df


def dataset_summary(df):

    return {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": int(df.isnull().sum().sum()),
        "Duplicate Rows": int(df.duplicated().sum())
    }