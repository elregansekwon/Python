import requests
from bs4 import BeautifulSoup

# 서버에서 HTML코드 받아오기
code = requests.get("http://www.cgv.co.kr/movies/?lt=1&ft=0") #서버에 요청 메세지 보내기 -->"서버주소url"
# print(code.text)

# HTML 코드 이쁘게 정리하기
soup = BeautifulSoup(code.text, "html.parser") # 그냥 "html.parser"은 html을 예쁘게 정리하는 방법 중 하나이다.
# print(soup)

# 내가 원하는 요소 가져오게 하기
# 가져와야 되는 코드--> <strong class="title">서울의 봄</strong>
title = soup.select("strong.title") # 속성이 class인 건 .으로 표시하자
num = 1
for i in title:
    print(f"{num}위 : {i.text}") #.text : 요소의 내용 추출
    num += 1

#[CSS 선택자]
# 확인하는 법 : 개발자도구에 코드 찍으면 가운데에 CSS선택자 뜬다. / 괜찮은지 확인하는 법 : 아무 데나 클릭하고 crtl+F 누르면 검색창에 내가 생각한 CSS 선택자 써보면 알 수 있다.
# - 속성명 class : "."
# - 속성명 id : "#"
# - ~의 자손 : ">"
# - ~의 후손 : " " 공백

# bs4로 크롤링이 안되는 사이트는 selenium모듈을 공부하면 된다.