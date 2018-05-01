import numpy as np
import matplotlib.pyplot as plt
import random


class draw_class(object):
    def __init__(self, worker_vector_list_,size_):
        self.worker_vector_list_ = worker_vector_list_
        self.size_=size_
        self.x =[]
    def draw(self):
        font_legend = {'family': 'Times New Roman', 'weight': 'normal', 'size': 10}
        fontXY = {'family': 'Times New Roman', 'weight': 'normal', 'size': 20}
        plt.figure(figsize=[10,4])  #画布大小
        plt.title('Vector Model')
        plt.xlabel('ability_dimension',fontXY)
        plt.ylabel('value',fontXY)
        for i in range(10):
            self.x.append('ability%s' % (i + 1))


        for j in range(len(self.worker_vector_list_)):
            plt.plot(self.x, self.worker_vector_list_[j],c ='gray',ls = 'dashed',lw=0.5,ms =self.size_, marker = 'D')
        plt.legend(loc = 'upper right',prop=font_legend)   #绘制图例
        plt.show()