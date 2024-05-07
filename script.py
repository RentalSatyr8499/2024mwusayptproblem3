import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import os

# Change the current working directory


# Load the data from the Excel file
df = pd.read_excel('usaypt dataframe (bucket).xlsx', sheet_name='Sheet2')

# Extract the columns from the dataframe
height = df['height']
volume = df['volume']
spin_ratio = df['spin ratio']

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
hist, xedges, yedges = np.histogram2d(height, volume, bins=3)

# Calculate the bin centers
xcenters = xedges[:-1] + np.diff(xedges)/2
ycenters = yedges[:-1] + np.diff(yedges)/2

# Construct arrays for the anchor positions of the 9 bars.
xpos, ypos = np.meshgrid(xcenters, ycenters, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Construct arrays with the dimensions for the 9 bars.
w = 2
dx = w*(xedges[1] - xedges[0]) / len(xedges)
dy = w*(yedges[1] - yedges[0]) / len(yedges)
dz = spin_ratio

# Create a color array (same length as xpos, ypos, and zpos)
colors = ['r', 'g', 'b'] * (len(xpos) // 3)

ax.set_xlabel('Drop height (cm)')
ax.set_ylabel('Droplet volume (mL)')
ax.set_zlabel('Spin Ratio (%)')

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors, zsort='average')

plt.show()