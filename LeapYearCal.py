
while True:
    year = int(input("Please enter a year: "))

    remainder_by_4 = year % 4
    remainder_by_100 = year % 100
    remainder_by_400 = year % 400

    if remainder_by_4 == 0 and remainder_by_100 != 0:
        print(f"{year} is a leap year")
    elif remainder_by_400 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is NOT a leap year")
