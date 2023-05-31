import random  # Импорт модуля для генерации случайных чисел
import math  # Импорт модуля для математических операций

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    def print_tree(self):
        if self.root is not None:
            self._print_recursive(self.root, "")
    
    def _print_recursive(self, node, prefix):
        if node is not None:
            print(prefix + "|--", node.value)
            self._print_recursive(node.left, prefix + "|   ")
            self._print_recursive(node.right, prefix + "|   ")

# Реализация распределения Эрланга с использованием метода сверток
def erlang_distribution(shape, scale):
    # Генерация n случайных чисел из равномерного распределения от 0 до 1
    uniform_numbers = [random.random() for _ in range(shape)]
    
    # Вычисление суммы логарифмов случайных чисел
    log_sum = sum([math.log(num) for num in uniform_numbers])
    
    # Применение масштабирования
    result = -scale * log_sum
    
    return result

# Функция для генерации случайных чисел с распределением Эрланга
def generate_erlang_numbers(shape, scale, count):
    return [erlang_distribution(shape, scale) for _ in range(count)]

# Функция для вставки элемента в бинарное дерево поиска
def insert_element(bst):
    value = float(input("Введите значение элемента для вставки: "))
    bst.insert(value)
    print("Элемент успешно вставлен!")

# Создание экземпляра класса BinarySearchTree
bst = BinarySearchTree()

# Ввод параметров генератора случайных чисел
shape = int(input("Введите параметр формы распределения Эрланга: "))
scale = int(input("Введите параметр масштаба распределения Эрланга: "))
count = int(input("Введите количество элементов в бинарном дереве: "))

# Проверка на минимальное количество вершин
if count < 12:
    print("Количество элементов должно быть не менее 12")
    exit()

# Генерация случайных чисел с распределением Эрланга
numbers = generate_erlang_numbers(shape, scale, count)

# Вставка элементов в бинарное дерево
for num in numbers:
    bst.insert(num)

# Вывод полученного бинарного дерева
print("Сгенерированное бинарное дерево:")
bst.print_tree()

# Вставка дополнительного элемента в бинарное дерево
insert_element(bst)

# Вывод обновленного дерева после вставки элемента
print("Обновленное бинарное дерево:")
bst.print_tree()
