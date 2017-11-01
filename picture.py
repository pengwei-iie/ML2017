#!/usr/bin/python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as py
lena = mpimg.imread('./Lena.png')
print lena.shape
plt.imshow(lena)
