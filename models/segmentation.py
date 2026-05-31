from sklearn.cluster import KMeans
import pandas as pd


def run_segmentation(
        df,
        features,
        clusters=4
):

    model = KMeans(
        n_clusters=clusters,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(
        features
    )

    result = df.copy()

    result["Segment"] = labels

    names = {
        0: "Premium",
        1: "Regular",
        2: "At Risk",
        3: "Growth"
    }

    result["Segment Name"] = (
        result["Segment"]
        .map(names)
    )

    return result