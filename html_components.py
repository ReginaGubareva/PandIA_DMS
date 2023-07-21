from dash import html, dash_table, dcc
import dash_bootstrap_components as dbc

import base_analysis
from styles import (
    header, table, cell, stripped_rows, table_row_highlight, table_colors
)

cons_tipo_description = base_analysis.br_water_consumer_type_description()
zone_description = base_analysis.br_water_zone_description()

consumer_types_tbl_text = html.P("Water consumption statistics from 2013 to 2020 by consumer type."
                                 "There are 19 different types of the consumers depends on the activity."
                                 "The biggest consumption is for Domestic type in Braganca region.")
zone_tbl_text = html.P("The water consumption statistics by Bragança districts. There are 66 districts"
                       "with different territory size and population amount."
                       )


def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def cell_style(value, min_value, max_value):
    style = {}
    if is_numeric(value):
        relative_value = (value - min_value) / (max_value - min_value)
        if relative_value <= 0.25:
            style = {
                'fontFamily': 'Open Sans',
                'textAlign': 'center',
                'height': '30px',
                'width': '20px',
                'padding': '2px 12px',
                'whiteSpace': 'inherit',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
                'backgroundColor': table_colors[0]['background'],
                'color': table_colors[0]['text']
            }
        elif relative_value <= 0.5:
            style = {
                'fontFamily': 'Open Sans',
                'textAlign': 'center',
                'height': '30px',
                'width': '20px',
                'padding': '2px 12px',
                'whiteSpace': 'inherit',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
                'backgroundColor': table_colors[1]['background'],
                'color': table_colors[1]['text']
            }
        elif relative_value <= 0.75:
            style = {
                'fontFamily': 'Open Sans',
                'textAlign': 'center',
                'height': '30px',
                'width': '20px',
                'padding': '2px 12px',
                'whiteSpace': 'inherit',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
                'backgroundColor': table_colors[2]['background'],
                'color': table_colors[2]['text']
            }
        elif relative_value <= 1:
            style = {
                'fontFamily': 'Open Sans',
                'textAlign': 'center',
                'height': '30px',
                'width': '20px',
                'padding': '2px 12px',
                'whiteSpace': 'inherit',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
                'backgroundColor': table_colors[3]['background'],
                'color': table_colors[3]['text']
            }
    return style


def generate_table(dataframe, max_rows=100):
    max_value = dataframe.max(numeric_only=True).max()
    min_value = dataframe.min(numeric_only=True).max()
    rows = []
    for i in range(min(len(dataframe), max_rows)):
        row = []
        for col in dataframe.columns:
            value = dataframe.iloc[i][col]
            style = cell_style(value, min_value, max_value)
            row.append(html.Td(value, style=style))
        rows.append(html.Tr(row))

    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        rows)


zone_description_tbl = generate_table(zone_description)
consumer_types_tbl = generate_table(cons_tipo_description)

# consumer_types_tbl = dash_table.DataTable(cons_tipo_description.to_dict('records'),
#                                           [{"name": i, "id": i} for i in cons_tipo_description.columns],
#                                           style_table=table,
#                                           style_cell=cell,
#                                           style_header=header,
#                                           # style_data_conditional=[stripped_rows, table_row_highlight]
#                                           )
