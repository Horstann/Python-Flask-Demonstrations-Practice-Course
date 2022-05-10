import re
Str = "The ape was at the apex."

# Search for a substring in a string
if re.search("ape", Str):
    print("Found!")

print()

# findall() returns a list of matches
# '.' to denote any character or whitespace
x = re.findall("ape.", Str)
print(x)

print()

# finditer() returns iterator of matches
for i in re.finditer("ape.", Str):
    indexLoc = i.span()
    print(indexLoc)
    print(Str[indexLoc[0] : indexLoc[1]])

print()

# square brackets [] match any characters between []
Str2 = "cat Rat mat fat Pat lat"
x = re.findall("[crmfpl]at", Str2)
print(x)

print()

# denote characters within a range
x = re.findall("[c-fC-F]at", Str2) # mean any character within c-f (lowercase) or C-F (uppercase)
print(x)

print()

# '^' to denote any characters to ignore/exclude
x = re.findall("[^cR]at", Str2)
print(x)

print()



# Replace all matches
regex = re.compile("[cR]at")
Str3 = regex.sub("CHANGE", Str2)
print(Str3)

print()

# What if we want '.' to denote a period, as usual? Use '\.'
# What if we want '\' to denote '\', as usual? Use '\\'

# Convert multi-line strings to single-line - replace '\n' with whitespace ' '
Str4 = """This is a
multi-line string
that goes on for
many many lines...
"""
regex = re.compile("\n")
Str5 = regex.sub(" ", Str4)
print(Str5)

print()

# Match single digits
# '\d' denotes '[0-9]'
# '\D' denotes '[^0-9]'
Str6 = "12a3b4c5"
print(re.findall("\d", Str6))
print(re.findall("\D", Str6))

print()

# Match series of digits by length
num = "123 1234 12345 123456 1234567"
print(re.findall("\d{4,6}", num))

print()

# Match based on width
phNum = "412-555-1212"
name = "Ultraman"
if re.search("\w{3}-\w{3}-\w{4}", phNum):
    print("It's a valid phone no.")
if re.search("\w{2,20}", name):
    print("It's a valid name.")

print()

# '\s' denotes space '[\f\n\r\t\v]'
# '\S' denotes '[^\f\n\r\t\v]'
if re.search("\w{2,20}\s\w{2,20}", "Takashi Mahayita"):
    print("It's a valid full name.")

print()

# '+' denotes 1 or more characters
print(re.findall("a+", "a as ape bug"))