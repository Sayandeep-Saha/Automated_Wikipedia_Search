from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

n = str(input("Enter the item you want to search: "))   #taking the input from the user


driver = webdriver.Chrome()                             # opening Chrome
driver.get('https://www.wikipedia.org')


searchbox = driver.find_element_by_xpath('//*[@id="searchInput"]')  #finding the searchbox using xpath
searchbox.send_keys(n)                                              


searchbutton = driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button/i')
searchbutton.click()


try:                                                   # Explicit Waits / refer: https://selenium-python.readthedocs.io/waits.html
    bodyContent = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "bodyContent"))
    )

    with open('My_Data.txt', 'w') as f:                 # Creating a text file and 
        print(n, bodyContent.text , file=f)             # Saving the search result in a created file
        # refer: https://stackoverflow.com/a/7152903     



finally:
    driver.quit()
    print('Successfully Data Is Saved')