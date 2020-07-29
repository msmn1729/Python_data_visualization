# -*- coding: utf-8 -*-
"""실습과제2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_Q6lkAVBb6JE-_-4Oy4TWqfJYoVr3CML
"""

# Commented out IPython magic to ensure Python compatibility.
# 실기 과제 2 준비 작업 1
# konlpy 라이브러리 설치
!pip install konlpy

# Matplotlib 한글 폰트 설정
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm

# %config InlineBackend.figure_format = 'retina'

!apt-get -qq -y install fonts-nanum > /dev/null

fontpath = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'
font = fm.FontProperties(fname=fontpath, size=9)
plt.rc('font', family='NanumBarunGothic') 
mpl.font_manager._rebuild()

# 파이썬프로그래밍활용 1급 실기과제-2 #

from bs4 import BeautifulSoup
import requests
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd


# 키워드 검색 뉴스 가사 타이틀 가져오기 
def get_news_titles(start_num, end_num):  
    
    while True :
        if start_num > end_num:
            break
 
        url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={}&start={}'.format(search_word, start_num)
        
        response = requests.get(url) 
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
                   
        # 뉴스 타이틀 가져오기
        titles =  soup.select('ul.type01 > li > dl > dt > a')
        
        # 뉴스 타이틀을 list에 저장
        for title in titles:
            title_list.append(title['title'])
            
        start_num += 10  # 읽어올 기사 수 조정 

    # 수집한 기사 타이틀 출력
    for no, title in enumerate(title_list, start=1) :
      print(no, title) 
    print("-"* 120)

# 워드 클라우드 그리기
def make_wordcloud(wordcount):
    
    okt = Okt() 
    sentences_tag = []
    
    # 형태소로 분석하여 리스트에 넣기
    for sentence in title_list:
        morph = okt.pos(sentence)
        sentences_tag.append(morph)
 
    noun_adj_list = []
    # 형태소 중 명사와 형용사만 리스트에 넣기
    for sentence in sentences_tag:
        for word, tag in sentence:
            if tag in ['Noun', 'Adjective']:
                noun_adj_list.append(word)
 
    # 단어 빈도수 세기
    count = Counter(noun_adj_list)
  
    # 빈도수가 높은 단어 50개 추출, 글자 길이가 2이상인 단어만 추출
    wordInfo = dict()
    for tags, counts in count.most_common(wordcount):
        if len(wordInfo) >= 50 :   # 빈도수가 높은 단어 50개 추출
            break
        if (len(str(tags)) > 1):  # 글자 길이가 2이상인 단어만 추출
            wordInfo[tags] = counts
            print ("%s : %d" % (tags, counts))
  
    # wordcloud 객체 생성(한글깨지는 문제 해결하기위해 font_path 지정)
    font_path = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'
    wc = WordCloud(font_path = font_path,
                          background_color='white', width=600, height=480)
    # wordcloud 객체에 데이터 매핑
    wc.generate_from_frequencies(wordInfo)

    # wordcloud 그리기
    plt.figure(figsize=(10, 6))
    plt.axis('off')
    plt.imshow(wc)
    plt.show()
    
    # 워드 클라우드 그림 파일로 저장하기    
    wc.to_file('2007-00326-박건열-3.png')   # 수험번호와 이름을 입력해주세요.

# 메인 프로그램     
if __name__ == '__main__':
    
    search_word = '신종 코로나'                # 키워드 검색
    title_list = []

    # 뉴스 기사 타이틀 크롤링(시작 ~ 끝)
    get_news_titles(1, 50)
 
    # 워드클라우드 그리기
    make_wordcloud(100)

