import matplotlib.pyplot as plt
from pkgs.visualization_functions import piePlot


plt.figure(figsize = (6,6))
piePlot('exercise_induced_angina','Distribution of Exercise Induced Angina %', ['teal', 'lightblue'])
print('Done')