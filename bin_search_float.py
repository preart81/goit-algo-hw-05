def upper_limit(arr: list, item: float) -> tuple[int, float | None]:
    """Пошук найменшого елементу у відсортованому масиві, який є більшим або
    рівним значенню item

    Повертає кортеж, де першим елементом є кількість ітерацій, потрібних для
    знаходження елемента. Другим елементом є "верхня межа" (найменший елемент,
    який є більшим або рівним item).

    Використовує двійковий алгоритм пошук для відсортованого масиву з дробовими
    числами.

    Параметри
    ----------
    arr : list
        відсортований масив з дробовими числами
    item : float
        значення, яке потрібно знайти

    Результат:
    ----------
    Кортеж з 2 елементів iterations: int
        кількість ітерацій, потрібних для знаходження елемента
    up_limit: float|None
        верхня межа - це найменший елемент, який є більшим або рівним заданому
        значенню.
    """

    iterations = 0
    up_limit = None
    l_low = 0
    l_high = len(arr) - 1

    while l_low <= l_high:
        iterations += 1
        mid = (l_low + l_high) // 2  # знаходмо середній елемент

        # DEBUG
        # print(f"{iterations=},{l_low=}, {l_high=}, {mid = }, {arr[mid]=}")

        if item > arr[mid]:
            l_low = mid + 1  # переходмо в праву частину масиву, верхня межа не знайдена

        elif item < arr[mid]:
            up_limit = arr[mid]  # записуємо верхню межу (вона > item)
            l_high = mid - 1  # переходмо в ліву частину масиву

        else:  # якщо arr[mid] == item
            # записуємо верхню межу (вона = item)
            up_limit = arr[mid]
            # повертаємо кількість ітерацій і верхню межу
            return iterations, up_limit

    # цикл завершено, відповідне значення не знайдено
    # повертаємо кількість ітерацій і верхню межу, яка може бути Null
    return iterations, up_limit


if __name__ == "__main__":
    # Тестуємо нашу функцію
    arr = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
    print(f"{arr = }")
    print(f"{len(arr) = }")
    test_items = [1.5, 1.3, 1.0, 3.0, 1.35, 1.4]
    # test_items = [1.3]

    print()
    print(f"{'Шукане item':^14} | {'Ітерацій':^8} | {'верхня межа':^14}")
    print("-" * 50)
    for test in test_items:
        iterations, up_limit = upper_limit(arr, test)
        # print(f"{test:14} | {iterations:^8} | {up_limit:^14}")
        print(f"{test:14} | {iterations:^8} | {up_limit or 'None':^14}")
