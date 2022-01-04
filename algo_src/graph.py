import numpy as np

class Node:
    def __init__(self, name):
        self.name = name
        self.parents = []
        self.children = []
        self.hub_value = 1
        self.auth_value = 1

    def update_hub_value(self):
        new_hub_value = 0
        for node in self.children:
            new_hub_value += node.auth_value
        self.hub_value = new_hub_value
        
    def update_auth_value(self):
        new_auth_value = 0
        for node in self.parents:
            new_auth_value += node.hub_value
        self.auth_value = new_auth_value
        

    def child_linking(self, new_child):
        for node in self.children:
            if node.name == new_child.name:
                return None
        self.children.append(new_child)
    
    def parent_linking(self, new_parent):
        for node in self.parents:
            if node.name == new_parent.name:
                return None
        self.parents.append(new_parent)

class Graph:
    def __init__(self):
        self.nodes = []

    def exist(self, name):
        for each_node in self.nodes:
            if each_node.name == name:
                return True
        return False

    def find_node(self, name):
        if(self.exist(name)):
            return next(node for node in self.nodes if node.name == name)
        else:
            node = Node(name)
            self.nodes.append(node)
            return node

    def add_edge(self, parent, child):
        parent_node = self.find_node(parent)
        child_node = self.find_node(child)
        parent_node.child_linking(child_node)
        child_node.parent_linking(parent_node)

    def display_graph(self):
        for node in self.nodes:
            print("Node {} ----> {}".format(node.name, [child.name for child in node.children]))

    def display_hub_auth_values(self):
        for node in self.nodes:
            print("Node {} -- Hub_value {} -- Auth_value {}".format(node.name, node.hub_value, node.auth_value))    

    def sort_nodes(self):
        self.nodes.sort(key=lambda node : int(node.name))    

    def normalization(self):
        sum_auth = sum(node.auth_value for node in self.nodes)
        sum_hub = sum(node.hub_value for node in self.nodes)

        for node in self.nodes:
            node.auth_value = node.auth_value/sum_auth
            node.hub_value = node.hub_value/sum_hub

    def get_auth_list(self):
        auth_list = []
        for node in self.nodes:
            auth_list.append(round(node.auth_value,4))
        return auth_list

    def get_hub_list(self):
        hub_list = []
        for node in self.nodes:
            hub_list.append(round(node.hub_value,4))
        return hub_list

    def get_node_list(self):
        node_list = []
        for node in self.nodes:
            node_list.append(node.name)
        return node_list


        


                
    




    
    