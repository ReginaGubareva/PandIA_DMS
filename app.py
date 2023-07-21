import dash_bootstrap_components as dbc
import plotly.express as px
from dash import html, dcc, dash, Output, Input

from geo_analysis import pt_water_pic, br_zone_consumption_pic

from styles import (SIDEBAR_STYLE,
                    CONTENT_STYLE,
                    NAVLINK_STYLE,
                    CONTENT_STYLE_HOME)

from html_components import (consumer_types_tbl_text,
                             consumer_types_tbl,
                             zone_description_tbl,
                             zone_tbl_text)
from figures import (total_by_consumer_type_fig,
                     dom_ind_fig,
                     prcp_fig,
                     population_fig,
                     covid_fig,
                     yearly_fig)
from test import portugal_map_fig

app = dash.Dash(__name__, external_stylesheets=["https://fonts.googleapis.com/css?family=Inconsolata",
                                                dbc.themes.BOOTSTRAP])
# app.head = [html.Link(rel='stylesheet', href='./static/style.css')]
sidebar = html.Div(
    [
        html.H2("PandIA Dashboards", className="display-4"),
        html.Hr(),
        html.P(
            "Resource consumption statistics for Bragança and Portugal", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact", style=NAVLINK_STYLE),
                dbc.NavLink("Bragança", href="/braganca", active="exact", style=NAVLINK_STYLE),
                dbc.NavLink("Portugal", href="/portugal", active="exact", style=NAVLINK_STYLE),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

home_page_content = html.Div(id="home_page_content", style=CONTENT_STYLE_HOME, children=[
    html.Div(className='row1', children=[
        dbc.Col([
            consumer_types_tbl_text,
            html.Br(),
            consumer_types_tbl
        ]),
        dbc.Col([
            html.Br(),
            html.Br(),
            zone_tbl_text,
            html.Br(),
            zone_description_tbl,
            html.Br()
        ]),
        dbc.Col([
            html.Br(),
            total_by_consumer_type_fig,
            yearly_fig,
            dom_ind_fig,
            prcp_fig,
            html.Br(),
            covid_fig,
            html.Br(),
            population_fig,
            html.Br()
        ]),
    ]),
])

portugal_content = html.Div(id="home_page_content", style=CONTENT_STYLE_HOME, children=[
    html.Div(className='row1', children=[
        dbc.Col([
            html.Br(),
            html.H4("Portugal map"),
            dcc.Graph(
                id='pt_map',
                figure=pt_water_pic
            )
        ])
    ])
])

app.layout = html.Div([dcc.Location(id="url"), sidebar, home_page_content])


@app.callback(Output("home_page_content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return home_page_content
    elif pathname == "/braganca":
        return html.P("This is the content of page 1. Yay!")
    elif pathname == "/portugal":
        return portugal_content
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
