
while True:
    year = int(input("Please enter a year: "))

    remeinder_by_4 = year % 4
    remeinder_by_100 = year % 100
    remeinder_by_400 = year % 400

    if remeinder_by_4 == 0 and remeinder_by_100 != 0:
        print(f"{year} is a leap year")
    elif remeinder_by_400 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is NOT a leap year")
