import folium
import mapclassify
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import pandas as pd


def classify(df, N=6):
    classifier = mapclassify.NaturalBreaks(y=df.companies, k=N)
    df["bucket"] = df[["companies"]].apply(classifier)
    labels = mapclassify.classifiers._get_mpl_labels(classifier, fmt="{:.0f}")
    labels[0] = labels[0].replace("0,", "1,")

    return df, labels


def plot_streets_heatmap(centroid: list, df: pd.DataFrame) -> folium.Map:
    def style_function(feature, N=6, cmap=plt.get_cmap("inferno")):
        bucket = df["bucket"].get(int(feature["id"][-5:]), None)
        if bucket == 0 and df["companies"].get(int(feature["id"][-5:]), None) == 0:
            bucket = None
        return {
            "fillOpacity": 0.6,
            "weight": 3,
            "opacity": 1,
            "fillColor": "303030"
            if bucket is None
            else mcolors.rgb2hex(cmap((bucket + 1) / N)),
            "color": "303030"
            if bucket is None
            else mcolors.rgb2hex(cmap((bucket + 1) / N)),
        }

    def highlight_function(feature):
        return {
            "fillColor": "#989898",
            "color": "#989898",
            "fillOpacity": 0.8,
        }

    df, labels = classify(df)
    m = folium.Map(location=centroid, zoom_start=13, tiles="CartoDBdark_matter")

    for bucket, label in enumerate(labels):

        feature_group = folium.FeatureGroup(name=label).add_to(m)
        folium.features.GeoJson(
            df[df.bucket == bucket],
            style_function=style_function,
            control=False,
            highlight_function=highlight_function,
            tooltip=folium.features.GeoJsonTooltip(
                fields=["thoroughfare", "companies"],
                aliases=["Street: ", "Registered companies: "],
                style=(
                    "background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"
                ),
            ),
        ).add_to(feature_group)

    folium.LayerControl(name="bla").add_to(m)
    title_html = """<h3 align="center" style="font-size:16px"><b>{}</b></h3>""".format(
        "Where are most companies registered?"
    )
    m.get_root().html.add_child(folium.Element(title_html))

    return m
