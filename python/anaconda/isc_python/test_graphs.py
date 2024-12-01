import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3])
print(G.nodes)
print(list(G.nodes))

H=nx.Graph()
H.add_node(4)
G.add_nodes_from(H)
print(G.nodes)

G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,4)
G.add_edge(4,1)
print(G.edges)


G.nodes[1]['Ville']='Paris'
G.nodes[2]['Ville']='Tunis'
G.nodes[3]['Ville']='New-York'
print(G.nodes[1])


G.edges[1,2]['Distance'] = 2000
print(G.edges[1,2])


C=nx.complete_graph(7)
nx.draw(C)
plt.show()
