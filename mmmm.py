import random

def generate_and_sort_arrays(n):
    arrays = []

    for i in range(n):
        array_size = random.randint(1, 10)  # Случайный размер массива от 1 до 10
        random_array = [random.randint(1, 100) for _ in range(array_size)]  # Заполняем массив случайными числами

        arrays.append(random_array)

    sorted_arrays = sorted(arrays, key=lambda x: (sum(x), len(x) % 2 == 0, x[0]))

    return sorted_arrays

# Пример использования
n = 5  # Задайте желаемое количество массивов
result = generate_and_sort_arrays(n)
print(result)