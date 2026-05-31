import pandas as pd


def generate_business_insights(df):

    insights = []

    if df is None:

        return [
            "No segmented data available."
        ]


    if "purchase_amount" in df.columns:

        revenue = (

            df

            .groupby(
                "Segment Name"
            )[
                "purchase_amount"
            ]

            .mean()

        )

        top = revenue.idxmax()

        insights.append(

            f"Highest spending customers belong to {top} segment."

        )


    if "frequency" in df.columns:

        loyal = (

            df

            .groupby(
                "Segment Name"
            )[
                "frequency"
            ]

            .mean()

        )

        top = loyal.idxmax()

        insights.append(

            f"{top} customers purchase most frequently."

        )


    counts = (

        df[
            "Segment Name"
        ]

        .value_counts()

    )


    biggest = counts.idxmax()

    insights.append(

        f"Most customers belong to {biggest} segment."

    )


    actions = {

        "Premium":
        "Launch loyalty rewards.",

        "At Risk":
        "Create retention campaigns.",

        "Growth":
        "Offer upsell opportunities.",

        "Regular":
        "Increase engagement."
    }


    for seg in counts.index:

        if seg in actions:

            insights.append(

                f"{seg}: {actions[seg]}"

            )


    return insights