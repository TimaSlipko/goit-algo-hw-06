import networkx as nx
from dfs import dfs
from bfs import bfs

G = nx.Graph()

red_line = [
    ('Академмістечко', 'Житомирська', 3),
    ('Житомирська', 'Святошин', 2),
    ('Святошин', 'Нивки', 2),
    ('Нивки', 'Берестейська', 2),
    ('Берестейська', 'Шулявська', 2),
    ('Шулявська', 'Політехнічний інститут', 2),
    ('Політехнічний інститут', 'Вокзальна', 2),
    ('Вокзальна', 'Університет', 1),
    ('Університет', 'Театральна', 1),
    ('Театральна', 'Хрещатик', 1),
    ('Хрещатик', 'Арсенальна', 2),
    ('Арсенальна', 'Дніпро', 2),
    ('Дніпро', 'Гідропарк', 2),
    ('Гідропарк', 'Лівобережна', 3),
    ('Лівобережна', 'Дарниця', 2),
    ('Дарниця', 'Чернігівська', 2),
    ('Чернігівська', 'Лісова', 2),
]

blue_line = [
    ('Героїв Дніпра', 'Мінська', 2),
    ('Мінська', 'Оболонь', 2),
    ('Оболонь', 'Петрівка', 2),
    ('Петрівка', 'Тараса Шевченка', 2),
    ('Тараса Шевченка', 'Контрактова площа', 2),
    ('Контрактова площа', 'Поштова площа', 1),
    ('Поштова площа', 'Майдан Незалежності', 1),
    ('Майдан Незалежності', 'Площа Льва Толстого', 2),
    ('Площа Льва Толстого', 'Олімпійська', 2),
    ('Олімпійська', 'Палац "Україна"', 1),
    ('Палац "Україна"', 'Либідська', 2),
    ('Либідська', 'Деміївська', 2),
    ('Деміївська', 'Голосіївська', 2),
    ('Голосіївська', 'Васильківська', 2),
    ('Васильківська', 'Виставковий центр', 2),
    ('Виставковий центр', 'Іподром', 2),
    ('Іподром', 'Теремки', 3),
]

green_line = [
    ('Сирець', 'Дорогожичі', 2),
    ('Дорогожичі', 'Лук\'янівська', 2),
    ('Лук\'янівська', 'Золоті ворота', 2),
    ('Золоті ворота', 'Палац спорту', 1),
    ('Палац спорту', 'Кловська', 2),
    ('Кловська', 'Печерська', 2),
    ('Печерська', 'Дружби народів', 2),
    ('Дружби народів', 'Видубичі', 2),
    ('Видубичі', 'Славутич', 2),
    ('Славутич', 'Осокорки', 3),
    ('Осокорки', 'Позняки', 2),
    ('Позняки', 'Харківська',2),
    ('Харківська', 'Вирлиця', 1),
    ('Вирлиця', 'Бориспільська', 2),
    ('Бориспільська', 'Червоний Хутір', 2),
]

for station1, station2, time in red_line:
    G.add_edge(station1, station2, weight=time, line='red')

for station1, station2, time in blue_line:
    G.add_edge(station1, station2, weight=time, line='blue')

for station1, station2, time in green_line:
    G.add_edge(station1, station2, weight=time, line='green')

transfers = [
    ('Театральна', 'Золоті ворота', 3),
    ('Хрещатик', 'Майдан Незалежності', 2),
    ('Палац спорту', 'Площа Льва Толстого', 3),
]

for station1, station2, time in transfers:
    G.add_edge(station1, station2, weight=time, line='transfer')


def calculate_cost(graph, path):
    if not path or len(path) < 2:
        return 0
    return sum(graph[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))

def compare_algorithms(graph, start, goal):
    print(f"\nroute: {start} - {goal}")
    
    dfs_result, dfs_visited = dfs(graph, start, goal)
    dfs_cost = calculate_cost(graph, dfs_result) if dfs_result else None
    
    bfs_result, bfs_visited = bfs(graph, start, goal)
    bfs_cost = calculate_cost(graph, bfs_result) if bfs_result else None
    
    if dfs_result:
        print(f"{'DFS'} {' - '.join(dfs_result)}")
    print(f"{len(dfs_result)} stops, {dfs_cost} mins, {dfs_visited} nodes visited")
    
    print("\n")

    if bfs_result:
        print(f"{'BFS'} {' - '.join(bfs_result)}")    
    print(f"{len(bfs_result)} stops, {bfs_cost} mins, {bfs_visited} nodes visited")

def main():
    test_routes = [
        ('Академмістечко', 'Осокорки'),
        ('Героїв Дніпра', 'Лівобережна'),
        ('Сирець', 'Васильківська'),
    ]

    for start, goal in test_routes:
        compare_algorithms(G, start, goal)

if __name__ == '__main__':
    main()
