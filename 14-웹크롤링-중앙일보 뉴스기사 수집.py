from bs4 import BeautifulSoup
import requests

keyword = input("키워드 입력 >> ")
page_num = 1
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
        print(result)
        print()
    page_num += 1
