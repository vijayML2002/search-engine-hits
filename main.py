
from similarity import cos_similarity
from link_preprocessing import create_baseset, extend_baseset 
from link_preprocessing import extend_baseset_to_n, store_link_details

mpath = "code/data"
c = cos_similarity(mpath)

keyword = input("Enter Keyword : ")
crank = c.csim(keyword, 5)

rootset = []

for i,cl in enumerate(crank):
    rootset.append(cl[0])
    print("{} {}".format(i+1, cl))

"""

bset = create_baseset(rootset)

new_bset = extend_baseset_to_n(bset,1)

store_link_details(new_bset)
    
c.close()

from pickle import load
from algo_src.graph import Graph
from link_preprocessing import get_sorted, load_link_details
from link_preprocessing import aggregate_ranks
from algo_src.hits_algorithm import hits
from link_preprocessing import load_labels

links = load_link_details()

egraph = Graph()

for each_link in links:
    parent = each_link[0]
    child = each_link[1]
    egraph.add_edge(parent, child)

egraph.sort_nodes()

hits(egraph, 20)

hub = egraph.get_hub_list()
auth = egraph.get_auth_list()
node = egraph.get_node_list()

print("Node - {}".format(node))
print("Hub - {}".format(hub))
print("Auth - {}".format(auth))


sorted_hub = get_sorted(node, hub)
sorted_auth = get_sorted(node, auth)

print("Sorted hub - {}".format(sorted_hub))
print("Sorted auth - {}".format(sorted_auth))

node_ranking = aggregate_ranks([sorted_hub, sorted_auth], 2)   

label = load_labels()

key_list = list(label.keys())
val_list = list(label.values())

for node in node_ranking:
    position = val_list.index(int(node))
    print("{} - {}".format(int(node), key_list[position]))
"""