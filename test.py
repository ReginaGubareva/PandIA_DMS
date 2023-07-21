import json

import geopandas as gpd
import plotly.graph_objects as go
import plotly.express as px

import geo_analysis

pt_polygons = geo_analysis.portugal_polygons()
# print(pt_polygons.columns)

gdf = gpd.GeoDataFrame(pt_polygons)
geo_json = gdf.to_json()
pt_json = json.loads(geo_json)

for i, feature in enumerate(pt_json["features"]):
    feature["id"] = str(i)
    # print(i)

json_object = json.dumps(pt_json)

pt_water = geo_analysis.pt_water_district()
# print(pt_water)

# with open('data/portugal_districts_polygons/pt_geo.json', 'w') as out_file:
#     out_file.write(json_object)


# portugal_map_fig = px.choropleth_mapbox(pt_water,
#                                         geojson=json_object,
#                                         locations=pt_water.Distrito,
#                                         color=pt_water[2013],
#                                         # featureidkey="properties.district",
#                                         # projection="mercator",
#                                         range_color=[pt_water[2013].min(), pt_water[2013].max()]
#                                         )

portugal_map_fig = pt_water.plot()
