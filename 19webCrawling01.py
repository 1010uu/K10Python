import requests
from bs4 import BeautifulSoup

#크롤링할 웹사이트 URL 및 접속
url = 'https://kin.naver.com/search/list.naver?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
respons=requests.get(url)

if respons.status_code==200: #응답코드가 200일때
    html=respons.text #html코드를 받아온다.
    soup=BeautifulSoup(html, 'html.parser') #파싱하기위해 soup객체로 변환
    
    #셀렉터로 추출(크롬)
    title1_1 = soup.select_one('#s_content > div.section > ul > li:nth-child(1) > dl > dt')
    #print("추출1_1:", title1_1)
    
    #텍스트만 추출
    text=title1_1.get_text()
    #print("추출2:", text)
    
    #ul class="basic1" 태그 하위요소 가져오기
    ul=soup.select_one('ul.basic1')
    #print("추출3:", ul)
    
    #print("추출4")
    titles2=ul.select('li>dl>dt>a')
    for tit in titles2:
        print(tit.get_text())
else:
    print(respons.status_code)