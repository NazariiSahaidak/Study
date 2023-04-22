# Імпортуємо необхідні бібліотеки
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
# Граф на основі матриці суміжності

path1 = "l1_1.txt"
path2 = "l1_2.txt"
path3 = "l1_3.txt"

with open(path1) as f:
    lines = (line for line in f if not line.startswith('#'))
    graph = np.loadtxt(lines, skiprows=1)

G = nx.from_numpy_matrix(np.matrix(graph), create_using=nx.DiGraph)
layout = nx.spring_layout(G)
nx.draw(G, layout)
nx.draw_networkx_edge_labels(G, pos=layout)
plt.show()


print(graph)
# Визначаємо кількість вершин у графі
V = len(graph)

# Метод, який повертає ребро з найменшою вагою
def get_min_edge(graph, selected):
    min_edge = float('inf')
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if not selected[j] and graph[i][j]:
                    if min_edge > graph[i][j]:
                        min_edge = graph[i][j]
                        x = i
                        y = j
    return x, y, min_edge


# Метод, який повертає ребро з найбільшою вагою
def get_max_edge(graph, selected):
    min_edge = float('-inf')
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if not selected[j] and graph[i][j]:
                    if min_edge < graph[i][j]:
                        min_edge = graph[i][j]
                        x = i
                        y = j
    return x, y, min_edge

# Метод, який знаходить мінімальне покриваюче дерево
def boruvka_mst(graph, worst=False):
    # Створюємо пусте множини MST
    mst = []

    # Ініціалізуємо кожну вершину як окремий компонент
    parent = [i for i in range(V)]

    # Зберігаємо кількість компонентів у графі
    num_trees = V

    # Поки кількість компонентів у графі більше одного
    while num_trees > 1:
        # Ініціалізуємо прапорці, що показують, чи є вершина у компоненті MST
        selected = [False] * V

        # Для кожної компоненти
        for i in range(num_trees):
            # Знаходимо ребро з найменшою вагою, що з'єднує компоненту з іншими компонентами
            if worst == True:
                x, y, min_edge = get_max_edge(graph, selected)
            else:
                x, y, min_edge = get_min_edge(graph, selected)

            # Додаємо ребро до MST
            mst.append([x, y, min_edge])

            # Позначаємо вершину як обрану
            selected[y] = True

            # Об'єднуємо компоненти
            x_parent = parent[x]
            y_parent = parent[y]
            for j in range(V):
                if parent[j] == y_parent:
                    parent[j] = x_parent
            # Оновлюємо кількість компонентів у графі
            num_trees = len(set(parent))

        return mst

sum_mst, sum_mst_worst = 0, 0
mst = boruvka_mst(graph)
mst_worst = boruvka_mst(graph, worst=True)
print("Мінімальне покриваюче дерево: ")
for u, v, weight in mst[1:]:
    sum_mst += weight
    l = len(f"({u}, {v}) -> {weight}")
    print(f"({u}, {v}) -> {weight}")
print(l * "-", end="\n\n")
print("+ {} - шлях нінімального дерева.".format(sum_mst))

print("Максимальне покриваюче дерево: ")
for u, v, weight in mst_worst[1:]:
    sum_mst_worst += weight
    l = len(f"({u}, {v}) -> {weight}")
    print(f"({u}, {v}) -> {weight}")
print(l * "-")
print("+ {} - шлях максимального дерева.".format(sum_mst_worst))