def get_cats_info(path):
    try:
        cats = []
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    cat_id, name, age = line.split(',')
                    cats.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
        return cats

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return []
    except ValueError:
        print("Неправильний формат даних у файлі")
        return []


# Використання
cats_info = get_cats_info("cats_file.txt")
print(cats_info)