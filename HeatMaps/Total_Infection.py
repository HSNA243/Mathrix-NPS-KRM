#Code that determines how many people are infected overall till a certain day

#Columns of Covid are 'Time of Infection', 'Time of reporting', 'x location', 'y location',
#       'Age', 'Diabetes', 'Respiratory Illnesses', 'Abnormal Blood Pressure',
#       'Outcome'

#Columns of pop are 'x location', 'y location', 'Population'

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("COVID_Dataset.csv")
pop = pd.read_csv("Population.csv")

day_num = 100

new_inf_area = [[[0 for i in range(20)] for j in range(20)] for k in range(250)]

sz = len(df['Age'])
print(sz, "meow")

for i in range(sz):
    new_inf_area[df['Time of Infection'][i]][df['y location'][i]-1][df['x location'][i]-1] += 1 
    
tot_inf_area = [[[0 for i in range(20)] for j in range(20)] for k in range(250)]
tot_inf_perc = [[[0 for i in range(20)] for j in range(20)] for k in range(250)]

for x in range(20):
    for y in range(20):
        tot_inf_area[0][y][x] = new_inf_area[0][y][x]

for i in range(249):
    for x in range(20):
        for y in range(20):
            tot_inf_area[i+1][y][x] = tot_inf_area[i][y][x]+new_inf_area[i+1][y][x]
            tot_inf_perc[i][y][x] = tot_inf_area[i][y][x]/pop['Population'][20*x+y]

pop_den = [[0 for i in range(20)] for j in range(20)]
for y in range(20):
    for x in range(20):
        pop_den[y][x] = pop['Population'][20*x+y]

im = plt.imshow(tot_inf_area[day_num], cmap = "magma", interpolation = "bilinear")
plt.colorbar(im)
plt.title("Day"+str(day_num))
plt.show()

