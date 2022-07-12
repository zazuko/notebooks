import os
from typing import Optional

import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, dcc, html
from dash.dependencies import Input, Output

from client import LindasClient
from utils import plot_streets_heatmap, plot_switzerland

client = LindasClient("https://ld.admin.ch/query")


def get_options():
    data = client.get_communes()
    options = [
        {"label": i, "value": j}
        for i, j in zip(data.municipality, data.municipality_id)
    ]
    id2name = dict(zip(data.municipality_id, data.municipality))
    return options, id2name


communes, id2name = get_options()


app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

controls = html.Div(
    [
        dcc.Dropdown(
            communes,
            id="commune-selector",
            placeholder="Select commune",
        ),
    ]
)

m = plot_switzerland()
m.save("/home/magdalena/zazuko/notebooks/notebooks/swisstopo/assets/basemap.html")

app.layout = dbc.Container(
    [
        html.Div(
            # className="banner",
            children=[
                html.Div(
                    className="position-absolute top-0 start-50 translate-middle-x p-3",
                    children=[
                        html.H2(
                            "Where are most companies registered?",
                            id="title",
                            style={"text-align": "center", "color": "#dddddd"},
                        ),
                    ],
                )
                # html.Div(
                #     className="container scalable",
                #     children=[
                #         html.Div(
                #             id="banner-title",
                #             children=[
                #                 html.H2(
                #                     "Where are most companies registered?",
                #                     id="title",
                #                     style={"text-align": "center"},
                #                 )
                #             ],
                #         ),
                #         html.Div(
                #             id="banner-logo",
                #             children=[
                #                 html.A(
                #                     id="logo",
                #                     children=[
                #                         html.Img(
                #                             src="https://zazuko.com/logo/zazuko-logo.svg"
                #                         )
                #                     ],
                #                     href="https://zazuko.com",
                #                     style={"display": "inline-flex"},
                #                 )
                #             ],
                #         ),
                #     ],
                # )
            ],
            # style={"height": "10vh", "align-items": "center", "display": "flex"},
        ),
        dbc.Row(
            [
                dbc.Col(
                    children=[
                        dbc.Col(
                            controls,
                            md=2,
                            style={
                                "position": "absolute",
                                "top": "1rem",
                                "left": "3rem",
                            },
                        ),
                        dcc.Loading(
                            id="loading",
                            children=[
                                html.Iframe(
                                    src="assets/basemap.html",
                                    id="div-map",
                                    style={
                                        "width": "100%",
                                        "height": "calc(100vh - 6px)",
                                    },
                                ),
                            ],
                            type="circle",
                            style={
                                "width": "100%",
                                "height": "calc(100vh - 6px)",
                                "display": "flex",
                                "align-items": "center",
                            },
                        ),
                    ],
                    md=12,
                    style={"padding": 0, "margin": 0},
                ),
            ],
        ),
    ],
    fluid=True,
    style={"background-color": "#121212"},
)


@app.callback(Output("div-map", "src"), Input("commune-selector", "value"))
def update_map(muni_id: str) -> Optional[str]:
    if muni_id:
        file = "assets/{}.html".format(id2name[muni_id])
        file_full_path = (
            "/home/magdalena/zazuko/notebooks/notebooks/swisstopo/{}".format(file)
        )
        if not os.path.isfile(file_full_path):
            centroid = client.get_commune_centroid(muni_id)
            df = client.get_commune_streets(muni_id)
            map_html = plot_streets_heatmap(centroid, df)
            map_html.save(
                "/home/magdalena/zazuko/notebooks/notebooks/swisstopo/{}".format(file)
            )

        return file


# Healthcheck route that returns a 200
@app.server.route("/healthz")
def healthcheck():
    return "OK"


# Expose the WSGI server to use with gunicorn
server = app.server

if __name__ == "__main__":
    app.run_server(debug=True)
