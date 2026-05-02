def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        salaries = []
        for line in lines:
            line = line.strip()
            if line:  # пропускаємо порожні рядки
                name, salary = line.split(',')
                salaries.append(int(salary))

        total = sum(salaries)
        average = total // len(salaries)

        return total, average

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return None, None
    except ValueError:
        print("Неправильний формат даних у файлі")
        return None, None


# Використання
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")