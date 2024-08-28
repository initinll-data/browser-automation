from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

# driver.get("https://www.python.org")
# print(driver.title)

url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url)

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)


driver.close()
