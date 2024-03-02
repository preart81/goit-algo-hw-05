def bin_search_float(arr, item):
    """Двійковий пошук для відсортованого масиву з дробовими
    числами.

    Результат: повертає кортеж з двома елементами:
     - n = кількість ітерацій, потрібних для знаходження елемента
     - up_limit = верхня межа - це найменший елемент, який є більшим або рівним
       заданому значенню.
    """

    iterations = 0
    low = 0
    up_limit = None
    high = len(arr) - 1

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if arr[mid] < item:
            low = mid + 1
        elif arr[mid] > item:
            up_limit = arr[mid]
            high = mid - 1
        else:
            up_limit = arr[mid]
            return iterations, up_limit
    return iterations, up_limit


if __name__ == "__main__":
    arr = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
    for test in [1.5, 1.0, 3.0, 1.3, 1.4]:
        iterations, up_limit = bin_search_float(arr, test)
        print(f"Результат для {test}: ітерацій: {iterations}, верхня межа: {up_limit}")
