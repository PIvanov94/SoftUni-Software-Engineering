n = int(input())
cars = {}

for _ in range(n):
    car, mileage, fuel = input().split("|")
    mileage = int(mileage)
    fuel = int(fuel)

    cars[car] = {"mileage": mileage, "fuel": fuel}

line = input()

while not line == "Stop":
    data = line.split(" : ")
    command = data[0]
    car = data[1]
    if command == "Drive":
        distance = int(data[2])
        fuel = int(data[3])
        if fuel > cars[car]["fuel"]:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["mileage"] += distance
            cars[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car]["mileage"] >= 100000:
            print(f"Time to sell the {car}!")
            del cars[car]
    elif command == "Refuel":
        fuel = int(data[2])
        refuel_tank = cars[car]["fuel"] + fuel
        if refuel_tank > 75:
            # current_fuel = cars[car]["fuel"]
            print(f"{car} refueled with {75 - cars[car]['fuel']} liters")
            cars[car]["fuel"] = 75
        else:
            cars[car]["fuel"] += fuel
            print(f"{car} refueled with {fuel} liters")
    elif command == "Revert":
        kilometers = int(data[2])
        decreased_mileage = cars[car]["mileage"] - kilometers
        if decreased_mileage <= 10000:
            cars[car]["mileage"] = 10000
        else:
            cars[car]["mileage"] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")
    line = input()

sorted_cars = sorted(cars.items(), key=lambda x: (-x[1]['mileage'], x[0]))

for car, value in sorted_cars:
    print(f"{car} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")