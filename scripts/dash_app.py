# from dash import html
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import text
# import pandas as pd
# import dash
# from dash import dcc
#
# # app = Flask(__name__)
#
# app = dash.Dash(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///identifier.db'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# # db = SQLAlchemy(app)
#
# cons_tipo_description = pd.DataFrame({'Consumer_type': [], 'Count': [], 'Max_consumption': [],
#                                       'Min_consumption': [], 'Avg_consumption': [], 'Std_consumption': []})
# columns = list(cons_tipo_description)
# data = []
# df = pd.read_csv("../../../PandIA project/PandIA exploratory analysis/data/water/braganca/main.csv")
# for i in df['Consumer_type'].unique():
#     if i == 0:
#         continue
#     consumer_i = df[df['Consumer_type'] == i]
#     # consumer_type_name = cons_tipos[cons_tipos['Code'] == i].Name.item()
#     N = len(consumer_i)
#     Max = consumer_i['Consumption'].max()
#     Min = consumer_i['Consumption'].min()
#     Avg = consumer_i['Consumption'].mean()
#     Std = consumer_i['Consumption'].std()
#     values = [i, N, Max, Min, Avg, Std]
#     zipped = zip(columns, values)
#     a_dictionary = dict(zipped)
#     data.append(a_dictionary)
# cons_tipo_description = cons_tipo_description.append(data, True)
# cons_tipo_description["Consumer_type"] = cons_tipo_description["Consumer_type"].astype(int)
# cons_tipo_description = cons_tipo_description.sort_values('Consumer_type')
# print(cons_tipo_description)
#
# app.layout = html.Div(
#     children=[
#         html.H1(children="Consumer Type Analytics",
#                 style={"fontSize": "48px", "color": "red"}),
#         html.P(
#             children="Analyze the behavior of the consumers"
#             " between 2013 and 2020",
#         ),
#         dcc.Graph(
#             figure={
#                 "data": [
#                     {
#                         "x": cons_tipo_description["Consumer_type"],
#                         "y": cons_tipo_description["Max_consumption"],
#                         "type": "lines",
#                     },
#                 ],
#                 "layout": {"title": "Maximal consumption by consumer types"},
#             },
#         ),
#         dcc.Graph(
#             figure={
#                 "data": [
#                     {
#                         "x": cons_tipo_description["Consumer_type"],
#                         "y": cons_tipo_description["Avg_consumption"],
#                         "type": "lines",
#                     },
#                 ],
#                 "layout": {"title": "Average consumption by consumer types"},
#             },
#         ),
#     ]
# )
#
#
#
#
#
#
# # @app.route('/test_db')
# # def test_db():
# #     try:
# #         db.session.query(text('1')).from_statement(text('SELECT 1')).all()
# #         return '<h1>It works.</h1>'
# #     except Exception as e:
# #         # e holds description of the error
# #         error_text = "<p>The error:<br>" + str(e) + "</p>"
# #         hed = '<h1>Something is broken.</h1>'
# #         return hed + error_text
#
# #
# # @app.route('/hello')
# # def hello_world():
# #     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run_server(debug=True)
