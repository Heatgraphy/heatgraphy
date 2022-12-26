import pytest
import numpy as np
from matplotlib import pyplot as plt

from heatgraphy.plotter.mesh import ColorMesh, Colors, LayersMesh, \
    TextMesh, SizedMesh, MarkerMesh


COLUMN = 20
ROW = 20

matrix = np.random.randint(0, 101, (ROW, COLUMN))

label = np.random.choice(list("abcdefg"), ROW)

stats_data = np.random.randn(10, ROW)

numbers = np.random.randint(10, 100, ROW)


def test_colormesh():
    ax = plt.subplot(111)
    ColorMesh(matrix).render(ax)
    plt.close()


def test_colors():
    ax = plt.subplot(111)
    Colors(matrix).render(ax)
    plt.close()
