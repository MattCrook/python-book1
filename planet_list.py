planet_list = ['Mercury', 'Mars']
planet_list.append("Jupiter")
planet_list.append("Saturn")
# ['Mercury, Mars', 'Jupiter', 'Saturn']


# print(planet_list)

planet_list.extend(["Uranus", "Neptune"])
# print(planet_list)
# ['Mercury, Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
planet_list.append("Pluto")
# print(planet_list)
# ['Mercury, Mars', 'Venus', 'Earth', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']


rocky_planets = planet_list[0: 3]
print(rocky_planets)
# ['Mercury, Mars', 'Venus', 'Earth']

del planet_list[7]
print(planet_list)
# ['Mercury, Mars', 'Venus', 'Earth', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']


spacecraft = [
    ("Cassini", "Saturn"),
    ("Viking", "Mars"),
    ("Blue", "Neptune"),
    ("Storm", "Jupiter"),
    ("Cold", "Pluto"),
    ("Home", "Earth"),
    ("Hot", "Venus"),
    ("Close", "Mercury"),
    ("Low Mass", "Uranus")
]

for planet in planet_list:
    for satellite in spacecraft:
        if planet == satellite[1]:
          print(satellite[0])
