#This is a tourist recommendation program that allows you to find amazing parts of a particular city drawing from your personal interests

destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#def get_destination_index(destination):
  # destination_index = None
  # for des in destinations:
  #   if des == destination:
  #     destination_index = destinations.index(des)
  #     return destination_index
  # return destination_index

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

   

#Testing get destination function
#print(get_destination_index("Los Angeles, USA")) --> expected output is 2
#print(get_destination_index("Paris, France")) --> expected output is 0

#def get_traveler_location(traveler):
  # traveler_destination = test_traveler[1]
  # traveler_destination_index = get_destination_index(traveler_destination)
  # return traveler_destination_index

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)

#print(test_destination_index)
  
# We are testing the get_traveler_location function here

# test_destination_index = get_traveler_location(test_traveler) --> expected output == 1
# print(test_destination_index)

# attractions = []
# for des in destinations:
#   attractions.append([])

# print(attractions)
attractions = [[] for destinaton in destinations]

#print(attractions)

#The block of code below is useful for adding various tourist attractions that correspond to the various destinations in our list

def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
  except ValueError:
    return

add_attraction("Los Angeles, USA",['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])


#print(attractions)


#def add_attraction(destination, attraction):
  # try:
  #   destination_index = get_destination_index(destination)
  # except ValueError:
  #   print("Error Here")

#print(add_attraction("Mombasa" ,"Fort Jesus"))


#The code below is meant to help our user find the most interesting places in a new city based on their interests
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest


la_arts = find_attractions("Los Angeles, USA", ['art'])

#print(la_arts)

#In the code below we seek to connect people with the attractions they are interested in

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)

  interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination
  for attraction in traveler_attractions:
    interests_string = interests_string + ": " + attraction
  return interests_string


smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])

print(smills_france)



