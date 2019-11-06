import requests
from lxml import etree


with open("C:\\Users\\Lab\\Desktop\\data.txt", "a", encoding='utf-8') as f:
    for i in range(3):
        i =  i + 1
    # i = 999
    # if(i == 999):
        url = "https://www.luoow.com/{}/".format(i)
        # url = "C:/Users/Lab/Desktop/vol.999.html"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"}
        data = requests.get(url, headers=headers).text
        s = etree.HTML(data)
        music_title = s.xpath('/html/body/div[@class="container"]/div[@class="title"]/text()')
        music_img = s.xpath('/html/body/div[@class="container"]/div[@class="cover_img"]/img/@src')
        music_tag = s.xpath('/html/body/div[@class="container"]/div[@class="tag"]/a/text()')
        music_decs = s.xpath('/html/body/div[@class="container"]/div[@class="desc"]/div[@class="vol-desc"]/text()')
        # music_player = s.xpath('/html/body/div[@class="container"]/div[6]/ul[@class="skPlayer-list"]/li[1]/span[2]/text()')
        music_player = s.xpath('/html/body/div[3]/div[6]/ul')
    # // *[ @ id = "skPlayer"] / ul
        # music_player = s.xpath('/html/body/div[3]/div[6]/ul/li[2]/span[2]')
        # / html / body / script[4] / text()
        # html
        # body
        # div.container
        # div  # skPlayer.skPlayer-list-on ul.skPlayer-list li span.skPlayer-list-name
        for j1 in music_title:
            f.write("标题：{}\n".format(j1))

        for j2 in music_img:
            f.write("图片：{}\n".format(j2))

        for j3 in music_tag:
            f.write("标签：{}\n".format(j3).replace("&nbsp", " "))

        for j4 in music_decs:
            f.write("{}".format(j4))

        for j5 in music_player:
            print(music_player,"\n")
            f.write("{}".format(j5))
            f.write("\n")

