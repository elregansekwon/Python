import requests
from bs4 import BeautifulSoup
import pandas as pd

keyword = input("검색하고 싶은 키워드를 입력하세요 >>")
code = requests.get(f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={keyword}") # html 가져오기
soup = BeautifulSoup(code.text, "html.parser") # html코드 예쁘게 정리
result = soup.select("a.keyword>div.tit") # css연산자로 요소내용 가져오기 / 보모나 조부모 활용해서 겹치는 css연산자 가지고 있는 애들 걸러내기
# 가져와야되는 요소 : <div class="tit">파이썬 자격증</div> --> 그 부모 <a class="keyword" href=>어쩌고
for i in result:
    print(i.text)

# 엑셀에 검색 결과 저장하기
results_list = [i.text for i in result]
df = pd.DataFrame(results_list, columns=['검색결과'])
excel_filename = f"{keyword}_검색결과.xlsx"
df.to_excel(excel_filename, index=False)
print(f"검색 결과가 {excel_filename} 파일로 저장되었습니다.")