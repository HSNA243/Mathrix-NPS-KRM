#Code that determines how many people are infected overall till a certain day

#Columns are 'Time of Infection', 'Time of reporting', 'x location', 'y location',
#       'Age', 'Diabetes', 'Respiratory Illnesses', 'Abnormal Blood Pressure',
#       'Outcome'

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
df = pd.read_csv("COVID_Dataset.csv")
pop = pd.read_csv("Population.csv")

#print(df.columns)

new_inf = [0]*250
new_mort = [0]*250

sz = len(df['Age'])
for i in range(sz):
    new_inf[df['Time of Infection'][i]] += 1
    if df['Outcome'][i] == 'Dead':
        new_mort[df['Time of reporting'][i]] += 1

tot_inf = new_inf[0:250]
tot_mort = new_mort[0:250]

for i in range(len(new_inf)-1):
    tot_inf[i+1] = tot_inf[i] + new_inf[i+1]
    tot_mort[i+1] = tot_mort[i] + new_mort[i+1]

print(tot_mort)
print(tot_inf)
plt.plot(range(250), tot_inf, 'y-', label = "Total Infections")
plt.plot(range(250), new_inf, 'y--', label = "New Infections")
plt.plot(range(250), tot_mort, 'r-', label = "Total Deaths")
plt.plot(range(250), new_mort, 'r--', label = "New Deaths")
plt.legend()
plt.yscale('log')
plt.axis([1,250,1,1000000])
plt.ylabel('People')
plt.xlabel('Day number')
plt.show()
    
