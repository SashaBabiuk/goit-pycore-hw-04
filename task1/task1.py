def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as fsalary:
            content = fsalary.readlines()
            total = sum(float(line.split(",")[1]) for line in content)

        return {
            "total_salary": total,
            "average_salary": total / len(content)
        }

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return {
            "total_salary": 0,
            "average_salary": 0
        }

print(total_salary("salary.txt"))