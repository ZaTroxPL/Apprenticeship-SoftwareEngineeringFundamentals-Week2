
var = input("Please enter a value: ")

print(var.upper())
print(len(var))

is_number = False

for i in var:
    if i.isdigit():
        is_number = True

print(is_number)