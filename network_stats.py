import networkx as nx 

G = nx.DiGraph()

f = open('like.txt')

for line in f:
	edge = line.split(' ')
	G.add_edge(edge[0], edge[1])

print("Node degrees: ")
for node in G.nodes:
	print(node, ': ', G.degree(node), ' ', G.out_degree(node), ' ', G.in_degree(node))

print("Clustering: ", nx.clustering(G, G.nodes))
print("Page Rank: ", nx.pagerank(G))