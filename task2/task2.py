def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            keys = ["id", "name", "age"]
            values = [line.strip().split(",") for line in file]

            return [dict(zip(keys, value)) for value in values]

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return []