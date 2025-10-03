import matplotlib.pyplot as plt
from pkgs.visualization_functions import countPlot


plt.figure(figsize = (8,6))
countPlot('slope', 'Slope Counts', 'Slope Classes', 'Slope Counts', 'teal')
print('done')