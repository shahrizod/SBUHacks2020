from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

options = webdriver.ChromeOptions()
#options.add_argument('headless')
driver = webdriver.Chrome(options=options)
url = "https://quizlet.com/130934620/print"
driver.get(url)
WebDriverWait(driver, 10).until(lambda x: x.find_element_by_class_name('PrintPageOptions-radioWrap'))
driver.find_element_by_xpath('/html/body/div[3]/main/div/div/div/div[3]/div[1]/div/div[2]/div[2]/div[4]/label/input').click()
WebDriverWait(driver, 10).until(lambda x: x.find_element_by_class_name('PrintPageOptions-radioWrap'))
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()
firstCol = soup.find_all(class_='term inner')
secondCol = soup.find_all(class_ = 'def inner')

terms = []
definitions = []

for term in firstCol:
    terms.append(term.text.split(".",1)[1])
for definition in secondCol:
    definitions.append(definition.text)

data = {'Terms':terms,'Definitions':definitions}
df = pd.DataFrame(data, columns=['Terms', 'Definitions'])
print(df)