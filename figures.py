# TODO: add commemoration analysis

import plotly.express as px
import plotly.graph_objects as go
from dash import dcc

import base_analysis

"""
Total consumption by different consumer types
"""
total_by_consumer_type = base_analysis.br_water_total_consumption_by_consumer_type()
total_by_consumer_type = px.area(total_by_consumer_type,
                                 x=total_by_consumer_type['Year'],
                                 y=total_by_consumer_type['Consumption'],
                                 color=total_by_consumer_type['Consumer_type'])
total_by_consumer_type_fig = dcc.Graph(
    id='total_by_consumer_type',
    figure=total_by_consumer_type
)

"""
Total consumption by year
"""
yearly = base_analysis.br_water_total_consumption()

yearly_fig = go.Figure()
yearly_fig.add_trace(go.Scatter(
    x=yearly.Year,
    y=yearly.Consumption,
    hovertext=yearly.Consumption,
    hoverinfo="text",
    name="Total consumption by year",
    marker=dict(
        color="blue"
    ),
    showlegend=True
))

yearly_fig = dcc.Graph(
    id='yearly',
    figure=yearly_fig
)

"""
Monthly consumption for domestic and industrial types
"""
domestico, industrial = base_analysis.br_domestico_industrial_monthly_consumption()

dom_ind_fig = go.Figure()
dom_ind_fig.add_trace(go.Scatter(
    x=domestico.Date,
    y=domestico.Consumption,
    hovertext=domestico.Consumption,
    hoverinfo="text",
    name="Domestico",
    marker=dict(
        color="blue"
    ),
    showlegend=True
))

dom_ind_fig.add_trace(go.Scatter(
    x=industrial.Date,
    y=industrial.Consumption,
    hovertext=industrial.Consumption,
    hoverinfo="text",
    name="Industrial",
    marker=dict(
        color="green"
    ),
    showlegend=True
))
dom_ind_fig.update_layout(title="Domestic and Industrial consumption by month")
dom_ind_fig = dcc.Graph(
    id='dom_ind_fig',
    figure=dom_ind_fig
)

'''
Precipitation level
'''
precipitation = base_analysis.br_precipitation_monthly()

prcp_fig = go.Figure()
prcp_fig.add_trace(go.Scatter(
    x=domestico.Date,
    y=domestico.Consumption,
    hovertext=domestico.Consumption,
    hoverinfo="text",
    name="Domestico",
    marker=dict(
        color="blue"
    ),
    showlegend=True
))
prcp_fig.add_trace(go.Scatter(
    x=industrial.Date,
    y=industrial.Consumption,
    hovertext=industrial.Consumption,
    hoverinfo="text",
    name="Industrial",
    marker=dict(
        color="green"
    ),
    showlegend=True
))
prcp_fig.add_trace(go.Scatter(
    x=precipitation.Date,
    y=precipitation.QPRtot,
    hovertext=precipitation.QPRtot,
    hoverinfo="text",
    name="Precipitation",
    marker=dict(
        color="red"
    ),
    showlegend=True
))
prcp_fig.update_layout(title="Precipitation level with consumption")
prcp_fig = dcc.Graph(
    id='prcp',
    figure=prcp_fig
)

'''
Population statistics
'''
population = base_analysis.br_population()
population_fig = go.Figure()
population_fig.add_trace(go.Scatter(
    x=population.Year,
    y=population["Net increase"],
    hovertext=population["Net increase"],
    hoverinfo="text",
    name="Net increase",
    marker=dict(
        color="blue"
    ),
    showlegend=True
))
population_fig.add_trace(go.Scatter(
    x=population.Year,
    y=population["Natural increase"],
    hovertext=population["Natural increase"],
    hoverinfo="text",
    name="Natural increase",
    marker=dict(
        color="green"
    ),
    showlegend=True
))
population_fig.add_trace(go.Scatter(
    x=population.Year,
    y=population["Net migration"],
    hovertext=population["Net migration"],
    hoverinfo="text",
    name="Net migration",
    marker=dict(
        color="red"
    ),
    showlegend=True
))
population_fig.update_layout(title="Population statistic")
population_fig = dcc.Graph(
    id='population',
    figure=population_fig
)

# population_fig.add_trace(go.Scatter(
#     x=population.Year,
#     y=population["Consumption"],
#     hovertext=population["Consumption"],
#     hoverinfo="text",
#     marker=dict(
#         color="purple"
#     ),
#     showlegend=False
# ))


"""
Covid statistics
"""
consumption_2020, covid = base_analysis.br_covid()

covid_fig = go.Figure()
covid_fig.add_trace(go.Scatter(
    x=consumption_2020.Month,
    y=consumption_2020["Consumption"],
    hovertext=consumption_2020["Consumption"],
    hoverinfo="text",
    name="Consumption",
    marker=dict(
        color="purple"
    ),
    showlegend=True))

covid_fig.add_trace(go.Scatter(
    x=covid.Date,
    y=covid["Cases"],
    hovertext=covid["Cases"],
    hoverinfo="text",
    name="Covid cases",
    marker=dict(
        color="orange"
    ),
    showlegend=True
))

covid_fig = dcc.Graph(
    id='covid',
    figure=covid_fig
)

# geojson = gpd.GeoSeries(pt_polygons["geometry"]).__geo_interface__
# print(geojson)