import matplotlib.pyplot as plt
from pkgs.visualization_functions import countPlot


plt.figure(figsize = (8,6))
countPlot('sex', 'Gender Counts', 'Gender Type', 'Gender Counts', 'teal')
print('Done')