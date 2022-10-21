import pandas as pd

from scripts.utils import csv_to_json
import logging

df = pd.read_csv("data/br_water_main.csv")


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
    logging.info(df)
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
    json_status, json_data = csv_to_json(cons_tipo_description)
    return {'resultStatus': json_status, 'resultData': json_data}


def br_water_zone_description():
    """
    It should be the table with the Consumption by Zone
    """
    zona = df.drop(columns=["Consumer_number", 'Consumer_type', "Installation_number", 'Month', 'Year', 'Date'])
    zona = zona.groupby(['Installation_zone'], as_index=False).sum()
    zona = zona.sort_values('Consumption', ascending=False)
    zona = zona.reset_index().drop(columns=['index'])
    json_status, json_data = csv_to_json(zona)
    return {'resultStatus': json_status, 'resultData': json_data}


def br_water_total_consumption():
    yearly = df.drop(
        columns=['Month', 'Consumer_number', 'Installation_zone', 'Installation_number', 'Date', 'Consumer_type'])
    yearly1 = yearly.groupby(['Year'], as_index=False).sum()
    json_status, json_data = csv_to_json(yearly1)
    return {'resultStatus': json_status, 'resultData': json_data}

