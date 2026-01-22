#yahooニュースのヘッドラインを抽出
from urllib import request
from bs4 import BeautifulSoup

url = "https://news.yahoo.co.jp/categories/it"

#指定URLの表示内容をざっくり取得
response = request.urlopen(url)
soup = BeautifulSoup(response, "html.parser")
response.close()
#print(soup)

#ヘッドラインを抽出
news_text = soup.find("div", "sc-1d6xg0e-3")

#タグを削除して表示　※全部一行で表示されてしまう><
#news_text = news_text.get_text()

#aタグごとにヘッドラインを取り出すようにする
for element in news_text.find_all("a"):
    if element in news_text.find_all("a"):
        print("")
    else:
        print(element.text)