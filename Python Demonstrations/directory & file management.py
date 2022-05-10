import os

print("\nCurrent working directory:\n" + os.getcwd())
print("\nCurrent working directory as a byte object:\n" + str(os.getcwdb()) + "\n")

d = os.getcwd()

# Change working directory
os.chdir(os.getcwd() + "\\Python Demonstrations")
# List directory
print(os.getcwd())
print(os.listdir())
print()

# Make a new directory
os.mkdir('Test')
# Rename a directory
os.rename('Test', 'New')
# Remove a file
#os.remove('Test.txt')
# Remove a directory
os.rmdir('New')

os.chdir(d)
print(os.getcwd())