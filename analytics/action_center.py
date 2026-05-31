import streamlit as st


def show_actions(df):

    if df is None:

        st.info(
            "Analyze business first."
        )

        return


    st.subheader(
        "🎯 Business Action Center"
    )


    recommendations = []


    if "Segment Name" in df.columns:

        segments = (

            df[
                "Segment Name"
            ]

            .value_counts()

        )


        for segment in segments.index:


            if segment == "Premium":

                recommendations.append({

                    "priority": "🟢 High",

                    "title": "Grow Premium Customers",

                    "action":
                    "Launch loyalty programs and premium offers."

                })


            elif segment == "At Risk":

                recommendations.append({

                    "priority": "🔴 Critical",

                    "title": "Reduce Customer Loss",

                    "action":
                    "Run retention campaigns and discounts."

                })


            elif segment == "Growth":

                recommendations.append({

                    "priority": "🟡 Medium",

                    "title": "Increase Revenue",

                    "action":
                    "Offer upsell bundles and recommendations."

                })


            elif segment == "Regular":

                recommendations.append({

                    "priority": "🟢 Medium",

                    "title": "Improve Engagement",

                    "action":
                    "Send personalized campaigns."

                })


    for rec in recommendations:

        st.markdown(
            f"""
### {rec['priority']}

**{rec['title']}**

{rec['action']}
"""
        )


    st.divider()


    st.success(

        f"""

Business Analysis Complete

Detected {len(recommendations)} business opportunities.

Focus on retaining customers before acquiring new ones.

"""

    )