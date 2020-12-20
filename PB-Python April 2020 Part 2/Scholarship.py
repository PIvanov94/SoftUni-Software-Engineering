import math

income = float(input())
average_success = float(input())
minimum_wage = float(input())

social_scholarship = math.floor(minimum_wage * 0.35)
excellent_scholarship = math.floor(average_success * 25)

if average_success < 4.50:
    print("You cannot get a scholarship!")
elif 4.50 <= average_success < 5.50:
    if income < minimum_wage:
        print(f"You get a Social scholarship {social_scholarship} BGN")
    else:
        print("You cannot get a scholarship!")
elif average_success >= 5.50:
    if income < minimum_wage:
        if social_scholarship > excellent_scholarship:
            print(f"You get a Social scholarship {social_scholarship} BGN")
        else:
            print(f"You get a scholarship for excellent results {excellent_scholarship} BGN")
    else:
        print(f"You get a scholarship for excellent results {excellent_scholarship} BGN")