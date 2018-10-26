import geopandas as gpd
import os
import pylab as pl

pumashp = gpd.GeoDataFrame.from_file(os.getenv("PUIDATA") + "/" + 
                    "geo_export_4ecb9d6c-d186-4a4d-839b-7f430b7915b6.shp")

pumashp.plot()
pl.title("just plotting the shapefile, default plot settings")
pl.show()


pumashp.plot(column="shape_area")
pl.title("coloring shapes by area and properly labling axes")
pl.ylabel("latitude (deg)")
pl.xlabel("longitude (deg)")
pl.show()

pumashp.plot(column="shape_area", legend=True)
pl.title("adding a colorbar (legend)")
pl.ylabel("latitude (deg)")
pl.xlabel("longitude (deg)")
pl.show()

print("crs", pumashp.crs)
pumashp.to_crs(epsg=2263, inplace=True)
print("new crs", pumashp.crs)
pumashp.plot(column="shape_area", legend=True)
pl.title("changing to State Plane Coordinates (epsg 2263)")
pl.ylabel("Northing (feet)")
pl.xlabel("Easting (feet)")
pl.show()


import choroplethNYC as cp
fig, ax, cb = cp.choroplethNYC(pumashp, column="shape_area")
ax.set_title("plotting with choroplethNYC for a custom colorbar placement")
pl.show()


fig, ax, cb = cp.choroplethNYC(pumashp, column="puma")
ax.set_title("colorcoding by PUMA")
pl.show()

fig, ax, cb = cp.choroplethNYC(pumashp, column="puma", kind="discrete")
ax.set_title("PUMA names are categorical value\n" +
             "so they should be plotted with a discrete colorbar\n" +
             "but there are too many values!")
pl.show()

pumashp['bo'] = (pumashp.puma.values / 100).astype(int)
fig, ax, cb = cp.choroplethNYC(pumashp, column="bo", kind="discrete")
ax.set_title("creating a categorical variable for the borough " +
             "from the PUMA code\n" +
             "and colorcoding by borough")
pl.savefig("NYCPUMA.png")
pl.show()

