from utils import extraction
import os, re
from similarity import cos_similarity
from link_preprocessing import create_baseset, extend_baseset 
from link_preprocessing import extend_baseset_to_n, store_link_details
from pickle import load
from algo_src.graph import Graph
from link_preprocessing import get_sorted, load_link_details
from link_preprocessing import aggregate_ranks
from algo_src.hits_algorithm import hits
from link_preprocessing import load_labels

def get_html_data(file_list):
    pathname = "code/data"

    title = []
    text = []
    filenames = []

    ex = extraction(pathname)

    for file in file_list:
        t, x = ex.title_and_data(file)
        x = x[:800] + "..."
        title.append(t)
        text.append(x)
        filenames.append(file)

    return title, text, filenames

def keyword_recommendation(keyword):
    mpath = "code/data"
    rank = []
    cosine_value = []
    final_rank = []

    c = cos_similarity(mpath)
    crank = c.csim(keyword, 5)
    c.close()
    
    for data in crank:
        rank.append(data[0])
        cosine_value.append(data[1])

    """
    bset = create_baseset(rank)
    new_bset = extend_baseset_to_n(bset,1)
    store_link_details(new_bset)    

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

    sorted_hub = get_sorted(node, hub)
    sorted_auth = get_sorted(node, auth)

    node_ranking = aggregate_ranks([sorted_hub, sorted_auth], 2)   

    label = load_labels()

    key_list = list(label.keys())
    val_list = list(label.values())

    for node in node_ranking:
        position = val_list.index(int(node))
        final_rank.append(key_list[position])
    """
    final_rank = rank

    return final_rank, cosine_value

