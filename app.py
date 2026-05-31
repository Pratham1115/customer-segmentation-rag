import streamlit as st

from utils.file_handler import (
    load_dataset,
    dataset_summary
)

from analytics.dashboard import (
    show_summary,
    segmentation_dashboard
)

from utils.preprocessing import (
    clean_data,
    prepare_features
)

from models.segmentation import (
    run_segmentation
)


st.set_page_config(
    layout="wide",
    page_title="AI Business Agent"
)


if "df" not in st.session_state:
    st.session_state.df=None


if "segmented" not in st.session_state:
    st.session_state.segmented=None


st.sidebar.title(
    "AI Business Agent"
)

page = st.sidebar.radio(

    "Navigation",

    [

        "Upload",

        "Segmentation",

        "Dashboard"

    ]

)


st.title(
    "📊 Business Insight Platform"
)



if page=="Upload":

    file = st.file_uploader(

        "Upload Dataset",

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
            "Upload Successful"
        )



if st.session_state.df is not None:

    show_summary(

        dataset_summary(

            st.session_state.df

        )

    )



if (
page=="Segmentation"
and
st.session_state.df
is not None
):


    if st.button(

        "Generate Segments"

    ):

        cleaned=clean_data(

            st.session_state.df

        )


        features,_=(

            prepare_features(

                cleaned

            )

        )


        segmented=(

            run_segmentation(

                cleaned,

                features

            )

        )


        st.session_state.segmented=segmented


        st.dataframe(

            segmented

        )



if page=="Dashboard":


    segmentation_dashboard(

        st.session_state.segmented

    )