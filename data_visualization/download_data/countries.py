# -*- coding: UTF-8 -*-
"""
获取两个字母的国别码
The i18n module was removed in pygal-2.0.0, however, it can now be found in the 
pygal_maps_world plugin.You can install that with pip install pygal_maps_world. 
Then you can access COUNTRIES as pygal.maps.world.COUNTRIES:

    from pygal.maps.world import COUNTRIES
    or
    from pygal_maps_world.i18n import COUNTRIES
    
Whats left of the i18n module can be imported with:

    from pygal_maps_world import i18n
"""

# from pygal.i18n import COUNTRIES
from pygal_maps_world.i18n import COUNTRIES

# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code, COUNTRIES[country_code])

def get_country_code(country_name):
    """根据指定的国家，返回Pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # 如果没有找到指定的国家，就返回None
    return None

# print(get_country_code("Turkey"))
# print(get_country_code("Sweden"))
# print(get_country_code("Puerto Rico"))