import matplotlib.pyplot as plt
from pkgs.visualization_functions import countPlot


plt.figure(figsize = (8,6)) # type: ignore
countPlot('chest_pain', 'Chest Pain Counts', 'Chest Pain Classes', 'Chest Pain Counts','green')
print('Done')