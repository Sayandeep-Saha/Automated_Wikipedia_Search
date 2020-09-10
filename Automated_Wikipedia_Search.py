from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

n = str(input("Enter the item you want to search: "))

driver = webdriver.Chrome()
driver.get('https://www.wikipedia.org')

searchbox = driver.find_element_by_xpath('//*[@id="searchInput"]')
searchbox.send_keys(n)

searchbutton = driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button/i')
searchbutton.click()

try:
    bodyContent = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "bodyContent"))
    )

    with open('My_Data.txt', 'w') as f:
        print('Filename:',bodyContent.text , file=f)
       
finally:
    driver.quit()
    print('Successfully Data Is Saved')
