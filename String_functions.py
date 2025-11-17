str = "my name Is sAkShi"

print(sorted(str))

print(sorted(str,reverse=True))

print(str.upper())

print(str.lower())

print(str.center(4))

print(str.swapcase()) # converts upper case char to lower case & vice versa

print(str.title()) # capitalise each 1st letter in each first word

print(str.capitalize()) # Capitalise 1st letter

print(str.rstrip("i")) # It removes any trailing characters

print(str.split(" ")) # Splits the string at the whitespace

print(str.endswith("hi")) # Returns true if string ends with substring.

print(str.startswith("my"))# Returns true if string starts with substring.

print(str.replace("s","v")) # replace all occurence of old 
print(str.replace("sakshi","diksha"))

print(str.find("s")) # Returns 1st index of 1st occurrer

print(str.count("am")) # Counts the occurrence of the substr