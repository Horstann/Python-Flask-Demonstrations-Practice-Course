x = input("Enter a character or integer: ")

try: # if x is a char or single digit integer
    a = ord(x)
    print(f"ASCII value of '{x}' = {a}.")
except:
    try: # if x is x a multi-digit integer
        a = int(x)
        print(f"You entered the integer {str(a)}")
    except ValueError: # if x isn't a multi-digit integer
        print("You entered neither a character nor integer!")
    finally: # gets executed regardless
        print(f"In finally block")

print()

"Multiple except statements"
try:
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    c = a/b
    print(f"{a} / {b} = {c}")
except ZeroDivisionError:
    print("Division by 0 isn't possible")
except ValueError:
    print("Not an integer")
except:
    print("Error")