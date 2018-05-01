import numpy as np
import matplotlib.pyplot as plt
import random

##################################################
################  parameter_setting  #############
##################################################

font_legend = {'family' : 'Times New Roman','weight' : 'normal','size'   : 10,}
fontXY = {'family' : 'Times New Roman','weight' : 'normal','size'   : 20,}
plt.figure(figsize=[10,4])  #画布大小
plt.title('Vector Model')
plt.xlabel('ability_dimension',fontXY)
plt.ylabel('value',fontXY)


##################################################
################ ax_X setting  ###################
##################################################
x =[]
for i in range(10):
    x.append('ability%s'%(i+1))


##################################################
################ ax_y setting  ###################
##################################################
for j in range(5):
    y = []
    for i in range(10):
        y.append(random.uniform(0, 1))
    plt.plot(x, y,c ='gray',ls = 'dashed',lw=0.5,ms =3, marker = 'D')
plt.plot(x, y,label='y = cos(x)',c ='gray',ls = 'dashed',lw=0.5,ms =3, marker = 'D')

##################################################
################ ax_y_again setting  #############
##################################################
y = []
for i in range(10):
    y.append(random.uniform(0, 1))
plt.plot(x, y, label='y = cos(x)', c='red', ls='dashed', lw=1, ms=3, marker='D')

plt.legend(loc = 'upper right',prop=font_legend)   #绘制图例
plt.show()