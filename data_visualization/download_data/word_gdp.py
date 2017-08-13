# -*- coding: UTF-8 -*-
"""分析世界上的人口信息"""
import json
import pygal.maps.world
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
try:
    from countries import get_country_code
except ImportError:
    raise ImportError('The file is not found. Please check the file name!')

filename = "gdp.json"
with open(filename) as f:
    gdp_data = json.load(f)

cc_gdps = {}
for gdp_dict in gdp_data:
    if gdp_dict["Year"] == "2015":
        country_name = gdp_dict["Country Name"]
        gdp = int(float(gdp_dict["Value"]))
        code = get_country_code(country_name)
        if code:
            cc_gdps[code] = gdp

cc_gdps_1, cc_gdps_2, cc_gdps_3 = {}, {}, {}
for cc, gdp in cc_gdps.items():
    if gdp < 100000000000:
        cc_gdps_1[cc] = gdp
    elif gdp < 1000000000000:
        cc_gdps_2[cc] = gdp
    else:
        cc_gdps_3[cc] = gdp


wm_style = RS('#336699', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World GDP in 2015, by Country'
wm.add("GDP在1千亿以下", cc_gdps_1)
wm.add("GDP在1千亿到1万亿之间", cc_gdps_2)
wm.add("GDP在1万亿以上", cc_gdps_3)

wm.render_to_file("world_gdp.svg")