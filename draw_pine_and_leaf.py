#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
pydot spine and leaf
@author: Diogo Montagner
"""
import pydot

graph = pydot.Dot(graph_type='graph', nodesep='.5', ranksep='.5', splines='false')
graph.set_node_defaults(shape='circle', fixedsize='true')

edge0 = pydot.Edge("SS0", "S0")
edge1 = pydot.Edge("SS0", "S1")
edge2 = pydot.Edge("SS1", "S0")
edge3 = pydot.Edge("SS1", "S1")

edge4 = pydot.Edge("SS0", "S2")
edge5 = pydot.Edge("SS0", "S3")
edge6 = pydot.Edge("SS1", "S2")
edge7 = pydot.Edge("SS1", "S3")

graph.add_edge(edge0)
graph.add_edge(edge1)
graph.add_edge(edge2)
graph.add_edge(edge3)
graph.add_edge(edge4)
graph.add_edge(edge5)
graph.add_edge(edge6)
graph.add_edge(edge7)

#
# Side A of spine
#

#edgel0a = pydot.Edge("S0", "LF0")
#edgel1a = pydot.Edge("S1", "LF0")
#edgel2a = pydot.Edge("S0", "LF1")
#edgel3a = pydot.Edge("S1", "LF1")
#edgel4a = pydot.Edge("S0", "LF2")
#edgel5a = pydot.Edge("S1", "LF2")
#edgel6a = pydot.Edge("S0", "LF3")
#edgel7a = pydot.Edge("S1", "LF3")

edgel0a = pydot.Edge("S0", "LF0")
edgel1a = pydot.Edge("S0", "LF1")
edgel2a = pydot.Edge("S0", "LF2")
edgel3a = pydot.Edge("S0", "LF3")
edgel4a = pydot.Edge("S1", "LF0")
edgel5a = pydot.Edge("S1", "LF1")
edgel6a = pydot.Edge("S1", "LF2")
edgel7a = pydot.Edge("S1", "LF3")

graph.add_edge(edgel0a)
graph.add_edge(edgel1a)
graph.add_edge(edgel2a)
graph.add_edge(edgel3a)
graph.add_edge(edgel4a)
graph.add_edge(edgel5a)
graph.add_edge(edgel6a)
graph.add_edge(edgel7a)

#
# Side B of spine
#

edgel0b = pydot.Edge("S2", "LF4")
edgel1b = pydot.Edge("S2", "LF5")
edgel2b = pydot.Edge("S2", "LF6")
edgel3b = pydot.Edge("S2", "LF7")
edgel4b = pydot.Edge("S3", "LF4")
edgel5b = pydot.Edge("S3", "LF5")
edgel6b = pydot.Edge("S3", "LF6")
edgel7b = pydot.Edge("S3", "LF7")

graph.add_edge(edgel0b)
graph.add_edge(edgel1b)
graph.add_edge(edgel2b)
graph.add_edge(edgel3b)
graph.add_edge(edgel4b)
graph.add_edge(edgel5b)
graph.add_edge(edgel6b)
graph.add_edge(edgel7b)

graph.write_png('spine_and_leaf.png')
