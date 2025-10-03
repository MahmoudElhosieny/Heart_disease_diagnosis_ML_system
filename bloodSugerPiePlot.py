import matplotlib.pyplot as plt
from pkgs.visualization_functions import piePlot


plt.figure(figsize = (6,6))
piePlot('fasting_blood_sugar','Distribution of Fasting Blood Sugar %', ['green', 'lightgreen'])