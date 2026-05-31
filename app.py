import streamlit as st

from utils.file_handler import (
    load_dataset,
    dataset_summary
)

from analytics.dashboard import (
    show_summary
)

from utils.preprocessing import (
    clean_data,
    prepare_features
)

from models.segmentation import (
    run_segmentation
)


st.set_page_config(
    layout="wide"
)

if "df" not in st.session_state:
    st.session_state.df=None


st.sidebar.title(
    "AI Business Agent"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Upload",
        "Segmentation"
    ]
)

st.title(
    "📊 Customer Segmentation"
)


if page=="Upload":

    file = st.file_uploader(
        "Upload",
        type=[
            "csv",
            "xlsx"
        ]
    )

    if file:

        df = load_dataset(
            file
        )

        st.session_state.df=df

        st.success(
            "Uploaded"
        )



if (
    st.session_state.df
    is not None
):

    df = st.session_state.df

    st.subheader(
        "Dataset"
    )

    show_summary(
        dataset_summary(df)
    )

    st.dataframe(df)



if (
page=="Segmentation"
and
st.session_state.df
is not None
):

    st.subheader(
        "Run Segmentation"
    )

    if st.button(
        "Start Analysis"
    ):

        cleaned = clean_data(
            st.session_state.df
        )

        features,_ = (
            prepare_features(
                cleaned
            )
        )

        segmented = (
            run_segmentation(
                cleaned,
                features
            )
        )

        st.success(
            "Completed"
        )

        st.dataframe(
            segmented
        )