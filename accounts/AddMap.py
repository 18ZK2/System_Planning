from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
class CheckinMaps(object):
    #
    def __init__(self,):
        
        self.url = 'https://labs.d-s-b.jp/ImagemapGenerator/'
        self.cssSelector = 'body > div > div.row.playground > div.col-sm-4.code.ex-code-prettify-hide-demo > div.ex-code-prettify-contents > pre > ol'

    def Session(self,):
        session = HTMLSession()
        render = session.get(self.url)
    def Analyze(self,):
        #セッション開始
        
        print(res)
        response=requests.get(self.url)
        print(response.status_code)
        if(response.status_code==requests.codes.ok):
            soup = BeautifulSoup(response.text,'html.parser')
            elems = soup.select(selector=self.cssSelector)
            print(len(soup))



'''

ステータスコード	範囲	説明
response.status_code
100番台	100-199	Informational：リクエストは受け取られ、処理が継続。
200番台	200-299	Success：リクエストに成功。
300番台	300-399	Redirection ：リダイレクトや移行など、リクエストの完了には追加的な処理が必要。
400番台	400-499	Client Error：クライアントからのリクエストに誤りあり。
500番台	500-599	Server Error ：サーバ側でリクエストの処理に失敗。

'''