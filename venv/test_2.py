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
