import networkx as nx
import sqlite3

conn = sqlite3.connect("me.db")
gr = nx.Graph()
c = conn.cursor()

for row in c.execute('SELECT * FROM edges'):
    gr.add_edge(row[0], row[1])

conn.commit()
conn.close()

print("Количество узлов", gr.number_of_nodes())
print("Количество граней", gr.number_of_edges())

degrees = nx.degree(gr)


print("Средняя cтепень вершины", sum(degrees.values()) / len(degrees))
print("Средний коэф собственной центральности", sum(nx.eigenvector_centrality(gr).values())/ len(nx.eigenvector_centrality(gr)))


print ("Средняя минимальная длина пути", nx.average_shortest_path_length (gr) )

print("Кластерный коэффициент ", nx.average_clustering(gr))


# С глубиной 20
# Количество узлов 9980
# Количество граней 450712
# Средняя cтепень вершины 90.32304609218437
# Средний коэф собственной центральности 0.003115173885015206
# Средняя минимальная длина пути 3.36771988711364
# Кластерный коэффициент  0.40743904918722357