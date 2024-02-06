import matplotlib.pyplot as plt
from matplotlib import image as img
import time
import sys
import numpy as np

def PlotFunction():

  # Keep in mind that the function can be changed to a sin, cos or tan graph when considering trigonometry. 
  
        plt.title("Brain Wave Analysis")
        x = np.arange(1, 15 * np.pi, 0.000001)
        y = np.sin(x)
        plt.plot(x, y, color="green")
        plt.show()

PlotFunction()
