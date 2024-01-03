from bs4 import BeautifulSoup
import requests
import korean_nouns

keyword = input("키워드 입력 >> ")
page_num = 1
dataset = [] #큰 장바구니
while True:
    url = f"https://www.joongang.co.kr/_CP/496?keyword={keyword}&sort%20=&pageItemId=439&page={page_num}"
    code = requests.get(url)
    soup = BeautifulSoup(code.text, "html.parser")
    title = soup.select("h2.headline a")
    if len(title) == 0: # 끝 페이지까지 크롤링 완료했으면?
        break
    for i in title:
        result = i.text.strip()
        print("제목 :", result)
        nouns_list = korean_nouns.get_nouns_list(result) #명사 추출 --> nouns_list에 저장 / ["명사1","명사2",...]
        dataset.append(nouns_list)
    if page_num ==5:
        break

    page_num += 1

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
df_apr = apriori(df, use_colnames=True, min_support=0.01) #apr 함수가 support값이 0.5인 것만 추출하게 원래 되어있음-->min_support 이용해서 값 조정하기
print(df_apr)

# itemsets가 두개짜리인 것들만 걸러내기
df_apr["length"] = df_apr["itemsets"].str.len()
df_apr = df_apr[df_apr["length"]==2]
df_apr["itemsets"] = df_apr["itemsets"].apply(lambda x:list(x))
df_apr["source"] = df_apr["itemsets"].str[0]
df_apr["target"] = df_apr["itemsets"].str[1]
print(df_apr)

# 연관분석 시각화
import networkx as nx
from pyvis.network import Network
import os
import webbrowser
import platform
import urllib.parse as par

G = nx.from_pandas_edgelist(df_apr, source="source", target="target", edge_attr="support")
net = Network(height="1000px", width="1500px")
net.from_nx(G)
net.show_buttons(filter_=["physics"])
net.save_graph("./network.html")

ap = os.path.abspath("./network.html")
if platform.system() == "Windows":
    webbrowser.open('file:///' + ap.replace('\\', '/')) # 윈도우
else:
    webbrowser.open("file://" + ap) # 맥

