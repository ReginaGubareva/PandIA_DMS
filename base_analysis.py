import calendar
import logging.config

import pandas as pd
from dash import html

from logging_conf import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

df = pd.read_csv("data/br/br_water_main.csv")


def br_water_consumer_type_description():
    """
    It should be a table with the base description.
    """
    cons_tipo_description = pd.DataFrame({'Consumer_type': [],
                                          'Count': [],
                                          'Max_consumption': [],
                                          'Min_consumption': [],
                                          'Avg_consumption': [],
                                          'Std_consumption': []})
    columns = list(cons_tipo_description)
    data = []

    for i in df['Consumer_type'].unique():
        consumer_i = df[df['Consumer_type'] == i]
        N = len(consumer_i)
        Max = consumer_i['Consumption'].max()
        Min = consumer_i['Consumption'].min()
        Avg = consumer_i['Consumption'].mean()
        Std = consumer_i['Consumption'].std()
        values = [i, N, Max, Min, Avg, Std]
        zipped = zip(columns, values)
        a_dictionary = dict(zipped)
        data.append(a_dictionary)

    data = pd.DataFrame.from_dict(data)
    cons_tipo_description = pd.concat([cons_tipo_description, data])
    cons_tipo_description = cons_tipo_description.sort_values('Consumer_type')
    cons_tipo_description = cons_tipo_description.sort_values('Count', ascending=False)
    return cons_tipo_description


def br_water_zone_description():
    """
    It should be the table with the Consumption by Zone
    """
    zona = df.drop(columns=["Consumer_number", 'Consumer_type', "Installation_number", 'Month', 'Year', 'Date'])
    zona = zona.groupby(['Installation_zone'], as_index=False).sum()
    zona = zona.sort_values('Consumption', ascending=False)
    zona = zona.reset_index().drop(columns=['index'])
    return zona


def br_water_total_consumption():
    """
    Here should be one line chart of total consumption by year.
    """
    yearly = df.drop(
        columns=['Month', 'Consumer_number', 'Installation_zone', 'Installation_number', 'Date', 'Consumer_type'])
    yearly1 = yearly.groupby(['Year'], as_index=False).sum()
    return yearly1


def br_water_total_consumption_by_consumer_type():
    """
    Here should be area plot of the total water consumption by year for each consumer type.
    """
    df_1 = df.copy()
    df_1 = df_1.drop(columns=['Month', 'Consumer_number', 'Installation_zone', 'Installation_number'])
    df_1 = df_1.groupby(['Year', 'Consumer_type'], as_index=False).aggregate({'Consumption': 'sum'})
    return df_1


#####################################################################
############# Domestic and Industrial types monthly analysis ########
#####################################################################


def br_domestico_industrial_monthly_consumption():
    """
    Here should be a line chart with monthly total consumption for domestico and industrial types
    """
    domestico = _get_monthly_consumption_by_type("DOMÉSTICO")
    insustrial = _get_monthly_consumption_by_type(" COM/INDUSTRIAL/OBRAS")
    return domestico, insustrial


def br_precipitation_monthly():
    """
    Here should be line chart of monthly precipitation level
    """
    precipitation = pd.read_csv("data/br/br_precipitation.csv")
    return precipitation


def br_population():
    """
    Line charts of the population dynamics.
    """
    population = pd.read_csv("data/br/br_population.csv")
    return population


def br_covid():
    """
    :return: covid cases and total water consumption in 2020
    """
    covid = pd.read_csv("data/br/br_covid.csv")

    df_2020 = df.drop(columns=["Consumer_number", "Installation_zone", "Installation_number", "Date"])
    df_2020 = df_2020[df_2020["Year"] == 2020].drop(columns=["Year"])
    df_2020 = df_2020[df_2020['Consumer_type'] == "DOMÉSTICO"].drop(columns=['Consumer_type'])
    df_2020 = df_2020.groupby(['Month'], as_index=False).sum()
    df_2020['Month'] = df_2020['Month'].apply(lambda x: calendar.month_abbr[x])

    return df_2020, covid


def br_water_consumption_by_consumer_type():
    cons = df.drop(
        columns=['Year', 'Month', 'Consumer_number', 'Installation_zone', 'Installation_number', 'Date']) \
        .groupby(['Consumer_type'], as_index=False).sum()
    cons = cons.sort_values('Consumption', ascending=False)
    cons = cons[cons['Consumer_type'] != 'CP.DOM/RURAL'].reset_index().drop(columns=['index'])
    return cons


def _get_monthly_consumption_by_type(consumer_type: str):
    consumption = df.drop(columns=["Consumer_number", "Installation_zone", "Installation_number", "Date"])
    consumption = consumption[consumption['Consumer_type'] == consumer_type].drop(columns=['Consumer_type'])
    consumption_sum = consumption.groupby(['Year', 'Month'], as_index=False).sum()
    consumption_sum["Date"] = consumption_sum["Year"].astype(str) + "/" + consumption_sum["Month"].astype(str)
    consumption_sum["Date"] = pd.to_datetime(consumption_sum["Date"], format='%Y/%m/%d').dt.strftime('%b-%Y')
    consumption_sum['Consumption'] = ((consumption_sum['Consumption']) / (consumption_sum['Consumption'].max())) * 10
    return consumption_sum


def generate_table(dataframe, max_rows=20):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ]),

    ])
