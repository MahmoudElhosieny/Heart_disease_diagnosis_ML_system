import matplotlib.pyplot as plt
from pkgs.visualization_functions import countPlot


plt.figure(figsize = (6,6))
countPlot('dataset_location', 'Datasets Location Cases', 'Dataset Location Name', 'Cases Counts', 'lightblue')
print('Done')