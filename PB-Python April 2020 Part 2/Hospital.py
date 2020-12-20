period = int(input())
docs = 7
treated_patients = 0
untreated_patients = 0

for i in range(1, period + 1):
    patients = int(input())
    if i % 3 == 0 and untreated_patients > treated_patients:
        docs += 1
    if patients > docs:
        untreated_patients += patients - docs
        treated_patients += docs
    else:
        treated_patients += patients

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")