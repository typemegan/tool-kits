import pandas as pd
import sys
import os
from datetime import datetime

output = os.path.abspath(os.getcwd()) + "/output/" \
         + str(round(datetime.now().timestamp()*1000)) + ".csv"
print(output)

if not os.path.exists(os.path.dirname(output)):
    os.mkdir(os.path.dirname(output))

exfile = sys.argv[1]


# 👉 excel 转换成 csv
data = pd.read_excel(exfile)
# 👉 注意：如果要用到字段名，head必须为True， 比如下面调整字段顺序就用到了
data.to_csv(output, index=None, header=True)

# 调整csv数据
data = pd.read_csv(output)
# print(data.columns)  # 👉 获取字段列表
# print(len(data.columns))
df = pd.DataFrame(data)
# print(df.head(1))
# 👉 改变列/字段顺序，跟go的append一样，需要更新df
df = df.reindex(columns=['Content', 'Notes', 'Title', 'Author', 'Type', 'Created','Location','Page', 'Tags'])
print(df.head(1))
# 👉 保存df到新的csv文件，不要索引号，不要字段名
df.to_csv(os.path.expanduser("~") + "/Documents/out.csv", index=None, header=False)