month = int(input("Enter month (1-12): "))
room_rate = int(input("Enter room rate per day: "))
days_stayed = int(input("Enter number of days stayed: "))

if month < 1 or month > 12:
    print("Invalid month. Please enter a value between 1 and 12.")
else:
    demand_months = [4, 5, 11, 12]
    if month in demand_months:
        room_rate = room_rate+((room_rate*20)/100)  

    total_tariff = room_rate * days_stayed
    print("Total hotel tariff is:", (total_tariff))