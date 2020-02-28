#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

class Corona(object):

    @staticmethod
    def corona(ctx, args=()):
        speech = '{0.author.mention} \n' + Corona.corona_kr() + '\n'+Corona.corona_daejeon()
        return speech.format(ctx)
    
    # 전국환자
    @staticmethod
    def corona_kr():
        res = requests.get('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun=')
        soup = BeautifulSoup(res.text, 'html.parser')
        sickpeople = soup.select('#content > div > div.bv_content > div > div:nth-child(3) > table > tbody > tr:nth-child(1) > td')
        return "전체 확진자 : "+str(sickpeople[0].contents[0])
    
    # 대전광역시 환자
    @staticmethod
    def corona_daejeon():
        res = requests.get('https://www.daejeon.go.kr/corona19/index.do')
        soup = BeautifulSoup(res.text, 'html.parser')
        sickpeople = soup.select('#contBox > div:nth-child(2) > div > ul > li.tab-1 > div.txt > strong')
        return "대전광역시 확진자 : "+str(sickpeople[0].contents[0])+" 명"