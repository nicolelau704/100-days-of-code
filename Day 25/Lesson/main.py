#Open and save each row of a csv file into a list
# with open("weather_data.csv") as f:
#     unformatted_data = f.read()
#     data = unformatted_data.splitlines()
#     print(data)

#Use python's built in csv file reader then try to save the data of one column to a list
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#
#     for row in data:
#         print(row)
#
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

#Use Pandas to open, read, and display information from the csv file
import pandas
data = pandas.read_csv("weather_data.csv")
print(data["temp"])
