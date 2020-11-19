# to take zones of similar population and compare their report_times
import pandas as pd
import matplotlib.pyplot as plt
import sys

df = pd.read_csv("COVID_Dataset.csv")
df_pop = pd.read_csv("Population.csv")
#print(df.columns)
df["Time to report"] = df["Time of reporting"]-df["Time of Infection"]
df = df.replace(to_replace="Alive", value=0)
df = df.replace(to_replace="Dead", value=1)

df1 = df_pop.loc[(df_pop["Population"] <= 7250) & (df_pop["Population"] >= 6750)].reset_index()
#print(df1)
zones = []

for i in range(len(df1)):
    zones.append([int(df1.iloc[i]["x location"]), int(df1.iloc[i]["y location"])])
print(zones)

report = []
avg = []
maxi = []
most = 0
most_ind = []

for zone in zones:
    times = []
    num_cases = len(df.loc[(df["x location"] == zone[0]) & (df["y location"] == zone[1])])
    if num_cases > most:
        most = num_cases
        most_ind = zone
    for i in range(1, 8):
         times.append(len(df.loc[(df["x location"] == zone[0]) & (df["y location"] == zone[1]) & (df["Time to report"] == i)]))
    report.append(times)

#print("report: ", report)

for i in range(1, 8):
    maxi.append(len(df.loc[(df["x location"] == most_ind[0]) & (df["y location"] == most_ind[1]) & (df["Time to report"] == i)]))

for i in range(7):
    tot = 0
    for j in range(len(df1)):
        tot += report[j][i]
    avg.append(round(tot/len(df1), 2))

# get percentage of people reporting in the first 3 days and after first 3 days
average = [round(sum(avg[0:3])/sum(avg)*100, 2), round(sum(avg[3:])/sum(avg)*100, 2)]
m = [round(sum(maxi[0:3])/sum(maxi)*100, 2), round(sum(maxi[3:])/sum(maxi)*100, 2)]
print("avg:",average, avg)
print("max:", m, maxi)

fig = plt.figure()
x_ax = ['<=3 days', '>3days']
axes = fig.add_axes([0.07,0.07,0.7,0.7])
axes.set_title("Cases with respect to reporting time(avg) for areas of similar population")
axes.set_xlabel("Days to report")
axes.set_ylabel("Percentage of infected population reported")
axes.bar(x_ax, average)
plt.show()

fig2 = plt.figure()
axes = fig2.add_axes([0.07,0.07,0.7,0.7])
axes.set_title("Cases with respect to reporting time(Highest infection area with similar population)")
axes.set_xlabel("Days to report")
axes.set_ylabel("Percentage of infected population reported")
axes.bar(x_ax, m)
plt.show()



'''#df2 = df.groupby(["x location", "y location","Time to report"])["Outcome"].sum().reset_index()
df3 = df.groupby(["x location", "y location","Time to report"])["Age"].count().reset_index() # just a dummy count to keep a count of the total number of people infected in a zone
#print(df3)
df4 = pd.concat([df2, df3], axis=1)
# sorting by number of cases to get highest and lowest areas
df_sorted = df.groupby(["x location", "y location"])["Outcome"].count().reset_index()
df_des = df_sorted.sort_values(by=['Outcome'], inplace=False, ascending=False).reset_index()
#print("Des")
#print(df_des)
most = []
least = []
df_asc = df_sorted.sort_values(by=['Outcome'], inplace=False, ascending=True).reset_index()
for i in range(10):
    least.append([df_asc["x location"][i], df_asc["y location"][i]])
    most.append([df_des["x location"][i], df_des["y location"][i]])
#print(most)
#print(least)
#getting the profile of the zones with highest and lowest cases
high_prof = []
low_prof = []
for i in range(1, 8):
    count_max, count_min = 0, 0
    for j in most:
        #print("x, y", j[0], j[1])
        row = df3.loc[(df3["x location"] == j[0]) & (df3["y location"] == j[1]) & (df3["Time to report"] == i), "Age"] #["Age"]
        row = list(row)
        #print("row", row)
        count_max += row[0]
    for j in least:
        row = df3.loc[(df3["x location"] == j[0]) & (df3["y location"] == j[1]) & (df3["Time to report"] == i), "Age"] #["Age"]
        row = list(row)
        #print("row", row)
        if len(row) != 0:
            count_min += row[0]
    #print(count_min)
    #print(count_max)
    low_prof.append(count_min)
    high_prof.append(count_max)
print(high_prof)
print(low_prof)
#print("Asc")
#print(df_asc)
#print("Most")
#print(most)
#print("Least")
#print(least)

tot = sum(high_prof)
tot1 = sum(low_prof)
for i in range(7):
    high_prof[i] = (high_prof[i])/tot*100
    low_prof[i] = (low_prof[i])/tot1*100

fig = plt.figure()
x_ax = ['1 day', '2 days', '3 days', '4 days', '5 days', '6 days', '7 days']
axes = fig.add_axes([0.07,0.07,0.7,0.7])
axes.set_title("Cases with respect to reporting time(Low infection areas)")
axes.set_xlabel("Days to report")
axes.set_ylabel("Percentage of infected population")
axes.bar(x_ax, low_prof)
plt.show()

fig2 = plt.figure()
axes = fig2.add_axes([0.07,0.07,0.7,0.7])
axes.set_title("Cases with respect to reporting time(High infection areas)")
axes.set_xlabel("Days to report")
axes.set_ylabel("Percentage of infected population")
axes.bar(x_ax, high_prof)
plt.show()

df4.to_csv("dummy.csv")
'''
#print(type(df2), df2)

#zonewise = []*20
#for i in range(20):
#    zonewise.append([[]]*20)

#for serie in df4:
 #   print(serie)
    #zonewise[serie[1]-1][serie[1]-1].append(serie[4]/serie[8]*100)

#print(zonewise)
#for i in range(1, 8):
#    zonewise.append(df.loc[(df["Time to report"] == i) & (df.loc[(df["x location"])))))
