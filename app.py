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

from rag.rag_engine import (
    build_vector_db,
    search_data
)

from rag.gemini_chat import (
    ask_ai
)


st.set_page_config(
    layout="wide"
)


defaults = {

    "df":None,

    "segmented":None,

    "db":None,

    "chat":[]

}


for k in defaults:

    if k not in st.session_state:

        st.session_state[k]=defaults[k]


page=st.sidebar.radio(

    "Navigation",

    [

        "Upload",

        "Business",

        "AI Assistant"

    ]

)


st.title(
    "📊 AI Business Agent"
)


# ----------------

if page=="Upload":

    file=st.file_uploader(

        "Upload Dataset",

        type=[

            "csv",

            "xlsx"

        ]

    )


    if file:

        df=load_dataset(
            file
        )

        st.session_state.df=df

        st.success(
            "Upload Complete"
        )

        show_summary(
            dataset_summary(df)
        )


# ----------------

elif page=="Business":

    if st.session_state.df is None:

        st.warning(
            "Upload dataset"
        )

    else:

        if st.button(
            "Analyze"
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


            st.session_state.db=(

                build_vector_db(

                    segmented

                )

            )


        if st.session_state.segmented is not None:

            segmentation_dashboard(

                st.session_state.segmented

            )


            st.subheader(
                "Insights"
            )


            for i in (

                generate_business_insights(

                    st.session_state.segmented

                )

            ):

                st.success(i)


# ----------------

elif page=="AI Assistant":


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


        q=st.chat_input(
            "Ask business question"
        )


        if q:


            st.chat_message(
                "user"
            ).write(
                q
            )


            st.session_state.chat.append(

                {

                    "role":"user",

                    "content":q

                }

            )


            context=(

                search_data(

                    st.session_state.db,

                    q

                )

            )


            answer=(

                ask_ai(

                    context,

                    q,

                    st.session_state.chat

                )

            )


            st.chat_message(

                "assistant"

            ).write(

                answer

            )


            st.session_state.chat.append(

                {

                    "role":"assistant",

                    "content":answer

                }

            )