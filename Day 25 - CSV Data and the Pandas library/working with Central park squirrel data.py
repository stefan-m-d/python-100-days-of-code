import pandas 

data = pandas.read_csv("Day 25 - CSV Data and the Pandas library/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_num = 0
red_num = 0
black_num = 0

fur_color_data = data["Primary Fur Color"]

for row in fur_color_data: 
    if row == "Gray":
        grey_num+=1
    elif row == "Black":
        black_num+=1
    elif row == "Cinnamon":
        red_num+=1
        

#shorter method shown:

# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])        
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print (f"Red squirrels: {red_num} , Black squirrels: {black_num} and Gray squirrels: {grey_num}")

new_data = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [grey_num, red_num, black_num]
}

new_data_to_save = pandas.DataFrame(new_data)
new_data_to_save.to_csv("new_data.csv")