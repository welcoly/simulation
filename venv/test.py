# encoding=utf-8

import numpy as np
import networkx as nx
from networkx import utils
import configparser
import matplotlib.pyplot as plt
import random
import math
import time
import csv

def calcu_len(dict_):
    count_  = 0
    for i in dict_:
        count_ +=1
    return count_



def CreateGraph(data):

    type=data[0][1]
    n=int(data[1][1])
    p=float(data[2][1])
    if data[3][1]=='None':
        seed=data[3][1]
    else:
        seed=int(data[3][1])
    k=int(data[4][1])
    m=int(data[5][1])

    if type=='er':
        G=nx.random_graphs.erdos_renyi_graph(n, 0.2, seed)

    elif type=='ws':
        G=nx.random_graphs.watts_strogatz_graph(n, 6, 0.3, seed)

    elif type=='ba':
        G=nx.random_graphs.barabasi_albert_graph(n, 2, seed)

    elif type=='regular':
        G=nx.random_graphs.barabasi_albert_graph(1, n, seed)

    return G


if __name__ == '__main__':
    conf = configparser.ConfigParser()
    conf.read('conf.cfg')
    G = CreateGraph(conf.items('Graph'))
    degree_dict ={}
    for i in G:
        t =G.neighbors(i)
        # print(t)  # <dict_keyiterator object at 0x000000A5BCF2E868>
        # print(calcu_len(t))
        degree_dict[calcu_len(t)] =0
    for i in G:
        t =G.neighbors(i)
        degree_dict[calcu_len(t)] +=1

    x = [0, 1]
    y = [0, 1]
    plt.figure()
    plt.plot(x, y)
    plt.show()

    # pos = nx.fruchterman_reingold_layout(G)
    # nx.draw(G,pos,node_size = 5)
    # plt.show()