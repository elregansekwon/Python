from bs4 import BeautifulSoup
import requests
import korean_nouns

keyword = input("키워드 입력 >> ")
page_num = 1
total_nouns = []  # 최종 모든 명사 넣는 리스트
while True:
    url = f"https://www.joongang.co.kr/_CP/496?keyword={keyword}&sort%20=&pageItemId=439&page={page_num}"
    code = requests.get(url)
    soup = BeautifulSoup(code.text, "html.parser")
    title = soup.select("h2.headline a")
    if len(title) == 0: # 끝 페이지까지 크롤링 완료했으면?
        break
    for i in title:
        print("제목 :", i.text.strip())
        print("링크 :", i.attrs["href"])
        code_news = requests.get(i.attrs["href"])
        soup_news = BeautifulSoup(code_news.text, "html.parser")
        content = soup_news.select_one("div#article_body")
        result = content.text.strip().replace("     ", " ").replace("   ", "")
        nouns_list = korean_nouns.get_nouns_list(result)  #모듈.함수()
        total_nouns = total_nouns + nouns_list
        print(result)
        print()
    if page_num == 1:
        break
    page_num += 1

print(total_nouns)

# 단어 빈도수 카운트
from collections import Counter  # 보통 모듈 import 함수는 맨 위에 몰아 쓰는 것이 좋다.import

count_result = Counter(total_nouns)
print(count_result)

# 단어 구름
from  wordcloud import WordCloud #모듈 설치할 때 모듈 이름에 커서 놓고 Alt+Enter+Enter 치면 자동 설치

wc = WordCloud(font_path="NanumMyeongjoBold.ttf", background_color="white").generate_from_frequencies(count_result)

# 고화질로 저장하기 (svg 파일로 저장)
with open(f"wordcloud.svg","w",encoding="utf-8") as text_file:
    text_file.write(wc.to_svg())

# 단어 구름 이미지 화면에 띄우기
import  matplotlib.pyplot as plt #matplotlib: 그래프 관련 모듈

plt.figure() # 이미지 띄울 창 만들기
plt.imshow(wc, interpolation="bilinear") #창에 이미지 넣기 / 2번째 인자는 화질 개선
plt.axis("off")#그래프 관련된 모듈이라 xy축 관련이 뜨는데 그런 것 제거 명령
plt.show()#화면에 띄우기