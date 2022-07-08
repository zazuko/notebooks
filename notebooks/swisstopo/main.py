from client import LindasClient
from utils import plot_streets_heatmap

if __name__ == "__main__":

    client = LindasClient("https://ld.admin.ch/query")
    muni = "<https://ld.admin.ch/municipality/1711>"
    centroid = client.get_commune_centroid(muni)
    df = client.get_commune_streets(muni)
    map = plot_streets_heatmap(centroid, df)
    map.save("plot.html")
