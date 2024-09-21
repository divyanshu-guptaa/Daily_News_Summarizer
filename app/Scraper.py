import re
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrape_news():
    service = Service('chromedriver-win64\chromedriver.exe')
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=service,options=options)

    news_websites = 'https://www.bbc.com/news'

    driver.get(url=news_websites)
    driver.implicitly_wait(10) 

    news_links = driver.find_elements(By.XPATH, "//a[@data-testid = 'internal-link']")
    pattern1 = "news/articles"
    pattern2 = "videos"

    urls = []
    for news_link in news_links:
        urls.append(news_link.get_attribute('href'))
        
    i=0
    articles = []
    processed_urls = []
    for url in urls:
        if (re.search(pattern1,url) and not re.search(pattern2,url)) and i<5 and url not in processed_urls:
            article = {}
            article['url'] = url
            
            driver.get(url=url)
            driver.implicitly_wait(20)
            
            headline = driver.find_element(By.XPATH,'//div[@data-component = "headline-block"]')
            headline_text = headline.text
            article['headline'] = headline_text
            
            div_elements = driver.find_elements(By.XPATH,'//div[@data-component = "text-block"]')
            news = ""
            for div_element in div_elements:
                news += div_element.text + " "
            article['news'] = news
            i+=1
            articles.append(article)
            
            processed_urls.append(url)
    return articles

    time.sleep(10)
    driver.quit()
