import numpy as np

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

# Функция для генерации случайных чисел с распределением Эрланга
def generate_erlang_numbers(shape, scale, count):
    return np.random.gamma(shape, scale, count)

# Создание экземпляра класса BinarySearchTree
bst = BinarySearchTree()

# Ввод параметров генератора случайных чисел
shape = int(input("Введите параметр формы распределения Эрланга: "))
scale = int(input("Введите параметр масштаба распределения Эрланга: "))
count = max(12, int(input("Введите количество элементов в бинарном дереве (минимум 12): ")))

# Генерация случайных чисел с распределением Эрланга
numbers = generate_erlang_numbers(shape, scale, count)

# Вставка элементов в бинарное дерево
for num in numbers:
    bst.insert(num)

# Вывод полученного бинарного дерева
print("Сгенерированное бинарное дерево:")
bst.print_tree()
