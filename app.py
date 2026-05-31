import streamlit as st

from utils.file_handler import (
    load_dataset,
    dataset_summary
)

from analytics.dashboard import (
    show_summary,
    segmentation_dashboard
)

from analytics.insights import (
    generate_business_insights
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

        "Dashboard",

        "Insights"

    ]

)


st.title(
    "📊 AI Business Insight Platform"
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

        st.session_state.df = (
            load_dataset(
                file
            )
        )

        st.success(
            "Dataset Uploaded"
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

st.session_state.df is not None

):

    if st.button(

        "Generate Segments"

    ):

        cleaned = (

            clean_data(

                st.session_state.df

            )

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


        st.success(

            "Segmentation Complete"

        )



if page=="Dashboard":

    segmentation_dashboard(

        st.session_state.segmented

    )



if page=="Insights":


    if st.session_state.segmented is None:

        st.info(

            "Generate segmentation first."

        )


    else:

        st.subheader(

            "AI Generated Insights"

        )


        insights=(

            generate_business_insights(

                st.session_state.segmented

            )

        )


        for i in insights:

            st.success(i)