data = input()
companies_ids = {}

while not data == "End":
    company_name, employee_id = data.split(" -> ")
    if company_name not in companies_ids:
        companies_ids[company_name] = []
    if employee_id not in companies_ids[company_name]:
        companies_ids[company_name].append(employee_id)

    data = input()

for company, emp_id in sorted(companies_ids.items(), key=lambda x: x[0]):
    print(company)
    for e_id in emp_id:
        print(f"-- {e_id}")