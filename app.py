import streamlit as st

from utils.file_handler import (
    load_dataset,
    dataset_summary
)

from utils.preprocessing import (
    clean_data,
    prepare_features
)

from models.segmentation import (
    run_segmentation
)

from analytics.dashboard import (
    show_summary,
    segmentation_dashboard
)

from analytics.insights import (
    generate_business_insights
)

from analytics.action_center import (
    show_actions
)

from rag.rag_engine import (
    build_vector_db,
    search_data
)

from rag.gemini_chat import (
    ask_ai
)


st.set_page_config(
    page_title="AI Business Agent",
    layout="wide"
)


defaults = {

    "df": None,

    "segmented": None,

    "db": None,

    "chat": []

}


for k in defaults:

    if k not in st.session_state:

        st.session_state[k] = defaults[k]


page = st.sidebar.radio(

    "Navigation",

    [

        "Upload Data",

        "Business Intelligence",

        "AI Assistant"

    ]

)


st.title(
    "📊 AI Customer Segmentation & Business Insights"
)


# -----------------
# UPLOAD
# -----------------

if page == "Upload Data":

    file = st.file_uploader(

        "Upload CSV/XLSX",

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



# -----------------
# BUSINESS
# -----------------

elif page == "Business Intelligence":

    if st.session_state.df is None:

        st.info(
            "Upload dataset first."
        )


    else:

        if st.button(
            "Analyze Business"
        ):

            cleaned = (

                clean_data(

                    st.session_state.df

                )

            )


            features, _ = (

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


            st.session_state.db = (

                build_vector_db(

                    segmented

                )

            )


        if st.session_state.segmented is not None:

            st.success(
                "Analysis Completed"
            )


            segmentation_dashboard(

                st.session_state.segmented

            )


            st.divider()


            st.subheader(
                "AI Business Insights"
            )


            insights = (

                generate_business_insights(

                    st.session_state.segmented

                )

            )


            for i in insights:

                st.info(i)


            st.divider()


            show_actions(

                st.session_state.segmented

            )


# -----------------
# AI CHAT
# -----------------

elif page == "AI Assistant":

    if st.session_state.db is None:

        st.info(
            "Analyze business first."
        )


    else:


        for msg in st.session_state.chat:

            st.chat_message(

                msg["role"]

            ).write(

                msg["content"]

            )


        question = st.chat_input(

            "Ask business question"

        )


        if question:


            st.chat_message(

                "user"

            ).write(

                question

            )


            st.session_state.chat.append({

                "role": "user",

                "content": question

            })


            context = (

                search_data(

                    st.session_state.db,

                    question

                )

            )


            answer = (

                ask_ai(

                    context,

                    question,

                    st.session_state.chat

                )

            )


            st.chat_message(

                "assistant"

            ).write(

                answer

            )


            st.session_state.chat.append({

                "role": "assistant",

                "content": answer

            })