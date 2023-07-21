import pandas as pd
import geopandas as gpd
import cv2

# polygons = gpd.read_file("data/polygons/polygons.shp")
df = pd.read_csv("data/br/br_water_main.csv", low_memory=False, usecols=["Year",
                                                                      "Consumer_type",
                                                                      "Installation_zone",
                                                                      "Consumption"])
pt_polygons = gpd.read_file("data/pt/portugal_districts_polygons/distritos_shape.shp")
# polygons = gpd.read_file("data/br/polygons/portugal_polygons.shp")
pt_water = pd.read_excel("data/pt/water_consumption_by_district.xlsx")

br_zone_consumption_pic = cv2.imread("data/yearly_zone_consumption.jpg")

pt_water_pic = cv2.imread("data/yearly_total_water_consumption_by_region.png")


def portugal_polygons():
    return pt_polygons


def pt_water_district():
    return pt_water




# def braganca_polygons():
#     br_polygons = polygons[polygons['Concelho'] == 'BRAGANÇA']
#     br_polygons = br_polygons.drop(
#         columns=['Dicofre', 'Concelho', 'Distrito', 'TAA', 'AREA_EA_Ha', 'AREA_T_Ha', 'Des_Simpli'])
#     table = df.groupby(['Installation_zone', 'Consumer_type', 'Year'], as_index=False).sum().sort_values('Consumption',
#                                                                                                          ascending=False)
#     br_merged = br_polygons.merge(table, left_on='Freguesia', right_on='Installation_zone', how='inner')
#
#     return br_merged
