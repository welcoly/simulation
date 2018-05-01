# encoding=utf-8

import numpy as np
import networkx as nx
from networkx import utils
import configparser
# import matplotlib.pyplot as plt
import random
import math
import time
import csv
from draw_class import *

# =================================================================
#                     parameters
# ==================================================================
conf_main = configparser.ConfigParser()
conf_main.read('conf_main.cfg')

worker_num = int(conf_main.items('Number_')[0][1])
worker_vector_switch = int(conf_main.items('Switch_')[0][1])

Requester_num = int(conf_main.items('Number_')[1][1])
Requester_vector_switch = int(conf_main.items('Switch_')[1][1])




# =================================================================
#                     Gen_Vector_For_Worker()
# ==================================================================
def Gen_Vector_For_Worker():
    worker_vector_List = []
    for worker_i in range(worker_num):
        worker_vector= []
        for i in range(10):
            worker_vector.append(random.uniform(0, 1))

        worker_vector_List.append(worker_vector)
    if worker_vector_switch == 1:
        print('========================worker_vector===========================')
        for i in range(worker_num):
            print(i)
            print(worker_vector_List[i])
        print('========================worker_vector===========================')

    return worker_vector_List

def Gen_Vector_For_Requester():
    Requester_vector_List = []
    for Requester_i in range(Requester_num):
        Requester_vector= []
        for i in range(10):
            Requester_vector.append(random.uniform(0, 1))

            Requester_vector_List.append(Requester_vector)
    if Requester_vector_switch == 1:
        print('========================Requester_vector===========================')
        for i in range(Requester_num):
            print(i)
            print(Requester_vector_List[i])
        print('========================Requester_vector===========================')

    return Requester_vector_List


if __name__ == '__main__':
    # worker_vector = Gen_Vector_For_Worker()
    # a = draw_class(worker_vector,2)   # the first parameter is value list;the second parameter is the dot size
    # a.draw()
    # requester_vector = Gen_Vector_For_Requester()
    # a = draw_class(requester_vector,2)   # the first parameter is value list;the second parameter is the dot size
    # a.draw()