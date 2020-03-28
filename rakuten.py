import requests
from bs4 import BeautifulSoup

keyword = input("라쿠텐에서 검색할 상품을 입력해 주세요 (japanese, english only):").replace(" ","+")
URL = f"https://search.rakuten.co.jp/search/mall/{keyword}"
print(URL)

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div",{"class":"dui-pagination"})
    links = pagination.find_all("a")
    pages =[]
    for link in links[:-2]:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page

def extract_goods(html):
    title = html.find("div", class_="content title").find("a")["title"]
    price = html.find("div", class_="content description price").find("span", class_="important").text
    link = html.find("div", class_="content title").find("a")["href"]

    return {"title":title, "pricd":price, "link":link}

def extract_good(last_page):
    goods = []
    for page in range(last_page):
        print(f"Scrapping goods in rakuten: {page}")
        result = requests.get(f"{URL}/?p={page}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", class_="dui-card searchresultitem")
        for result in results:
            good = extract_goods(result)
            goods.append(good)
    return goods

def get_goods_info():
    last_page = get_last_page()
    goods = extract_good(last_page)
    return goods

