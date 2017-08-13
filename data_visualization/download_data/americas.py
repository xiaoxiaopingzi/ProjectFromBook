# -*- coding: UTF-8 -*-
"""创建一个突出北美、中美、南美的世界地图"""
import pygal.maps.world

wm = pygal.maps.world.World()
wm.title = "North, Central, and South America"
wm.add("North America", ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file("americas.svg")

