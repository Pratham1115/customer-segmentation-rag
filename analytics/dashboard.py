import streamlit as st
import plotly.express as px


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


    if "Segment Name" not in df.columns:

        st.warning(
            "Segment data unavailable."
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


    numeric = df.select_dtypes(
        include="number"
    )


    if len(numeric.columns) > 0:

        target = numeric.columns[0]

        chart2 = px.box(
            df,
            y=target,
            color="Segment Name"
        )

        c2.plotly_chart(
            chart2,
            use_container_width=True
        )


    st.subheader(
        "Segment Statistics"
    )

    stats = (

        df

        .groupby(
            "Segment Name"
        )

        .mean(
            numeric_only=True
        )

    )

    st.dataframe(
        stats,
        use_container_width=True
    )