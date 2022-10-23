import base_analysis
import plotly.express as px
import plotly.graph_objects as go

from logging.config import dictConfig
from dash import html, dcc, dash, dash_table
from flask import Flask

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

# app = Flask(__name__)
app = dash.Dash(__name__)

# app.add_url_rule('/br/water/consumer_type_description', view_func=base_analysis.br_water_consumer_type_description)
# app.add_url_rule('/br/water/zonas_description', view_func=base_analysis.br_water_zone_description)
# app.add_url_rule('/br/water/total', view_func=base_analysis.br_water_total_consumption)
# app.add_url_rule('/br/water/total_by_consumer_type',
#                  view_func=base_analysis.br_water_total_consumption_by_consumer_type)
# app.add_url_rule('/br/water/monthly_consumption_domestic_industrial',
#                  view_func=base_analysis.br_domestico_industrial_monthly_consumption)

# TODO: add commemoration analysis

cons_tipo_description = base_analysis.br_water_consumer_type_description()
zone_description = base_analysis.br_water_zone_description()
yearly = base_analysis.br_water_total_consumption()
total_by_consumer_type = base_analysis.br_water_total_consumption_by_consumer_type()
total_by_consumer_type_fig = px.area(total_by_consumer_type,
                                     x=total_by_consumer_type['Year'],
                                     y=total_by_consumer_type['Consumption'],
                                     color=total_by_consumer_type['Consumer_type'])

domestico, industrial = base_analysis.br_domestico_industrial_monthly_consumption()

dom_ind_fig = go.Figure()
dom_ind_fig.add_trace(go.Scatter(
    x=domestico.Date,
    y=domestico.Consumption,
    hovertext=domestico.Consumption,
    hoverinfo="text",
    marker=dict(
        color="blue"
    ),
    showlegend=False
))
dom_ind_fig.add_trace(go.Scatter(
    x=industrial.Date,
    y=industrial.Consumption,
    hovertext=industrial.Consumption,
    hoverinfo="text",
    marker=dict(
        color="green"
    ),
    showlegend=False
))


app.layout = html.Div(
    children=[
        html.H1(children="Consumer Type Analytics",
                style={"fontSize": "48px", "color": "red"}),
        html.P(
            children="Analyze the behavior of the consumers"
                     " between 2013 and 2020",
        ),
        dash_table.DataTable(cons_tipo_description.to_dict('records'),
                             [{"name": i, "id": i} for i in cons_tipo_description.columns]
                             ),
        html.Br(),
        html.Br(),
        html.P(
            children="The consumption by Braganca districts.",
        ),

        dash_table.DataTable(zone_description.to_dict('records'),
                             [{"name": i, "id": i} for i in zone_description.columns]
                             ),
        html.Br(),
        html.Br(),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": yearly["Year"],
                        "y": yearly["Consumption"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Total consumption by years"},
            },
        ),
        dcc.Graph(
            id='example-graph',
            figure=total_by_consumer_type_fig
        ),
        dcc.Graph(
            id='dom_ind_fig',
            figure=dom_ind_fig
        ),

    ])


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
