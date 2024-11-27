from treelib import *

arb = Tree()
arb.create_node("Racine", "root")
arb.create_node("Noeud1", "node1", parent="root")
arb.create_node("Noeud2", "node2", parent="root")
arb.create_node("Noeud3", "node3", parent="root")
arb.create_node("Feuille1", "leaf1", parent="node1")
arb.create_node("Feuille2", "leaf2", parent="node1")

arb.show()
