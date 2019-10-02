# creates a dict called county
county = {
    'Chatham': 'CH',
    'Wake': 'WK',
    'Alamance': 'AL',
    'Lee': 'LE',
    'Harnett': 'HT',
    'Brunswick': 'BK'
}
# creates a dict called cities
cities = {
    'CH': 'Siler City',
    'WK': 'Raleigh',
    'AL': 'Burlington',
    'LE': 'Sanford',
    'HT': 'Angier',
    'BK': 'Oak Island'
}
# prints out the county and the corresponding town
print('-' * 10)
# for the number of state, abbrev, the key pairs do the following
for state, abbrev in list(county.items()):
    print(f"{state} county is abbreviated {abbrev}")
    print(f"and has the settlement of: {cities[abbrev]}")

# for city and town key pairs, print the second set, the town names.
print("\n")
for city, towns in list(cities.items()):
    print(f"{towns}")