import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
url = 'https://www.olx.co.id/mobil-bekas_c198'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
while True:
    try:
        driver.find_element(By.CSS_SELECTOR, "div._38O09 > button").click()
        time.sleep(2)
    except NoSuchElementException:
        print("Tombol tidak ditemukan, berhenti mengklik")
        break
cars=[]
soup = BeautifulSoup(driver.page_source,"html.parser")
for item in soup.findAll('li',class_='_3V_Ww'):
    brand = item.find('div',class_='_2Gr10').text
    price = item.find('span',class_='_1zgtX')
    year = item.find('div', class_='_21gnE')
    place = item.find('div', class_='_3VRSm')
    cars.append(
        (brand,price,year,place)
    )
df = pd.DataFrame(cars, columns = ['Brand', 'Price', 'Year', 'Place'])
print(df)
df.to_csv('scrapingdata.csv',index=False)
