import networkx as nx
import matplotlib.pyplot as plt

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

print(f"total stops: {G.number_of_nodes()}")
print(f"total connections: {G.number_of_edges()}")
print(f"is connected: {nx.is_connected(G)}")
print(f"average vertex degree: {sum(dict(G.degree()).values()) / G.number_of_nodes():.2f}")

start = 'Святошин'
end = 'Печерська'
shortest_path = nx.shortest_path(G, start, end, weight='weight')
path_length = nx.shortest_path_length(G, start, end, weight='weight')

print(f"\nshortest path from '{start}' to '{end}':")
print(" - ".join(shortest_path))
print(f"total weight (mins): {path_length}")

closeness = nx.closeness_centrality(G, distance='weight')
central = sorted(closeness.items(), key=lambda x: x[1], reverse=True)[:5]

print("\n5 central stations:")
for station, centrality in central:
    print(f"  {station}: {centrality:.4f}")

degree_dict = dict(G.degree())
hubs = sorted(degree_dict.items(), key=lambda x: x[1], reverse=True)[:5]

print("\nmost connected stations:")
for station, degree in hubs:
    print(f"  {station}: {degree} connections")

plt.figure(figsize=(16, 12))

pos = nx.spring_layout(G, k=2, iterations=50, seed=100)

red_edges = [(u, v) for u, v, d in G.edges(data=True) if d.get('line') == 'red']
blue_edges = [(u, v) for u, v, d in G.edges(data=True) if d.get('line') == 'blue']
green_edges = [(u, v) for u, v, d in G.edges(data=True) if d.get('line') == 'green']
transfer_edges = [(u, v) for u, v, d in G.edges(data=True) if d.get('line') == 'transfer']

nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='red', width=3, alpha=0.7, label='red line')
nx.draw_networkx_edges(G, pos, edgelist=blue_edges, edge_color='blue', width=3, alpha=0.7, label='blue line')
nx.draw_networkx_edges(G, pos, edgelist=green_edges, edge_color='green', width=3, alpha=0.7, label='green line')
nx.draw_networkx_edges(G, pos, edgelist=transfer_edges, edge_color='gray', width=2, style='dashed', alpha=0.5, label='transfers')

nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=300, edgecolors='black', linewidths=2)

nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold')

plt.title("Metro transport network", fontsize=16, fontweight='bold')
plt.legend(loc='upper left', fontsize=10)
plt.axis('off')
plt.tight_layout()
plt.show()
