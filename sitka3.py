# Changing the file to include all the daa for the year of 2018
# Change the tittle to daily low and hiw temperatures -2018
# extract low temps from the file and add the chart
# shade in the area between high and low

import csv
from datetime import datetime

infile = open("sitka_weather_2018_simple.csv", "r")

csvfile = csv.reader(infile)

header_row = next(csvfile)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []  # y-axis
lows = []  # y-axis
dates = []  # x-axis

# somedate = datetime.strptime('2018-07-01', '%Y-%m-%d')

for row in csvfile:
    highs.append(int(row[5]))  # by adding int the values are intigers
    lows.append(int(row[6]))
    thedate = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(thedate)

print(highs)
print(lows)

import matplotlib.pyplot as plt

fig = plt.figure()
plt.plot(dates, highs, c="red", alpha=0.5)  # alpha is to make it transparent
plt.plot(dates, lows, c="blue", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor="cyan", alpha=0.5)

plt.title("Daily low and high temperatures - 2018", fontsize=16)
plt.xlabel("Days", fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

fig.autofmt_xdate()
plt.show()
