# https://ithelp.ithome.com.tw/articles/10196410
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""
example01
"""
# labels = ['A', 'B', 'C', 'D', 'E', 'F']
# size = [33, 52, 12, 17, 62, 48]

# separated = (.1,0,0,0,0,0)

# plt.pie(size, labels=labels, autopct='%1.1f%%' ,explode=separated) # autopct='%1.1f%%'是用來顯示百分比
# plt.axis('equal')

# plt.show()

"""
example02
"""
# data = {'names':['a','b','c','d','e'],
#         'jan':[133,122,101,104,320],
#         'feb':[122,132,144,98,62],
#         'march':[64,99,32,12,65]}

# df = pd.DataFrame(data, columns=['names', 'jan', 'feb', 'march'])
# df['total'] = df['jan'] + df['feb'] + df['march']
# colors = [(1,.4,.4),(1,.6,1),(.5,.3,1),(.7,.7,.2),(.6,.2,.6)]

# plt.pie( df['total'] ,
#     labels = df['names'],
#     colors = colors,
#     autopct='%1.1f%%',
#     ) 

# plt.axis('equal') # 等比例
# plt.show()

"""
Bar Chart
"""
col_count = 3
bar_width = 0.2
index = np.arange(col_count)
A_scores = (553,536,548)
B_scores = (518,523,523)
C_scores = (613,570,588)
D_scores = (475,505,499)

A = plt.bar(index, A_scores, bar_width, alpha=.4, label="K") 
B = plt.bar(index+0.2, B_scores, bar_width, alpha=.4, label="C") 
C = plt.bar(index+0.4, C_scores, bar_width, alpha=.4, label="N") # x,y ,width
D = plt.bar(index+0.6, D_scores, bar_width, alpha=.4, label="F") # x,y ,width

def createLabels(data):
    for item in data:
        height = item.get_height()
        plt.text(
            item.get_x()+item.get_width()/2., 
            height*1.05, 
            '%d' % int(height),
            ha = "center",
            va = "bottom",
        )
createLabels(A)
createLabels(B)
createLabels(C)
createLabels(D)

plt.ylabel("Mean score")
plt.xlabel("Subject")
plt.title("Test Scores by Contry")
plt.xticks(index+.3 / 2 ,("Math","Reading","Science")) # plt.xticks為底下的文字（為了至中所以+.3 / 2）
plt.legend() # plt.legend()為右上角的圖。
plt.grid(True)
plt.show()