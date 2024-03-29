# goit-algo-hw-05

## 1. hash_table.py

Програмна реалізація хеш-таблиці у вигляді класу HashTable.

Функції:

-   **hash_function(self, key):** Функція, яка приймає ключ і повертає індекс у хеш-таблиці. Використовує вбудовану функцію hash Python, щоб отримати хеш ключа, а потім бере остачу від ділення цього хешу на розмір таблиці self.size.
-   **insert(self, key, value):** функція, яка додає пару ключ-значення до хеш-таблиці. Вона спочатку обчислює хеш ключа, а потім перевіряє, чи вже існує в таблиці такий ключ. Якщо так, то оновлює значення. Якщо ні, то додає нову пару ключ-значення до відповідного ланцюга.
-   **get(self, key):** функція, яка повертає значення для даного ключа. Вона спочатку обчислює хеш ключа, а потім шукає пару ключ-значення у відповідному ланцюгу. Якщо вона знаходить пару з правильним ключем, то повертає відповідне значення. Якщо ні, вона повертає None.
-   **delete(self, key):** функція, яка видаляє пару ключ-значення з хеш-таблиці. Вона спочатку обчислює хеш ключа, а потім шукає пару ключ-значення у відповідному ланцюгу. Якщо вона знаходить пару з правильним ключем, то видаляє її. Параметри: key - ключ, що видаляється.

## 2. bin_search_float.py

Реалізація двійкового пошуку для відсортованого масиву з дробовими числами.

**def upper_limit(arr: list, item: float) -\> tuple[int, float \| None]:** Пошук найменшого елементу у відсортованому масиві, який є більшим або рівним значенню item.

Повертає кортеж, де першим елементом є кількість ітерацій, потрібних для знаходження елемента. Другим елементом є "верхня межа" (найменший елемент, який є більшим або рівним item).

Використовує двійковий алгоритм пошук для відсортованого масиву з дробовими числами.

**Параметри**

**arr :** *list* відсортований масив з дробовими числами  
 **item :** *float* значення, яке потрібно знайти

**Результат:**

Кортеж з 2 елементів   
**iterations:** *int* кількість ітерацій, потрібних для знаходження елемента  
**up_limit:** *float\|None* верхня межа - це найменший елемент, який є більшим або рівним заданому значенню.

## 3. text_search.py

Порівняння швидкості роботи алгоритмів текстового пошуку.

Реалізовано алгоритми пошуку:

-   Бойера-Мура
-   Кнута-Морріса-Пратта
-   Рабіна-Карпа

Проведено тести швидкості роботи алгоритмів на двох текстових файлах з пошуком існуючого та неіснуючого в тексті зразка.

| Тестовий файл | Алгоритм             | Тип паттерна     | Час      |
|---------------|----------------------|------------------|----------|
| стаття 1.txt  | Бойера-Мура          | існуючий рядок   | 0.010547 |
| стаття 1.txt  | Кнута-Морріса-Пратта | існуючий рядок   | 0.029576 |
| стаття 1.txt  | Рабіна-Карпа         | існуючий рядок   | 0.067198 |
| стаття 1.txt  | Бойера-Мура          | неіснуючий рядок | 0.349420 |
| стаття 1.txt  | Кнута-Морріса-Пратта | неіснуючий рядок | 1.534561 |
| стаття 1.txt  | Рабіна-Карпа         | неіснуючий рядок | 3.347846 |
| стаття 2.txt  | Бойера-Мура          | існуючий рядок   | 0.056810 |
| стаття 2.txt  | Кнута-Морріса-Пратта | існуючий рядок   | 0.157509 |
| стаття 2.txt  | Рабіна-Карпа         | існуючий рядок   | 0.420245 |
| стаття 2.txt  | Бойера-Мура          | неіснуючий рядок | 0.517203 |
| стаття 2.txt  | Кнута-Морріса-Пратта | неіснуючий рядок | 1.963563 |
| стаття 2.txt  | Рабіна-Карпа         | неіснуючий рядок | 5.215334 |

### Висновки

Найкращий час пошуку у алгоритма Бойера-Мура: його час втричі менше часу роботи алгоритму Кнута-Морріса-Пратта і в \~7 разів менше за час алгоритма Рабіна-Карпа.

Разом з тим з результатів тестів видно, що пошук неіснуючого рядка в рази збільшує час виконання всіх алгоритмів.  
При пошуку неіснуючого рядка рейтинг швидкості роботи алгоритмів залишається таким же як і при пошуку існуючого рядка.

Рейтинг швидкості роботи алгоритмів текстового пошуку в порядку зростання часу пошуку:

1.  Бойера-Мура
2.  Кнута-Морріса-Пратта
3.  Рабіна-Карпа
