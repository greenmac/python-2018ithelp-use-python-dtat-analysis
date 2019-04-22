# https://ithelp.ithome.com.tw/articles/10196571
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

start = datetime.datetime(2016, 1, 1)
end = datetime.datetime(2017, 1, 1)

# 上面這邊引入了yahoo上"F"也就是Finance的資料，並給予要抓取的開始時間start與結束時間end
data = web.DataReader('F', 'yahoo', start, end)

plt.plot(data)
plt.show()