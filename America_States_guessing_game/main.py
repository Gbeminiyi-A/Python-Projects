import pandas

#
# data = pandas.read_csv('weather_data.csv')
# temp = data['temp']
#
# # temp.mean()
# # print(data[data.temp == data['temp'].max()])
#
# monday = data[data.day == 'Monday']
# cel = monday['temp']
# fah = (9/5)*cel + 32
# print(fah)

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
color = data[data['Primary Fur Color'] == 'Cinnamon']
cin = color.count()
print(cin.to_dict())

color2 = data[data['Primary Fur Color'] == 'Black']
black = color2.count()
black.to_dict()

color3 = data[data['Primary Fur Color'] == 'Gray']
gray = color3.count()
print(gray.to_dict())

data_dict = {'colors': ['Cinnamon', 'Black', 'Gray'],
             'number': [cin['Primary Fur Color'], black['Primary Fur Color'], gray['Primary Fur Color']]}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv('new data')
