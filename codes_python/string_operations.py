print("PROGRAM TO DEMONSTRATE VARIOUS STRING OPERATIONS")
print()

print("Consider a string :")
name = "SouMyaDeep siNha"
print("name = ", end=' ')
print(name)
print()
print("name.capitalize() => Converts the first character to upper case => ", end=' ')
print(name.capitalize())
print()

print("name.upper() => Converts a string into upper case => ", end=' ')
print(name.upper())
print()

print("name.lower() => Converts a string into lower case => ", end=' ')
print(name.lower())
print()

print("name.center(length, character) => Returns a centered string => ", end=' ')
print(name.center(30, "-"))
print()

print("name.count(''e'') => Returns the number of times a specified value occurs in a string => ", end=' ')
print(name.count("e"))
print()

print("name.endswith(''p'') => Returns true if the string ends with the specified value => ", end=' ')
print(name.endswith("p"))
print()

print("name.find(''M'') => Searches the string for a specified value and returns the position of where it was found => ", end=' ')
print(name.find("M"))
print()

print("name.index(''o'') => Searches the string for a specified value and returns the position of where it was found => ", end=' ')
print(name.index("o"))
print()

print("name.islower() => Returns True if all characters in the string are lower case => ", end=' ')
print(name.islower())
print()

print("name.isupper() => Returns True if all characters in the string are upper case => ", end=' ')
print(name.isupper())
print()

print("name.isdigit() => Returns True if all characters in the string are ldigits => ", end=' ')
print(name.isdigit())
print()

print("name.rfind(''D'') => Searches the string for a specified value and returns the last position of where it was found => ", end=' ')
print(name.rfind("D"))
print()

print("name.title() => Converts the first character of each word to upper case => ", end=' ')
print(name.title())
print()