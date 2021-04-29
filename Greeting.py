
var = input("Please enter a value: ")

print(var.upper())
print(len(var))

is_number = False

for character in var:
    if character.isdigit():
        is_number = True

print(is_number)