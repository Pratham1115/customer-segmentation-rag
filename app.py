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
    page_title="AI Business Agent",
    layout="wide"
)


if "df" not in st.session_state:
    st.session_state.df = None


if "segmented" not in st.session_state:
    st.session_state.segmented = None


st.sidebar.title(
    "📊 AI Business Agent"
)


page = st.sidebar.radio(

    "Navigation",

    [

        "Upload Data",

        "Business Intelligence",

        "AI Assistant"

    ]

)


st.title(
    "AI Customer Segmentation & Business Insights"
)


# ------------------
# UPLOAD
# ------------------

if page == "Upload Data":

    file = st.file_uploader(
        "Upload CSV / XLSX",
        type=[
            "csv",
            "xlsx"
        ]
    )

    if file:

        df = load_dataset(
            file
        )

        st.session_state.df = df

        st.success(
            "Dataset uploaded."
        )

        show_summary(
            dataset_summary(df)
        )

        st.dataframe(
            df,
            use_container_width=True
        )


# ------------------
# BUSINESS INTELLIGENCE
# ------------------

elif page == "Business Intelligence":

    if st.session_state.df is None:

        st.info(
            "Upload dataset first."
        )

    else:

        if st.button(
            "Analyze Business"
        ):

            with st.spinner(
                "Analyzing..."
            ):

                cleaned = clean_data(
                    st.session_state.df
                )


                features,_=(

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


                st.session_state.segmented = segmented


        if st.session_state.segmented is not None:

            st.success(
                "Analysis Completed"
            )

            segmentation_dashboard(
                st.session_state.segmented
            )

            st.divider()

            st.subheader(
                "AI Insights"
            )

            insights = (

                generate_business_insights(

                    st.session_state.segmented

                )

            )

            for i in insights:

                st.info(i)


# ------------------
# AI ASSISTANT
# ------------------

elif page == "AI Assistant":

    st.info(
        "Coming next → RAG Chat"
    )