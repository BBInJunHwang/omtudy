from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://amostv.co.kr/amostv/MAN/MAN0100.mw")  


bsObject = BeautifulSoup(html, "html.parser") 

#print(bsObject) # 웹 문서 전체가 출력됩니다. 

# print(bsObject.title) # 타이틀만 가져오기

for meta in bsObject.head.find_all('meta'):
   print(meta.get('content')) # 메타 데이터만 찾아서 content 속성만 가져온다.


