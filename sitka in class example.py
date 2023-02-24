# Changing the file to include all the daa for the year of 2018
# Change the tittle to daily low and hiw temperatures -2018
# extract low temps from the file and add the chart
# shade in the area between high and low

import csv
from datetime import datetime

infile = open("sitka_weather_2018_simple.csv", "r")
infile2 = open("death_valley_2018_simple.csv", "r")

csvfile = csv.reader(infile)
csvfile2 = csv.reader(infile2)

header_row = next(csvfile)
header_row2 = next(csvfile2)

# get the title by reading the first value in the second index
Title_name1 = next(csvfile)[1]
Title_name2 = next(csvfile2)[1]
print(Title_name1)
print(Title_name2)

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs1 = []  # y-axis
lows1 = []  # y-axis
dates1 = []  # x-axis

highs2 = []  # y-axis
lows2 = []  # y-axis
dates2 = []  # x-axis

row_count = 1

# somedate = datetime.strptime('2018-07-01', '%Y-%m-%d')
# create a variable hlding the index matching the desired argument
# header_index = header_row.index("TMAX")
# header_index = header_row.index("TMIN")

for row in csvfile:
    highs1.append(
        int(row[header_row.index("TMAX")])
    )  # by adding int the values are intigers
    lows1.append(int(row[header_row.index("TMIN")]))
    thedate = datetime.strptime(row[2], "%Y-%m-%d")
    dates1.append(thedate)


try:
    for row in csvfile2:
        highs2.append(
            int(row[header_row2.index("TMAX")])
        )  # by adding int the values are intigers
        lows2.append(int(row[header_row2.index("TMIN")]))
        thedate = datetime.strptime(row[2], "%Y-%m-%d")
        dates2.append(thedate)
        row_count += 1
        print(row_count)
except:
    print(f"This is the row with the data issue {row_count}")

print(highs2)
print(lows2)

import matplotlib.pyplot as plt

fig = plt.figure()
plt.subplot(2, 1, 1)
plt.plot(dates1, highs1, c="red", alpha=0.5)  # alpha is to make it transparent
plt.plot(dates1, lows1, c="blue", alpha=0.5)
plt.fill_between(dates1, highs1, lows1, facecolor="cyan", alpha=0.5)
plt.title(Title_name1, fontsize=16)
plt.xlabel("Days", fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

fig = plt.figure()
plt.subplot(2, 1, 2)
plt.plot(dates2, highs2, c="red", alpha=0.5)  # alpha is to make it transparent
plt.plot(dates2, lows2, c="blue", alpha=0.5)
plt.fill_between(dates2, highs2, lows2, facecolor="cyan", alpha=0.5)
plt.title(Title_name2, fontsize=16)
plt.xlabel("Days", fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.suptitle(
    "Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US"
)

fig.autofmt_xdate()

plt.show()


# the 2 is for the number of rows, the first 1 is the number of columns,
# and the last one is the reference to the plot
# subplot is used to specify the different plot area
""" plt.subplot(2, 1, 1)
plt.plot(dates1, highs1, c="red")
plt.title("Highs")

plt.subplot(2, 1, 2)
plt.plot(dates1, lows1, c="blue")
plt.title("Lows")


plt.show() """


fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

ax1.plot(dates1, highs1, c="red", alpha=0.5)
ax1.plot(dates1, lows1, c="blue", alpha=0.5)
ax1.fill_between(dates1, highs1, lows1, facecolor="cyan", alpha=0.5)
ax1.set_title(Title_name1, fontsize=16)
ax1.set_ylabel("Temperature (F)", fontsize=16)
ax1.tick_params(axis="both", which="major", labelsize=16)

ax2.plot(dates2, highs2, c="red", alpha=0.5)
ax2.plot(dates2, lows2, c="blue", alpha=0.5)
ax2.fill_between(dates2, highs2, lows2, facecolor="cyan", alpha=0.5)
ax2.set_title(Title_name2, fontsize=16)
ax2.set_xlabel("Days", fontsize=16)
ax2.set_ylabel("Temperature (F)", fontsize=16)
ax2.tick_params(axis="both", which="major", labelsize=16)

plt.suptitle(
    "Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US"
)
fig.autofmt_xdate()
plt.show()
