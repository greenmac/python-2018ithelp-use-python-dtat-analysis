# https://ithelp.ithome.com.tw/articles/10194027
import pandas as pd
import numpy as np

"""
fortune1000
"""
# fortune = pd.read_csv('fortune1000-final.csv', encoding = 'unicode_escape', index_col='Rank')
# sector = fortune.groupby('Sector')
# sector.get_group('Energy')
# print(sector.get_group('Energy').head())

"""
example01
"""
col = ['class','name','hbd']
data = [['class0', 'user0', '1993-10-01'],
        ['class0', 'user1', '1992-10-02'],
        ['class1', 'user2', '1990-10-01'],
        ['class2', 'user3', '1983-10-03'],
        ['class1', 'user4', '1991-10-02'],
        ['class0', 'user5', '2001-10-03']]
frame = pd.DataFrame(data,columns=col)
frame_class = frame.groupby('class')

# print(frame_class.groups)
# {
#     'class0': Int64Index([0, 1, 5], dtype='int64'), 
#     'class1': Int64Index([2, 4], dtype='int64'), 
#     'class2': Int64Index([3], dtype='int64')
# }

# print(frame_class.get_group('class1'))

"""
example02
"""
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                      'foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})
# print(df)

# print(df.groupby('A').sum())
#             C         D
# A                      
# bar  1.084385 -0.315260
# foo  2.379708 -1.140547

print(df.groupby(['A', 'B']).sum())
#                   C         D
# A   B                        
# bar one   -0.920197  0.585847
#     three  0.832764 -0.630151
#     two    1.715080 -1.006039
# foo one    0.414989 -0.484931
#     three  0.753149 -0.395930
#     two   -1.614265  2.092886