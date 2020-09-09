from bs4 import BeautifulSoup
from selenium import webdriver as wd
import time
import re

#웹페이지 크롤링
def crawlPage(driver, url):
    driver.get(url)

    for _ in range(10):
        driver.execute_script("window.scrollTo(0, 999999999);") #스크롤 계속 내림
        time.sleep(3)

    html_source = driver.page_source

    return html_source

#크롤링한 데이터 파싱
def parsing(html_source):
    regExpView = re.compile('조회수 [0-9,]*회')
    data = []   #(동영상링크, 조회수) 저장
    bs = BeautifulSoup(html_source, "html.parser")  
    info = bs.find_all("a", attrs={'id':'video-title'}) #a태그중 id가 video-title인 태그 찾기

    for i in info:
        ret = regExpView.search(str(i)) #링크가져오기
        data.append(("https://www.youtube.com/" + i.get('href'), ret.group()))

    print(data)

if __name__ == '__main__':
    driver = wd.Chrome(executable_path="chromedriver.exe")
    subject = ["mozart", "bach"]

    for artist in subject:
        url = "https://www.youtube.com/results?search_query=" + artist
        html_source = crawlPage(driver, url)
        parsing(html_source)