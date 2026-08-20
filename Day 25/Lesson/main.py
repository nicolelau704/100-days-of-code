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
# import pandas
# data = pandas.read_csv("weather_data.csv")

#print just a column of the data
# print(data["temp"])

#save the data as a dictionary
# data_dict = data.to_dict()
# print(data_dict)

#save the data from a column as a list
# temp_list = data["temp"].to_list()
# print(temp_list)

#Find the average temperature
# sum = 0
# for temp in temp_list:
#     sum += temp
#
# average = round(sum / len(temp_list))
# print(f"The average temperature is {average}")

#alternate way to find the average
# print(data["temp"].mean())

#Find the maximum temperature
# print(data["temp"].max())

#print a row of data
# print(data[data.day =="Monday"])

#print the row with the highest temperature
# highest = data["temp"].max()
# print(data[data.temp == highest])

#print the value of something from the row
# monday = data[data.day == "Monday"]
# print(monday.condition)

#convert Monday's temperature to Fahrenheit
# temp = (monday.temp * (9/5)) + 32
# print(temp)

#create a dataframe from scratch
# data_dict = {
#     "students": ['Amy', 'James', 'Angela'],
#     "scores": [76, 56, 65]
# }
#
# data2 = pandas.DataFrame(data_dict)
# data2.to_csv("new_data.csv")

#Create a dataframe of how many of each squirrel color there is in central park 2018
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data["Primary Fur Color"])
