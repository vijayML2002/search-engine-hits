def hits(graph, iteration):
    for i in range(iteration):
        hits_per_iteration(graph)

def hits_per_iteration(graph):
    for node in graph.nodes:
        node.update_hub_value()
        node.update_auth_value()
    graph.normalization()
