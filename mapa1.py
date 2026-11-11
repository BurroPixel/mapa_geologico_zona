import os
import geopandas as gpd
import matplotlib.pyplot as plt

os.makedirs("mapas", exist_ok=True)

geo = gpd.read_file("data/geo21g1P.shp")
fallas = gpd.read_file("data/falla_21g1.shp")

fig, ax = plt.subplots(figsize=(10, 10))
geo.plot(ax=ax, column="codi", categorical=True, cmap="tab20",
         edgecolor="black", linewidth=0.2, legend=True,
         legend_kwds={"loc": "center left", "bbox_to_anchor": (1, 0.5),
                      "fontsize": 5, "ncol": 2})
fallas.plot(ax=ax, color="red", linewidth=0.8)

ax.set_title("Geología del cuadrángulo de Huarmey (21g1)")
ax.set_xlabel("Este (m) - UTM 17S")
ax.set_ylabel("Norte (m) - UTM 17S")
plt.savefig("mapas/mapa1.png", dpi=200, bbox_inches="tight")
plt.show()