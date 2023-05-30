import random

# Класс узла бинарного дерева
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Функция для генерации случайного бинарного дерева
def generate_binary_tree(num_elements):
    if num_elements <= 0:
        return None
    root_value = random.randint(1, 100)
    root = Node(root_value)
    num_elements -= 1
    if num_elements > 0:
        # Распределение параметров для генерации левого и правого поддеревьев
        k = random.randint(1, 10)  # Параметр формы распределения Эрланга
        scale = random.uniform(0.1, 1.0)  # Параметр масштаба распределения Эрланга
        
        # Генерация случайного количества элементов для левого поддерева
        num_left_elements = random.randint(0, num_elements)
        num_right_elements = num_elements - num_left_elements
        
        # Рекурсивная генерация левого и правого поддеревьев
        root.left = generate_binary_tree(num_left_elements)
        root.right = generate_binary_tree(num_right_elements)
    
    return root

# Функция для вставки элемента в бинарное дерево
def insert_element(root, value):
    if root is None:
        return Node(value)
    
    if value < root.value:
        root.left = insert_element(root.left, value)
    elif value > root.value:
        root.right = insert_element(root.right, value)
    
    return root

# Ввод параметров генератора случайных чисел
k = int(input("Введите параметр формы распределения Эрланга (целое число): "))
scale = float(input("Введите параметр масштаба распределения Эрланга (вещественное число от 0.1 до 1.0): "))
num_elements = int(input("Введите количество элементов в бинарном дереве (не менее 12): "))

# Генерация случайного бинарного дерева
random.seed()
tree = generate_binary_tree(num_elements)

# Вывод сгенерированного дерева
print("Сгенерированное бинарное дерево:")
def print_tree(root):
    if root is None:
        return
    print_tree(root.left)
    print(root.value)
    print_tree(root.right)
print_tree(tree)

# Вставка нового элемента
value_to_insert = int(input("Введите элемент для вставки в дерево: "))
tree = insert_element(tree, value_to_insert)

# Вывод дерева после вставки элемента
print("Дерево после вставки элемента:")
print_tree(tree)