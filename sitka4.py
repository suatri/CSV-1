# handle error checking try and except
# change the file to use death valley


import csv
from datetime import datetime

infile = open("death_valley_2018_simple.csv", "r")

csvfile = csv.reader(infile)

header_row = next(csvfile)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []  # y-axis
lows = []  # y-axis
dates = []  # x-axis
row_count = 1

# somedate = datetime.strptime('2018-07-01', '%Y-%m-%d')


try:
    for row in csvfile:
        highs.append(int(row[4]))  # by adding int the values are intigers
        lows.append(int(row[5]))
        thedate = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(thedate)
        row_count += 1
        print(row_count)

except:
    print(f"This is the row with the data issue {row_count}")


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
