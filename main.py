import graphviz
import networkx as nx
import scipy.io as sio

from constant import MTX_FILE_NAME


matrix = sio.mmread(MTX_FILE_NAME)

G = nx.from_scipy_sparse_array(matrix)

dot = nx.nx_agraph.to_agraph(G)
dot.graph_attr.update(overlap="false", splines="true")

print('Number of edges: ', dot.number_of_edges())
print('Number of nodes: ', dot.number_of_nodes())

sfdp_graph = graphviz.Source(dot.string(), format='png', engine='sfdp')

sfdp_graph.render('sfdp_matrix_output', view=True)