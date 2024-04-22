"""
nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
"""
print("---------- Exercise 1 ----------")
temperatures = []

with open("nyc_weather.csv") as file:
    for line in file:
        tokens = line.strip().split(',')
        if len(tokens) >= 2:
            try:
                temperature = int(tokens[1])
                temperatures.append(temperature)
            except ValueError:
                print("Invalid Temperature. Ignored the Row:", line)
        else:
            print("Incomplete Data. Ignored the Row:", line)

print("Temperatures:", temperatures)


# What was the average temperature in first week of January?
print(sum(temperatures[0:7]) / len(temperatures[0:7]))

# What was the maximum temperature in first 10 days of Jan
print(temperatures[0:10])

print("---------- Exercise 2 ----------")

weather_dict = {}

with open("nyc_weather.csv", "r") as file:
    for line in file:
        tokens = line.split(',')
        day = tokens[0]
        try:
            temperature = int(tokens[1])
            weather_dict[day] = temperature
        except ValueError:
            print("Invalid temperature. Ignored the row")

print("Weather Dictionary:", weather_dict)

# What was the temperature on Jan 9
print(weather_dict['Jan 9'])

# What was the temperature on Jan 4
print(weather_dict['Jan 4'])
