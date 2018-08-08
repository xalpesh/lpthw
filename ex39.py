#create a mapping of state abbreviation
states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
    }

# Create a basic set of states and cities
cities = {
    'CA' : 'San Francisco',
    'MI' :'Detroit',
    'FL' : 'Jacksonville'   
    }

# add more cities to list
cities['OR'] = 'Portland'
cities['NY'] = 'New York'

# print out some cities
print('-'*10)
print("NY state has city", cities['NY'])
print("OR state has city", cities['OR'])

#print some states
print('-'*10)
print("Michigan abreaviation is :", states['Michigan'])
print("Florida abreaviation is :", states['Florida'])

# do it by states and then city
print('-'*10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every stat abreaviation
print('-'*10)
for state, abrev in list(states.items()):
    print(f"{state} state is abbreaviate by {abrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# print every state and city in state
print('-' * 10)
for state, abrev in list(states.items()):
   print(f"{state} state is abbreaviate by {abrev}")
   print(f"and has the city {cities[abrev]}") 

print('-' * 10)
state = states.get('Texas')

if not state:
    print("Sorry no Texas")

city = cities.get('TX','Does not Exits')
print(f"the city for the state 'TX' is {city}")
