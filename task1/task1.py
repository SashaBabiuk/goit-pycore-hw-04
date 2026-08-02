def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.readlines()
            total = sum(float(line.split(",")[1]) for line in content)

        return (total, total / len(content))
        
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return (0, 0)

print(total_salary("salary.txt"))