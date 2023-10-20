def forecast(*args):
    weather_data = {
        'Sunny': [],
        'Cloudy': [],
        'Rainy': [],
    }
    [weather_data[weather].append(city) for city, weather in args]

    result = ''

    for weather_, cities in weather_data.items():
        for city_ in sorted(cities):
            result += f'{city_} - {weather_}\n'

    return result


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print()
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print()
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
