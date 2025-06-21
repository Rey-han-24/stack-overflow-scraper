from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys 
import time
import pandas as pd
#Credit Rey-han-24
chrome_driver = r"C:\Users\hp\Documents\chromedriver\chromedriver-win64\chromedriver.exe"
service = Service(chrome_driver)
driver = webdriver.Chrome(service=service)
driver.get('https://www.stackoverflow.com')

search_element = driver.find_element(By.NAME, 'q')
search_element.click()
search_element.send_keys('Switch for python ')
search_element.send_keys(Keys.ENTER)

wait = WebDriverWait(driver, 30)
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'answer-hyperlink')))
#Credit Rey-han-24
urls = set()
page_count = 0
while True:
    page_count += 1
    print(f"Scraping page {page_count}...")
    elements = driver.find_elements(By.CLASS_NAME, 'answer-hyperlink')
    for element in elements:
        urls.add(element.get_attribute('href'))
    print(f"Found {len(elements)} unique links on page {page_count}")
    try:
        next_element = driver.find_element(By.LINK_TEXT, 'Next')
        next_element.click()
    except:
        print("No more pages....")
        break

urls_list = list(urls)

for i, url in enumerate(urls_list):
    print(f"Link #{i+1}: {url}")
print("Result displayed. Exiting the automation.")
driver.quit()

excel_file_save_path = r"E:\Programming data\Projects\Datascraping.xlsx"
df = pd.DataFrame(urls_list, columns=["Links STACKOVERFLOW"]) # type: ignore
df.to_excel(excel_file_save_path, index=False)
print(f"File saved at {excel_file_save_path}")
#Credit Rey-han-24
print(f"=== SCRAPING SUMMARY ===")
print(f"Total pages scraped: {page_count}")
print(f"Total links collected: {len(urls_list)}")
print(f"Unique links: {len(set(urls_list))}")


