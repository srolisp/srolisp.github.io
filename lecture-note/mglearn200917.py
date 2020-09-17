import folium
m = folium.Map(location=[45.5236, -122.6750])
m

m.__dir__()

m._to_png()

import os
os.get_exec_path()

m._to_png(5)

import io
import folium
from PIL import Image

m = folium.Map(location=[45.5236, -122.6750], width=500, height=300)
img_data = m._to_png(5)
img = Image.open(io.BytesIO(img_data))
img
