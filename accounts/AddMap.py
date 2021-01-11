from .dbManage import AddMap,RatestMapNum
from re import findall
class CheckinMaps(object):
    #
    def __init__(self,):
        #edge を環境に合わせないと
        self.edge = r'C:\Users\BOUfU\Documents\System_Planing\System_Planning\edgedriver_win64\msedgedriver.exe'
        self.url = 'https://labs.d-s-b.jp/ImagemapGenerator/'
        self.cssSelector = 'body > div > div.row.playground > div.col-sm-4.code.ex-code-prettify-hide-demo > div.ex-code-prettify-contents > pre > ol'
    #文字列分け
    def SplitTexts(self,texts):

        slicedText = texts.split('\r\n')
        return slicedText[1:-1]
    #番号付け
    def NumberingImagemapShapes(self,texts):

        # <area shape="rect" coords="202,328,534,636" href="#" alt="" />
        start = RatestMapNum()
        if(start[0][0]==None):

            start=0
        else:
            
            start = start[0][0]
        print(start,len(texts))
        result=[]
        for i in range(len(texts)):
            num = i+start
            text = texts[i]
            #番号付け
            text = text.replace('alt=""','alt='+str(num))
            #分追加
            text = text.replace('/>','onclick="getname(this.alt)"/>')
            result.append(text)
            #切り分けた形を抽出
            #切り分けたマップを抽出
            shape = findall(r'shape="(.+)" coords=',text)[0]
            coords = findall(r'coords="(.+)" href=',text)[0]
            #DBに登録　とりあえず名前は'test{num}'
            AddMap('test'+str(num),shape,coords)
        
        return result
    #html組み立te
    def MakeMapHTML(self,numberdMapdata):

        pass