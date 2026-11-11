import geopandas as gpd

geo = gpd.read_file("data/geo21g1P.shp")
print("CRS:", geo.crs)
print("Límites:", geo.total_bounds)
print("Unidades:", len(geo))
print(geo.columns.tolist())

pueblos = gpd.read_file("data/pueblo_21g1.shp")
print(pueblos.head(15))