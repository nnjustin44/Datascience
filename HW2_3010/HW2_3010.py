import pandas as pd
import numpy as np
# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
import plotly as plt
#from matplotlib import rc
import seaborn as sns

cell = pd.read_csv("\User\justinnguyen\Downloads\Cancer Risk.csv")

# Descriptive Stats of the dataframe

print(cell.describe(include='all'), '\n')
print(cell.describe(include=[np.object]), '\n')
print(cell.describe(include=[np.number]), '\n')
print(cell.head())
# Tables Freq
print(cell['Gender'].value_counts())
s = pd.crosstab(cell.Gender, columns='Gender')
print(s)

# Rel.Freq.
s_rel = s/s.sum()
print(s_rel)

# Bar Chart
sx=['Female', 'Male']
pos=np.arange(len(sx))
ct=[106,83]

plt.bar(pos, ct, color='blue', edgecolor= 'black')
plt.xticks(pos, sx)
plt.xlabel('Gender', frontsize=14)
plt.ylabel('Count', fontsize=14)
plt.title ('Figure 1: Bar chart of Gender')

# Pie Chart
labels=['Female','Male']
colors=['pink', 'blue']
sizes=[106,83]
plt.pie(sizes,labels=labels,colors=colors, startangle= 90, autopct= '%1.1f%%')
plt.title('Figure 2: Pie Chart of Gender')
plt.axis('equal')
plt.show()

labels=['Never','Former','Current']
colors=['green','orange','red']
sizes=[106,83]
plt.pie(sizes,labels=labels, colors=colors, startangle=90, autopct='%1.1f%%')
plt.title("Figure 3: Pie Chart of SmokeStat")
plt.axis('equal')
plt.show()



#Quant Var

#Histogram
plt.hist(cell['Calories'], color='red', edgecolor='black')
plt.xlabel('Caloric Intake')
plt.ylabel('Calories')
plt.title('Figure 4: for Caloric Intake')
plt.show()

plt.hist(cell['Fat'], color='yellow', edgecolor= 'black')
plt.xlabel('Fat Levels')
plt.ylabel('Fat')
plt.title('Figure 5: for Fat Levels')
plt.show()

plt.hist(cell['Age'], color='green', edgecolor= 'black')
plt.xlabel('Age')
plt.ylabel('Smoke') #correct the label 'smoke' isnt right
plt.title('Figure 7: for Age Levels')
plt.show()

#Boxplot
plt.boxplot(cell['Calories'])
plt.xlabel('Number of Calories')
plt.title('Figure 8: Boxplot of Caloric Intake')
plt.show()

plt.boxplot(cell['Fat'])
plt.xlabel('Fat Levels')
plt.title('Figure 9: Boxplot of Fat Levels')
plt.show()

plt.plot(cell['Age'])
plt.xlabel('Age of Smokers')
plt.title('Figure 10: Boxplot of Fat Levels')
plt.show()


#Tables Rel. Freq.
print(cell['Calories'].value_counts())
a= pd.crosstable(cell.Calories, columns= 'Calories')
print(s)

s_rel = a/a.sum()
print(s_rel)

