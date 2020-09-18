from bs4 import BeautifulSoup
from selenium import webdriver as wd
import time
import re
import pandas as pd

#csv로 저장
def savaToCSV(data, filename="no_name.csv"):
    column_name = ["링크", "좋아요", "싫어요", "조회수"]
    dataFrame = pd.DataFrame(data, columns=column_name)
    dataFrame.to_csv(filename,
                     header=True,
                     na_rep="0")

#웹페이지 크롤링
def crawlPage(driver, url):
    driver.get(url)

    for _ in range(10):
        driver.execute_script("window.scrollTo(0, 999999999);") #스크롤 계속 내림
        time.sleep(2.5)

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
        url = "https://www.youtube.com/" + i.get('href')    #동영상 주소
        #좋아요 싫어요 가져오기
        like, dislike = parsingLikeDislike(url)
        data.append((url, like, dislike, ret.group()))  #링크, 좋아요, 싫어요, 조회수

    return data

#좋아요 싫어요 파싱
def parsingLikeDislike(url):
    driver = wd.Chrome(executable_path="chromedriver.exe")
    driver.get(url)
    html_source = driver.page_source
    bs = BeautifulSoup(html_source, "html.parser")
    info = bs.find_all("script")    #자바스크립트에 있는 값 긁었음
    
    for i in info:
        likeCount = 0
        dislikeCount = 0
        regExpView = re.compile('좋아요 [0-9,]*개')
        ret = regExpView.search(str(i))  # 링크가져오기
        if ret:
            likeCount = ret.group()[4:-1]   #"좋아요 12,123개"에서 숫자만 나오게
            break
            
    for i in info:
        regExpView = re.compile('싫어요 [0-9,]*개')
        ret = regExpView.search(str(i))  # 링크가져오기
        if ret:
            dislikeCount = ret.group()[4:-1]    #"싫어요 12,123개"에서 숫자만 나오게
            break

    driver.quit()
    return likeCount, dislikeCount  #좋아요, 싫어요 개수 반환

if __name__ == '__main__':
    driver = wd.Chrome(executable_path="chromedriver.exe")
    subject = ["mozart", "bach"]

    for artist in subject:
        url = "https://www.youtube.com/results?search_query=" + artist
        html_source = crawlPage(driver, url)
        data = parsing(html_source)
        savaToCSV(data, artist + ".csv")