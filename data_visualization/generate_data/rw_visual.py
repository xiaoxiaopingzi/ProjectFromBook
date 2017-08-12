# -*- coding: UTF-8 -*-
"""  """
import matplotlib.pyplot as plt

try:
    from randomWalk import RandomWalk
except ImportError:
    raise ImportError('The file is not found. Please check the file name!')

while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n)")
    if keep_running == "n":
        break