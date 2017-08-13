# -*- coding: UTF-8 -*-
"""分析世界上的人口信息"""
import json
import pygal.maps.world
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
try:
    from countries import get_country_code
except ImportError:
    raise ImportError('The file is not found. Please check the file name!')

filename = "population_data.json"
with open(filename) as f:
    pop_data = json.load(f)

# 创建一个包含人口数量的字典
cc_populations = {}
# 打印每个国家2010年的人口数量
for pop_dict in pop_data:
    if pop_dict["Year"] == "2010":
        country_name = pop_dict["Country Name"]
        # python无法将包含小数的字符串转换为整数，需要先转为浮点数，再将浮点数转换为整数
        population = int(float(pop_dict["Value"]))
        code = get_country_code(country_name)
        if code:
            # 如果返回了国别码，就将国别码和人口数量分别作为键和值填充字典
            cc_populations[code] = population

# 根据人口数量将所有的国家分为三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# 查看每组分别包含多少个国家
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

"""
十六进制格式的RGB颜色是一个以井号（#）打头的字符串，后面跟着6个字符，
其中前两个字符表示红色分量，接下来的两个表示绿色分量，最后两个表示蓝色分量。每个分量
的取值范围为00（没有相应的颜色）~FF（包含最多的相应颜色）

使用LightColorizedStyle加亮了地图的颜色

add()方法，它接受一个标签和一个列表，其中后者包含我们要突出的国家的国别码。
# 每次调用add()都将为指定的国家选择一种新颜色，并在图表左边显示该颜色和指定的标签
# 当第二个实参传递了一个字典而不是列表时，这个字典将两个字母的Pygal国别码作为键，
# 将人口数量作为值。Pygal根据这些数字自动给不同国家着以深浅不一的颜色（人口最少的国家颜色最浅，人口最多的国家颜色最深）
"""
wm_style = RS('#336699', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add("小于1000万人", cc_pops_1)
wm.add("1000万到10亿人之间", cc_pops_2)
wm.add("10亿人以上", cc_pops_3)

wm.render_to_file("world_population.svg")