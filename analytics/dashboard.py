import streamlit as st
import plotly.express as px
import pandas as pd


IGNORE_COLUMNS = [
    "customer_id",
    "Segment",
    "Segment Name"
]


def show_summary(summary):

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Rows", summary["Rows"])
    c2.metric("Columns", summary["Columns"])
    c3.metric("Missing", summary["Missing Values"])
    c4.metric("Duplicates", summary["Duplicate Rows"])



def segmentation_dashboard(df):

    if df is None:

        st.info(
            "Generate segmentation first."
        )

        return


    st.subheader(
        "Business Dashboard"
    )


    c1, c2 = st.columns(2)


    chart1 = px.histogram(
        df,
        x="Segment Name"
    )

    c1.plotly_chart(
        chart1,
        use_container_width=True
    )


    if "purchase_amount" in df.columns:

        chart2 = px.box(
            df,
            y="purchase_amount",
            color="Segment Name"
        )

        c2.plotly_chart(
            chart2,
            use_container_width=True
        )


    st.divider()

    st.subheader(
        "Business Statistics"
    )


    numeric = (

        df

        .select_dtypes(
            include="number"
        )

        .columns

        .tolist()

    )


    stats_cols = [

        col

        for col in numeric

        if col not in IGNORE_COLUMNS

    ]


    if len(stats_cols) > 0:

        stats = (

            df

            .groupby(
                "Segment Name"
            )[

                stats_cols

            ]

            .agg(

                [

                    "mean",

                    "max",

                    "min"

                ]

            )

            .round(2)

        )


        st.dataframe(

            stats,

            use_container_width=True

        )


    st.divider()


    st.subheader(
        "AI Business Insights"
    )


    if "purchase_amount" in stats_cols:

        revenue = (

            df

            .groupby(
                "Segment Name"
            )[
                "purchase_amount"
            ]

            .mean()

            .idxmax()

        )


        st.success(

            f"💰 Highest spending customers belong to: {revenue}"

        )


    if "frequency" in stats_cols:

        loyal = (

            df

            .groupby(
                "Segment Name"
            )[
                "frequency"
            ]

            .mean()

            .idxmax()

        )


        st.info(

            f"🔁 Most loyal customers belong to: {loyal}"

        )


    st.caption(
        "Business metrics exclude IDs and text columns."
    )