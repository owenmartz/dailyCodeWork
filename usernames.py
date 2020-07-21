#This is a username generator based on first and last names. This program is also meant to generate temporary passwords alongside these usernames

def username_generator(first_name, last_name):
  if len(first_name) < 3 or len(last_name) < 4:
    username = first_name + last_name
  else:
    username = first_name[:3] + last_name[:4]
  return username

#the password function takes in the username and shifts all the letters to the right by one such that the last letter of the username ends up as the first letter of the password
def password_generator(username):
  password = ""
  for char in range(len(username)):
    letter = username[char-1]
    password += letter
    
  return password
