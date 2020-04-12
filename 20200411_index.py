from selenium import webdriver
from bs4 import BeautifulSoup
import schedule
import time

#크롬을 안뜨게 하고 싶으면 아래 옵션 적용
'''options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
driver = webdriver.Chrome('chromedriver',options=options)'''

def get_my_stock():

    driver = webdriver.Chrome('chromedriver')
    #삼성전자,SK하이닉스,셀트리온,카카오
    codes = ['005930','000660','035720','068270']

    for code in codes:

        url = 'https://m.stock.naver.com/item/main.nhn#/stocks/'+code+'/total'
        driver.get(url)
        time.sleep(2)

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        name = soup.select_one('#header > div.end_header_topinfo > div.flick-container.major_info_wrp > div > div:nth-child(2) > div > div.item_wrp > div > h2').text
        current_price = soup.select_one('#header > div.end_header_topinfo > div.flick-container.major_info_wrp > div > div:nth-child(2) > div > div.stock_wrp > div.price_wrp > strong').text
        rate = soup.select_one('#header > div.end_header_topinfo > div.flick-container.major_info_wrp > div > div:nth-child(2) > div > div.stock_wrp > div.price_wrp > div > span.gap_rate > span.rate').text

        print(name,current_price,rate)
    print('----------')
    driver.quit()

def job():
    get_my_stock()

def run():
    schedule.every(15).seconds.do(job)  # 15초에 한번씩 job()을 실행
    while True:
        schedule.run_pending()

if __name__ == "__main__": #이 파일을 직접 실행했을 때 run()을 돌린다. (module을 통해 다른 파일에 import될 때는 이게 성립이 안되어서 run실행안됨)
    run()