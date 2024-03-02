import pandas as pd
from timeit import timeit
from text_search_algs import boyer_moore_search, kmp_search, rabin_karp_search

if __name__ == "__main__":

    tests = [
        {
            "file": "./text_files/стаття 1.txt",
            "pattern_real": "програмування",
            "pattern_fake": "неіснуючий рядок",
        },
        {
            "file": "./text_files/стаття 2.txt",
            "pattern_real": "Профілювання",
            "pattern_fake": "синхрофазотрон",
        },
    ]

    algorithms = [
        {
            "name": "Бойера-Мура",
            "func": boyer_moore_search,
        },
        {
            "name": "Кнута-Морріса-Пратта",
            "func": kmp_search,
        },
        {
            "name": "Рабіна-Карпа",
            "func": rabin_karp_search,
        },
    ]
    # список для зюерігання результатів тестів
    test_results = []

    # Налаштування тестів
    # к-ть повторів для timeit
    number = 1000

    print()
    print("Запуск тестів")

    for test in tests:
        file = test["file"]
        pattern_real = test["pattern_real"]
        pattern_fake = test["pattern_fake"]

        print()
        print("-" * 50)
        print(f"Тестовий файл '{file.split('/')[-1]}'")
        print("-" * 50)

        with open(file, "r", encoding="windows-1251") as f:
            text = f.read()

        # Пошук існуючого рядка
        print(f"Тест пошуку існуючого рядка '{pattern_real}'")
        for alg in algorithms:
            test_results.append(
                {
                    "file": file.split("/")[-1],
                    "alg": alg["name"],
                    "type": "існуючий рядок",
                    "time": timeit(
                        lambda: alg["func"](text, pattern_real), number=number
                    ),
                }
            )

        # Пошук неіснуючого рядка
        print(f"Тест пошуку неіснуючого рядка '{pattern_fake}'")
        for alg in algorithms:
            test_results.append(
                {
                    "file": file.split("/")[-1],
                    "alg": alg["name"],
                    "type": "неіснуючий рядок",
                    "time": timeit(
                        lambda: alg["func"](text, pattern_fake), number=number
                    ),
                }
            )
    print("-" * 50)
    print("Завершено тестування")
    print("=" * 50)

    # Виведення результатів тестів
    print(pd.DataFrame(test_results))
