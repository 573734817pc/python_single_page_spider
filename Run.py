from spiderLib import Main
url = 'http://finance.ce.cn/stock/gsgdbd/201904/17/t20190417_31876313.shtml'
get_rule = '<h1 id="articleTitle">(.*?)</h1>.*?<div class="content" id="articleText">.*?><p>(.*?)</p>'
obj = Main.Main(url,get_rule)
res = obj.main()
print(res)
