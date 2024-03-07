class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

    def __str__(self, level=0, prefix="Root: "):
        ret = "\\t" * level + prefix + str(self.key) + "\\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def right_rotate(y):
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x

def insert(root, key):
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

# Максимум
def find_max_value_in_avl(root):
    current = root

    # Ідемо вправо до кінця дерева
    while current.right is not None:
        current = current.right

    # Повертаємо найбільше значення
    return current.key

# Мінімум
def find_min_value_in_avl(root):
    current = root

    # Ідемо вліво до кінця дерева
    while current.left is not None:
        current = current.left

    # Повертаємо найменше значення
    return current.key

# Сума
def sum_all_values_in_avl(root):
    if root is None:
        return 0

    # Рекурсивно обчислюємо суму для лівого та правого піддерева
    left_sum = sum_all_values_in_avl(root.left)
    right_sum = sum_all_values_in_avl(root.right)

    # Повертаємо суму значень поточного вузла та його піддеревь
    return root.key + left_sum + right_sum

# Запуск 
root = None
keys = [10, 20, 26, 0, 25, 28, 27, 2, 120, 126, -100, 125]

for key in keys:
    root = insert(root, key)   

print("AVL-Дерево:")
print(root)

# Максимум
max_value = find_max_value_in_avl(root)
print("Найбільше значення в AVL-дереві:", max_value)

# Мінімум
min_value = find_min_value_in_avl(root)
print("Найменше значення в AVL-дереві:", min_value)

# Сума
total_sum = sum_all_values_in_avl(root)
print("Сума всіх значень в AVL-дереві:", total_sum)

