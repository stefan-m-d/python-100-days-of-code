# import csv
# data = []

# with open ("Day 25 - CSV Data and the Pandas library\weather_data.csv") as file:
#     for line in file:
#         row = line.rstrip('\n')
#         data.append(row)

# print (data)

# temperatures = []

# with open ("Day 25 - CSV Data and the Pandas library\weather_data.csv") as file:
#     data = csv.reader(file)
#     for row in data:
#         if row[1] == 'temp':
#             pass
#         else:  
#             temperatures.append(int(row[1]))

# print (temperatures)

import pandas

data = pandas.read_csv("Day 25 - CSV Data and the Pandas library\weather_data.csv")

#list = data["temp"].to_list()

# average = sum(list) / len (list)

# print (list)
# print (average)

# get column mean

# print (data["temp"].mean())

# get column max

# print (data["temp"].max())

# get row where temp is max

# print (data[data.temp == data.temp.max()])

# get monday temp and convert it to fahrenheit (or freedom units)

monday = data[data.day == "Monday"]

print (monday.temp[0])
print ((monday.temp[0])*1.8 + 32)