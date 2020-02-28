#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

res = requests.get('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun=')
soup = BeautifulSoup(res.text, 'html.parser')
table = soup.select('#content > div > div.bv_content > div > div:nth-child(3) > table > tbody > tr:nth-child(1) > td')
print(table)

