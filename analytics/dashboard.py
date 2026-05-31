import streamlit as st


def show_summary(summary):

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Rows",
        summary["Rows"]
    )

    c2.metric(
        "Columns",
        summary["Columns"]
    )

    c3.metric(
        "Missing Values",
        summary["Missing Values"]
    )

    c4.metric(
        "Duplicates",
        summary["Duplicate Rows"]
    )