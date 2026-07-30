def total_salary(path):
    with open(path, "r", encoding="utf-8") as fsalary:
        content = fsalary.readlines()
        total = sum(float(line.split(",")[1]) for line in content)

    return {
        "total_salary": total,
        "average_salary": total / len(content)
    }

print(total_salary("salary.txt"))