import requests
from bs4 import BeautifulSoup
import numpy as np
import re
import matplotlib.pyplot as plt
import matplotlib

number = {}
list = ['2019-nCoV', 'Mers-Cov-2', 'the+COVID-19+virus', 'nCov-2019', 'Wuhan+Coronavirus']
for i in range(5):
    try:
        requests.adapters.DEFAULT_RETRIES = 5
        r = requests.get('https://www.nytimes.com/search', params={'query': list[i]})
        # print(r.url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        demo = r.text
        # print(demo)
        soup = BeautifulSoup(demo, 'lxml')
        s = soup.select('.css-qmql6p p')
        S = str(s)
        S = S.replace(",", "")
        a = re.findall(r'(\w*[0-9]+)\w*', S)
        number[i] = int(a[0])
        # print(re.match(r'^\d', content))S
        for j in range(9):
            Str = soup.select('.css-e1lvw9 a')[j]['href']
            url = 'https://www.nytimes.com' + Str
            print(url)
            webpage = requests.get(url)
            list[i].replace("+", " ")
            name = (list[i], str(j))
            emm = '-'
            N = emm.join(name)
            print(N)
            f = open(N+".txt",'w')
            f.writelines(webpage.text)
            f.close()

    except:
        print('异常')

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
matplotlib.rcParams['axes.unicode_minus'] = False
num = np.array([number[0], number[1], number[2], number[3], number[4]])
"""
绘制水平条形图方法barh
参数一：y轴
参数二：x轴
"""
plt.barh(range(5), num, height=0.7, color='steelblue', alpha=0.8)  # 从下往上画
plt.yticks(range(5), ['2019-nCoV', 'Mers-Cov-2', 'the COVID-19 virus', 'nCov-2019',  'Wuhan Coronavirus'])
plt.xlim(1500, 40000)
plt.xlabel("数量")
plt.title("纽约时报病毒名称数量统计")
plt.show()
print(number)
