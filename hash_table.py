class HashTable:
    """Клас для створення хеш-таблиці"""

    def __init__(self, size):
        """Конструктор класу.

        Приймає один аргумент — розмір хеш-таблиці, та створює список з певним
        числом ланцюгів. Число ланцюгів відповідає розміру хеш-таблиці."""
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        """Функція, яка приймає ключ і повертає індекс у хеш-таблиці.

        Використовує вбудовану функцію hash Python, щоб отримати хеш ключа,
        а потім бере остачу від ділення цього хешу на розмір таблиці
        self.size."""
        return hash(key) % self.size

    def insert(self, key, value):
        """функція, яка додає пару ключ-значення до хеш-таблиці.

        Вона спочатку обчислює хеш ключа, а потім перевіряє, чи вже існує в
        таблиці такий ключ. Якщо так, то оновлює значення. Якщо ні, то додає
        нову пару ключ-значення до відповідного ланцюга."""
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        """функція, яка повертає значення для даного ключа.

        Вона спочатку обчислює хеш ключа, а потім шукає пару ключ-значення у
        відповідному ланцюгу. Якщо вона знаходить пару з правильним ключем, то
        повертає відповідне значення. Якщо ні, вона повертає None."""
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        """функція, яка видаляє пару ключ-значення з хеш-таблиці.

        Вона спочатку обчислює хеш ключа, а потім шукає пару ключ-значення у
        відповідному ланцюгу. Якщо вона знаходить пару з правильним ключем, то її видаляє.

        Параметри:
        key - ключ, що видаляється."""
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    self.table[key_hash].remove(pair)
                    return True  # Повертаємо True, якщо видалення пройшло успішно
        return False  # Повертаємо False, якщо видалення не вдалося


if __name__ == "__main__":
    # Тестуємо нашу хеш-таблицю:
    H = HashTable(5)
    H.insert("apple", 10)
    H.insert("orange", 20)
    H.insert("banana", 30)

    # Виведемо всі елементи таблиці
    print(H.get("apple"))  # Виведе: 10
    print(H.get("orange"))  # Виведе: 20
    print(H.get("banana"))  # Виведе: 30

    # Тестуємо видалення елементів
    H.delete("banana")  # Видаляємо елемент "banana"
    H.delete("pinapple")  # Видаляємо неіснуючий елемент "pinapple"
