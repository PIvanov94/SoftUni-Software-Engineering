movie_title = input()
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while movie_title != "Finish":
    free_seats = int(input())
    ticket_type = input()
    ticket_counter = 0
    while ticket_type != "End":
        ticket_counter += 1
        if ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1

        if ticket_counter == free_seats:
            break
        ticket_type = input()
    percentages = ticket_counter / free_seats * 100

    print(f"{movie_title} - {percentages:.2f}% full.")
    movie_title = input()

total_tickets = standard_tickets + student_tickets + kid_tickets

print(f"Total tickets: {total_tickets}")

standard_percentages = standard_tickets / total_tickets * 100
student_percentages = student_tickets / total_tickets * 100
kid_percentages = kid_tickets / total_tickets * 100

print(f"{student_percentages:.2f}% student tickets.")
print(f"{standard_percentages:.2f}% standard tickets.")
print(f"{kid_percentages:.2f}% kids tickets.")