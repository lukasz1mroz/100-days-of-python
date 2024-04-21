# import csv
#
# with open ('weather_data.csv') as weather_data:
#     rows = csv.reader(weather_data)
#
#     records = []
#
#     for row in rows:
#         records.append(row)
#
# print(f"Weather data: {records}")

import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
data_temp = data["temp"].to_list()

avg = int(sum(data_temp) / len(data_temp))
# avg = data["temp"].mean()

print(f"Avg temp: {avg}")
print(data[data.temp == data["temp"].max()])

data_two = pandas.DataFrame(data_dict)
data.to_csv("data_two.csv")