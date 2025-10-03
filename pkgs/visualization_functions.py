import matplotlib.pyplot as plt
from pkgs.data import clean_data


cleanData = clean_data
#Count plot
def countPlot(column_name,title, xlabel, ylabel, barcolor):
    ax = cleanData[column_name].value_counts().plot(kind = 'bar', rot = 20,color= barcolor, edgecolor = 'black',linewidth = 1)
    plt.title(title)
    plt.xlabel(xlabel,fontsize = 11, fontweight = 'bold')
    plt.ylabel(ylabel)
    ax.bar_label(ax.containers[0], fontsize = 8, fontweight = 'bold', padding = 2)
    return ax
    # plt.show()

#pie plot
def piePlot(column_name,title, colors_list):
    ax =cleanData[column_name].value_counts().plot(kind = 'pie', autopct = '%0.1f%%', colors = colors_list ,shadow = True,startangle = 90,explode =[0.05,0])
    plt.title(title)
    return ax
    # plt.show()


#Histogram plot
def agehistPlot():
    ax = cleanData['age'].plot(kind = 'hist', rot = 25, color='lightgreen', edgecolor = 'black', linewidth = 1.2)
    plt.title('Histogram of Age Distribution')
    plt.xlabel('Age',fontsize = 11, fontweight = 'bold')
    plt.ylabel('Frequency')
    ax.bar_label(ax.containers[0], fontsize =8, fontweight = 'bold', padding = 2) # type: ignore
    return ax
    # plt.show()


#Features plot
def locationCountPlot():
    countPlot('dataset_location', 'Datasets Location Cases', 'Dataset Location Name', 'Cases Counts', 'lightblue')


def genderCountPlot():
    countPlot('sex', 'Gender Counts', 'Gender Type', 'Gender Counts', 'teal')


def slopCountPlot():
    countPlot('slope', 'Slope Counts', 'Slope Classes', 'Slope Counts', 'teal')


def restingElectroCountPlot():
    countPlot('resting_electrocardiographic_results', 'Resting Electrocardiographic Counts', 'Resting Electrocardiographic Classes', 'Resting Electrocardiographic Counts', 'lightgreen')


def chestingPainCountPlot():
    countPlot('chest_pain', 'Chest Pain Counts', 'Chest Pain Classes', 'Chest Pain Counts','green')

def bloodSugerPiePlot():
    piePlot('fasting_blood_sugar','Distribution of Fasting Blood Sugar %', ['green', 'lightgreen'])

def exercisePiePlot():
    piePlot('exercise_induced_angina','Distribution of Exercise Induced Angina %', ['teal', 'lightblue'])

print('done')


