#Create a Dictionary with a List nested inside for the values
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

#Print "Lille"
#print(travel_log["France"][1])

#Create a nested List inside a List
nested_list = ["A", "B", ["C", "D"]]

#Print "D"
#print(nested_list[2][1])

#Create a dictionary with a nested dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 8
    },
}

#Print "Stuttgart"
print(travel_log["Germany"]["cities_visited"][2])
