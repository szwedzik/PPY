import random

cities = ["Warszawa", "Kraków", "Łódź", "Wrocław", "Poznań", "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Katowice"]
visited_cities = []

while len(visited_cities) < 10:
    city = random.choice(cities)
    if city not in visited_cities:
        visited_cities.append(city)

print("Plan wycieczki:")
for i, miasto in enumerate(visited_cities):
    print(f"{i + 1}. {miasto}")
