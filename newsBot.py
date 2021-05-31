from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, sys, datetime

def fetchHeadlines(driver):
    for i in range(2):
        html = driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        time.sleep(2)
    news = []
    for i in range(3, 30):
        try:
            xpath = "/html/body/c-wiz/div/div[2]/div[2]/div/main/c-wiz/div[1]/div["+str(i)+"]/div/div/article/h3/a"
            text = driver.find_element(By.XPATH, xpath).text
            news.append(text)
        except Exception as e:
            i+=1
    if news == []:
        return "No results to show"
    return news 

def searchNews(driver, searchQuery):
    news = []
    searchBar = driver.find_element_by_xpath("/html/body/div[4]/header/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]")
    searchBar.send_keys(searchQuery)
    searchBar.send_keys(Keys.ENTER)
    time.sleep(1)
    for i in range(2):
        html = driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        time.sleep(2)
    heading = "Search Results for '", searchQuery, "'..."
    news.append(heading)
    for i in range(1, 30):
        try:
            xpath = "/html/body/c-wiz[2]/div/div[2]/div[2]/div/main/c-wiz/div[1]/div["+str(i)+"]/div/article/h3/a"
            text = driver.find_element(By.XPATH, xpath).text
            news.append(text)
        except Exception as e:
            i+=1
    if news==[]:
        return "No results to show" 
    return news 

def display(news):
    f = open("newsdump.txt", "w")
    now = datetime.datetime.now()
    today = now.strftime("%d,%B,%Y")
    f.writelines(today)
    f.writelines("\n")
    temp = driver.find_element_by_xpath("/html/body/c-wiz/div/div[2]/div[2]/div/aside/c-wiz/div/div[1]/div/div[2]/div[1]/div[1]/span").text 
    f.writelines(temp)
    f.writelines("\n\n")
    if news == "No results to show":
        return news 
    for i in news:
        f.writelines(i)
        f.writelines("\n\n")
    f.close()

try:
    searchQuery = sys.argv[1]
except Exception as e:
    searchQuery = ""

driver = webdriver.Firefox()
path = "https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en"
driver.get(path)
time.sleep(1)

if searchQuery=="":
    news = fetchHeadlines(driver)
else:
    news = searchNews(driver, searchQuery)
display(news)

driver.quit()