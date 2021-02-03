from .dbManage import AddMap,RatestMapNum
from re import findall
import sys

class CheckinMaps(object):
    #
    def __init__(self,):
        self.url = 'https://labs.d-s-b.jp/ImagemapGenerator/'
        self.cssSelector = 'body > div > div.row.playground > div.col-sm-4.code.ex-code-prettify-hide-demo > div.ex-code-prettify-contents > pre > ol'
    #文字列分け
    def SplitTexts(self,texts):

        slicedText = texts.split('\r\n')
        if(slicedText[0]=='<map name="ImageMap">' and slicedText[-1] == '</map>'):

            return slicedText[1:-1]
        else:
            
            return -1
    #番号付け
    def NumberingImagemapShapes(self,texts):

        # <area shape="rect" coords="202,328,534,636" href="#" alt="" />
        start = RatestMapNum()
        result=[]
        length = len(texts)
        for i in range(length):
            num = i+start
            text = texts[i]
            #番号付け
            text = text.replace('alt=""','alt='+str(num))
            #分追加
            text = text.replace('/>','onclick="getname(this.alt)"/>')
            #切り分けた形を抽出
            #切り分けたマップを抽出
            shape = findall(r'shape="(.+)" coords=',text)[0]
            coords = findall(r'coords="(.+)" href=',text)[0]
            #DBに登録　とりあえず名前は'test{num}'
            r = {'shape':shape,'coords':coords,}
            result.append(r)
        return result


#html組み立te
class BuildHTML(object):

    def __init__(self):
        pass

    def MakeMap(self,mapDatas):

        areas = []
        for m in mapDatas:
            a = '<area shape="'+m[2]+'"'+'coords="'+m[3]+'" nohref alt ='+str(m[0])+' onclick="'+'getname(this.alt)"/>'
            areas.append(a)
        return areas

    def Build(self,imgURL,areas):

        head = '<head><meta charset="utf-8" /><title></title></head>'
        cssLoad = '<link href="/static/test.css" rel="stylesheet">'
        homeLink = ' <a href="{% url '+'index2'+' %}">戻る</a><br> '
        inputForm ='<tr><td align="right"><b> 入力した場所：</b></td><td><input type="text" name="get_room_name" size="30" maxlength="10" value="0" required> <input type="submit" name="statebuttom"></td></tr>'
        img = '<img src="'+imgURL+'" usemap="#ImageMap" alt="" />'
        maps='<map name="ImageMap">'
        for area in areas:

            maps=maps+area
        script = '<script>function getname(alt){document.room.get_room_name.value =alt;}</script>'
        maps=maps+script
        maps=maps+'</map>'

        forms = '<form name="room" id="room" method="POST">'+inputForm+img+maps+'</form>'
        result = '<html>'+head+'<body>'+forms+'<body>'+'<html>'
        return result

    def Build_test(self,imgURL,areas):
        '''
        {% csrf_token %}
        '''
        img = '<img src="'+imgURL+'" alt="" >'
        temp ='<!DOCTYPE><html><head><title>title</title>'+img+'</head><html>'

        return temp
        



