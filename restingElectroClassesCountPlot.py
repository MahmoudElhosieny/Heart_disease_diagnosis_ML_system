import matplotlib.pyplot as plt
from pkgs.visualization_functions import countPlot


plt.figure(figsize = (8,6))
countPlot('resting_electrocardiographic_results', 'Resting Electrocardiographic Counts', 'Resting Electrocardiographic Classes', 'Resting Electrocardiographic Counts', 'lightgreen')
print('Done')