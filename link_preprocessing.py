import os
from utils import extraction
import pickle
from operator import itemgetter
from collections import OrderedDict

def subtract_list(li1, li2):
    return list(set(li2) - set(li1))

def save_labels():

    mpath = "code/data"
    filename = "label.pickle"

    label = {}

    for i,file in enumerate(os.listdir(mpath)):
        label[file] = i

    if(os.path.exists(filename)):
        os.remove(filename)

    with open(filename, 'wb') as handle:
        pickle.dump(label, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load_labels():
    filename = "label.pickle"
    file_to_read = open(filename, "rb")
    loaded_dictionary = pickle.load(file_to_read)
    return loaded_dictionary


def link_combinations(search_file):

    label_dictionary = load_labels()

    mpath = "code/data"
    links = []

    search_file_index = label_dictionary[search_file]

    e = extraction(mpath)

    for file in os.listdir(mpath):
        tags = e.href_tag(file)
        
        start_link = file
        start_index = label_dictionary[start_link]
        
        if(search_file_index != start_index):
            continue

        for destination_file in tags:
            destination_index = label_dictionary[destination_file]
            comb = [start_index, destination_index]
            links.append(comb)

    return links

def create_baseset(rootset):

    baseset_links = []

    for file in rootset:
        file_links = link_combinations(file)
        baseset_links.extend(file_links)

    return baseset_links

def extend_baseset(baseset):

    label_dictionary = load_labels()

    key_list = list(label_dictionary.keys())
    val_list = list(label_dictionary.values())

    main_node = []
    check_node = []
    files = []

    for link in baseset:
        main_node.append(link[0])
        check_node.append(link[1])

    new_main_node =  subtract_list(main_node, check_node)

    for node in new_main_node:
        position = val_list.index(node)
        files.append(key_list[position])

    more_baseset = create_baseset(files)

    baseset.extend(more_baseset)

    return baseset

def extend_baseset_to_n(baseset, n):
    for i in range(n):
        baseset = extend_baseset(baseset)
    return baseset

def store_link_details(links):

    link_filename = "graph.txt"

    if(os.path.exists(link_filename)):
        os.remove(link_filename)

    textfile = open(link_filename, "w")
    for element in links:
        textfile.write(str(element[0]) + "," + str(element[1]) + "\n")
    textfile.close()

def load_link_details():
    
    link_filename = "graph.txt"
    links = []
    
    with open(link_filename) as f:
        lines = f.readlines()   

    for line in lines:
        links.append(line.strip().split(","))

    return links


def get_sorted(X, Y):
    Z = [x for _,x in sorted(zip(Y,X))][::-1]
    return Z

def aggregate_ranks(data, rank_num):
    
    assert rank_num == 2
    
    rank_a = data[0]
    rank_b = data[1]
    
    score = {}

    value = len(rank_a)
    for rank_element in rank_a:
        if rank_element in score:
            score[rank_element] += value
        else:
            score[rank_element] = value
        value -= 1

    value = len(rank_b)
    for rank_element in rank_b:
        if rank_element in score:
            score[rank_element] += value
        else:
            score[rank_element] = value
        value -= 1

    sort_score = OrderedDict(sorted(score.items(), key=itemgetter(1)))
    return list(sort_score.keys())[::-1]
 










