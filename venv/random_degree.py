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

conf1 = configparser.ConfigParser()
conf1.read('conf1.cfg')
netizenNum = int(conf1.items('Netizen')[0][1])
sourceNum = int(conf1.items('Source')[0][1])
NodeNum = netizenNum
DoNum = int(conf1.items('Expriment')[0][1])  # 跑的次数
Source_knowledge_switch = int(conf1.items('Switch')[0][1])  # 是否显示 Source_knowledge
Source_location_switch = int(conf1.items('Switch')[1][1])  # 是否显示 Source_location
netizen_temp_switch = int(conf1.items('Switch')[2][1])  # 是否显示 netizen_temp 状态
netizen_SearchRadius_switch = int(conf1.items('Switch')[3][1])  # 是否显示 netizen_SearceRadius
netizen_knowledge_switch = int(conf1.items('Switch')[4][1])  # 是否显示 netizen_knowledge
netizen_location_switch = int(conf1.items('Switch')[5][1])  # 是否显示 netizen_location
soueceList_switch = int(conf1.items('Switch')[6][1])  # 是否在信息源集成后显示信息源信息
netizen_switch = int(conf1.items('Switch')[7][1])  # 是否在网民集成后显示网民信息
environment_Length = int(conf1.items('Expriment')[1][1])  # 环境边长
search_radius_mu_devide_environment_length = float(conf1.items('Netizen')[1][1])  # 网民搜索半径对于环境边长的比例
step_length_devide_environment_length = float(conf1.items('Netizen')[2][1])  # 网民步长对于环境边长的比例


# =================================================================
#                    Gen_konwledge_For_Source()
# ========================================================== ========
def Modified_Gen_konwledge_For_Source():
    source_konwledge_List = []
    for source_i in range(sourceNum):
        source_konwledge = []
        for i in range(10):
            if i == (source_i % 10):
                source_konwledge.append(1)
            else:
                source_konwledge.append(0)
        source_konwledge_List.append(source_konwledge)
    return source_konwledge_List


# =================================================================
#                     Gen_location_For_Source()
# ==================================================================
def Gen_location_For_source():
    source_location_List = []
    for source_i in range(sourceNum):
        source_location = []
        for i in range(2):
            randomNum = random.uniform(0, environment_Length)
            source_location.append(randomNum)
        source_location_List.append(source_location)
    if Source_location_switch == 0:
        print('========================为信息源设定初始位置===========================')
        for i in range(sourceNum):
            # print i, '**************'
            print(source_location_List[i])
        print('========================为信息源设定初始位置===========================')
        print
    return source_location_List


    # =================================================================


#                     Gen_temp_For_Netizen()
# ==================================================================
def Gen_temp_For_Netizen():
    netizen_temp_List = []
    for netizen_i in range(netizenNum):
        netizen_temp_knowledge = []
        for i in range(10):
            # 产生十个零
            initial_Num = 0
            netizen_temp_knowledge.append(initial_Num)
        netizen_temp_List.append(netizen_temp_knowledge)
    if netizen_temp_switch == 1:
        print('========================为网民影子知情度设定背景===========================')
        print(netizen_temp_List[0])
        print('========================为网民影子知情度设定背景===========================')
        print
    return netizen_temp_List


# =================================================================
#                     Gen_SearchRadius_For_Netizen()
# ==================================================================
def Gen_SearchRadius_For_Netizen():
    netizen_SearchRadius_List = []
    for netizen_i in range(netizenNum):
        netizen_SearchRadius = search_radius_mu_devide_environment_length * environment_Length
        netizen_SearchRadius_List.append(netizen_SearchRadius)
    if netizen_SearchRadius_switch == 1:
        print('========================为网民搜索半径设定===========================')
        for i in range(20):
            print(netizen_SearchRadius_List[i])
        print('========================为网民搜索半径设定===========================')
        print
    return netizen_SearchRadius_List


# =================================================================
#                     Gen_location_For_Netizen()
# ==================================================================
def Gen_location_For_Netizen():
    netizen_location_List = []
    for netizen_i in range(netizenNum):
        netizen_location = []
        for i in range(2):
            randomNum = random.uniform(0, environment_Length)
            netizen_location.append(randomNum)
        netizen_location_List.append(netizen_location)
    if netizen_location_switch == 1:
        print('========================为网民设定初始位置===========================')
        for i in range(20):
            print(netizen_location_List[i])
        print('========================为网民设定初始位置===========================')
        print
    return netizen_location_List


# =================================================================
#                     Gen_konwledge_For_Netizen()
# ==================================================================
def Gen_konwledge_For_Netizen():
    netizen_knowledge_List = []
    for netizen_i in range(netizenNum):
        netizen_knowledge = []
        for i in range(10):
            # 产生八个零
            initial_Num = 0
            netizen_knowledge.append(initial_Num)
        netizen_knowledge_List.append(netizen_knowledge)
    if netizen_knowledge_switch == 1:
        print('========================为网民知情度设定背景===========================')
        print(netizen_knowledge_List[0])
        print('========================为网民知情度设定背景===========================')
        print
    return netizen_knowledge_List


# =================================================================
#                            CreateGraph（）
# ==================================================================
def CreateGraph(i): #产生一个随机网络
    n=500 # p为网络节点
    link = i + 0.0
    p=link / n#p为节点之间的链接概率
    G = nx.random_graphs.erdos_renyi_graph(n, p)
    return G


# =================================================================
#               netizensMove（）
# ==================================================================
def netizensMove(G_):
    a = random.SystemRandom()
    move_angle = range(0, 360, 1)
    for i, node in enumerate(G_.node):
        randomNum = a.sample(move_angle, 1)[0]
        G_.node[i]['location'][0] += step_length_devide_environment_length * environment_Length * math.cos(randomNum)
        G_.node[i]['location'][1] += step_length_devide_environment_length * environment_Length * math.sin(randomNum)
    return 0


# =================================================================
#               getTotalKnowledge（）
# ==================================================================
def getTotalKnowledge_for_everyNode(G_):
    for i, node in enumerate(G_.node):
        G_.node[i]['totalKnowledge'] = 0
        for j in range(10):
            G_.node[i]['totalKnowledge'] += G_.node[i]['knowledge'][j]
    return 0


# =================================================================
#                   get_knowledge()
# ==================================================================
def get_knowledge(node, source):
    for i in range(10):
        if source[1][i] == 1:
            node['knowledge'][i] = 1
        else:
            pass
    return 0


# =================================================================
#                   distance（）
# ==================================================================
def distance(node, source):
    x = node['location'][0] - source[0][0]
    y = node['location'][1] - source[0][1]
    distance_ = float(math.sqrt(x * x + y * y))
    return distance_


# =================================================================
#                  netizens_Search（）
# ==================================================================
def netizens_Search(G_, sourceList_, netizenNum_, sourceNum_):
    for i in range(netizenNum_):
        for j in range(sourceNum_):
            if distance(G_.node[i], sourceList_[j]) <= G_.node[i]['search_radius']:
                get_knowledge(G_.node[i], sourceList_[j])
            else:
                pass



# =================================================================
#                  max_netizens_Total_knowledge（）
# ==================================================================
def max_netizens_Total_knowledge(G_):
    max_total_knowledge = 0
    for node in G_.node:
        if max_total_knowledge <= G_.node[node]['totalKnowledge']:
            max_total_knowledge = G_.node[node]['totalKnowledge']
        else:
            pass
    return max_total_knowledge


# 线上交流
def Online_Spread(G_):
    for node in G_.node:
        for i in G_.neighbors(node):
            for j in range(10):
                if G_.node[i]['knowledge'][j] == 1:
                    G_.node[node]['temp'][j] = 1
                else:
                    pass

    for node in G_.node:
        for i_ in range(10):
            if G_.node[node]['temp'][i_] == 1:
                G_.node[node]['knowledge'][i_] = 1
            else:
                pass

    for j in G_.node:
        for k in range(10):
            G_.node[j]['temp'][k] = 0
    return 0


# 打印所有网民属性
def printNetizens(G_):
    print( '============================these are netizens===============================')
    for node in G_.node:
        print (node)
        print (G_.node[node])
        print (G_.neighbors(node))
        print ('***')
    print ('============================these are netizens===============================')
    return 0


# 打印所有信息源属性
def printSources(sourceList_, sourceNum_):
    print ('============================these are sources===============================')
    for source in range(sourceNum_):
        print (source)
        print (sourceList_[source])
    print ('============================these are sources================================')


# 网民属性集成
def wangminjicheng(G_, netizen_knowledge_, netizen_location_, netizen_temp_knowledge_, netizen_search_radius_):
    for i, node in enumerate(G_.node):
        G_.node[i]['knowledge'] = netizen_knowledge_[i]
        G_.node[i]['totalKnowledge'] = 0
        G_.node[i]['location'] = netizen_location_[i]
        G_.node[i]['temp'] = netizen_temp_knowledge_[i]
        G_.node[i]['search_radius'] = netizen_search_radius_[i]
    return 0


# 信息源属性集成
def xinxiyuanjicheng(sourceList_, source_location_, source_knowledge_, sourceNum_):
    for j in range(sourceNum_):
        source = []
        source.append(source_location_[j])
        source.append(source_knowledge_[j])
        sourceList_.append(source)
    return 0


# =================================================================
#                            主程序入口
# ==================================================================
if __name__ == '__main__':
    print ('=============================================================')
    print ('============= start the simulation of CI ====================')
    print ('=============================================================')
    print ('initializing......')

    for degree_ in range(2, 20,2):
        totaltime_degree = 0.0

        for donum in range(DoNum):
            # 生成网络
            G = CreateGraph(degree_)
            # 初始化网民知情度背景
            netizen_knowledge = Gen_konwledge_For_Netizen()
            # 初始化网民初始位置
            netizen_location = Gen_location_For_Netizen()
            # 初始化网民影子初始知情度
            netizen_temp_knowledge = Gen_temp_For_Netizen()
            # 初始化网民搜索半径
            netizen_search_radius = Gen_SearchRadius_For_Netizen()
            # 初始化信息源初始位置
            source_location = Gen_location_For_source()
            # 初始化信息源信息
            source_knowledge = Modified_Gen_konwledge_For_Source()
            # 网民属性集成
            wangminjicheng(G, netizen_knowledge, netizen_location, netizen_temp_knowledge, netizen_search_radius)
            if netizen_switch == 1:
                printNetizens(G)
                # 信息源属性集成
            sourceList = []
            xinxiyuanjicheng(sourceList, source_location, source_knowledge, sourceNum)
            if soueceList_switch == 1:
                printSources(sourceList, sourceNum)

            time = 0.0
            while 1:
                max_knowledge = max_netizens_Total_knowledge(G)
                max_knowledge_before = max_knowledge
                netizens_Search(G, sourceList, netizenNum, sourceNum)
                Online_Spread(G)
                getTotalKnowledge_for_everyNode(G)
                netizensMove(G)
                time += 1
                print( 'time', time)
                print( 'doNum', donum)
                # print( 'degree', degree_)
                # print ('total_time', totaltime_)
                print ('DoNum', DoNum)
                print ('degree:',degree_)
                print( '------------------------------------')
                max_knowledge = max_netizens_Total_knowledge(G)
                print (max_knowledge)
                if max_knowledge > max_knowledge_before:
                    print ('max_knowledge_increase')
                    print  (max_knowledge)
                    print (degree_)
                    result_line = '%d,%d,%d' % (max_knowledge, time, degree_)
                    ratefile = open('random_degree.csv', 'a')
                    ratefile.write(result_line + '\n')

                if netizen_switch == 1:
                    printNetizens(G)
                    # print max_netizens_Total_knowledge(G)
                if max_knowledge == 8:
                    totaltime_degree += time
                    for node in G.node:
                        print ('netizen:', node)
                        print ('location:', G.node[node]['location'])
                        print ('knowledge:', G.node[node]['knowledge'])
                        print ('totalKnowledge:', G.node[node]['totalKnowledge'])
                    print ('complete search')
                    print (donum)
                    result_line = '**********%d' % donum
                    ratefile = open('random_degree.csv', 'a')
                    ratefile.write(result_line + '\n')
                    break
        totaltime_degree = totaltime_degree/DoNum
        result_line = '%d,%d' % (degree_ ,totaltime_degree)
        ratefile = open('random_degree_totaltime.csv', 'a')
        ratefile.write(result_line + '\n')


