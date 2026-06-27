import numpy as np
import networkx as nx
import graphviz
import scipy.io as sio
import networkx as nx


MTX_FILE_NAME = 'Alemdar.mtx'

matrix = sio.mmread(MTX_FILE_NAME)

G = nx.from_scipy_sparse_array(matrix)

dot = nx.nx_agraph.to_agraph(G)
dot.graph_attr.update(overlap="false", splines="true")

sfdp_graph = graphviz.Source(dot.string(), format='png', engine='sfdp')

sfdp_graph.render('sfdp_matrix_output', view=True)