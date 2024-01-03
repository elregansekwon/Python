from selenium import webdriver #selenium모듈: 자동 마우스 스크롤 가능
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)
browser.get("https://www.youtube.com/watch?v=_-ugbwhhApI")
time.sleep(3)

counts = {} # {위치값1 : 10, 위치값2 : 1, 위치값3 : 4, 위치값4 : 5, ....}
while True:
    ActionChains(browser).key_down(Keys.PAGE_DOWN).perform()
    cur_height = browser.execute_script("return document.documentElement.scrollTop")
    # print(cur_height)
    if cur_height in counts:
        counts[cur_height] += 1
    else:
        counts[cur_height] = 1
        # 어떤 숫자가 100회 나오면중단
    if counts[cur_height] >= 100:
        break

# 댓글 수집
comments = browser.find_elements(By.CSS_SELECTOR, "#content-text")
for i in comments:
    print(i.text.replace("\n", "").strip())
    print("-----------------------------------------")

# 결과를 DataFrame으로 저장
data = {"댓글": [i.text.replace("\n", "").strip() for i in comments]}
df = pd.DataFrame(data)

# 엑셀 파일로 저장
df.to_excel("유튜브댓글_수집결과.xlsx", index=False)
print("유튜브댓글_수집결과.xlsx 파일에 결과가 저장되었습니다.")

browser.close()