import os
from os import listdir
from os.path import join
import numpy as np
import skimage.io
import skimage.transform
import matplotlib.pyplot as plt


path = 'HRDataSet/t1.bmp'
img = skimage.io.imread(path)
plt.show(img)
