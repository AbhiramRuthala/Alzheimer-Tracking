
# Import the necessary files

import numpy as np
import matplotlib.pyplot as plt

# Code to plot the respective graphs using matplotlib

def Plot():
        plt.figure(figsize=(12.5, 8))
        x = np.linspace(0, 100, 1000)
  # Determine the equation
        y = (-1 * (x ** 2))+ 2 * x + 5

        # y = [neuronLevels.get(HormoneTracker), result]
        # plt.xlim(0, neuronLevels.get(HormoneTracker))

        plt.plot(x, y, color='blue')
        plt.xlabel('Time (In seconds)')

        # Y-Axis plot
        plt.ylabel(HormoneTracker.capitalize() + ' Levels')
        plt.title('The ' + HormoneTracker.capitalize() + ' levels over time (In seconds)')
  # Show ticks on X and Y-Axis
        plt.xticks()
        plt.yticks()
  # Show the graph when you run the program
        plt.show()


# Call the function
    Plot()
