class VoterElligibility(Exception):
    def __init__(self):
        super()

try:
    age = int(input("Enter your age: "))
    if age < 18: raise VoterElligibility
except ValueError:
    print("Age must be an integer.")
except VoterElligibility:
    print("You can't vote yet. You must be at least 18 years old.")
else: print("You are elligible to vote!")
finally: print("Program ended.")