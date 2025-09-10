full_name = input("Enter your full name (First, Middle, Last): ")

first, middle, last = [name.strip() for name in full_name.split(',')]

first = first.capitalize()
last = last.capitalize()

middle = middle[0].upper() + "."

print(f"Formatted Name: {last}, {first} {middle}")