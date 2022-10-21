import json


def csv_to_json(csv_data) -> (str, json):
    result_status = 'FAILURE'
    result_data = []

    row_count = csv_data.shape[0]
    column_count = csv_data.shape[1]
    column_names = csv_data.columns.tolist()

    # Option [1]
    # row_json_data = csv_data.to_json(orient='records')

    # Option [2]
    final_row_data = []
    for index, rows in csv_data.iterrows():
        final_row_data.append(rows.to_dict())

    json_result = {'rows': row_count, 'cols': column_count, 'columns': column_names, 'rowData': final_row_data}
    result_data.append(json_result)
    result_status = 'SUCCESS'

    return result_status, result_data
