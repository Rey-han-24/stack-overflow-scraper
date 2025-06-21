# 🔍 Stack Overflow Data Scraper using Python + Selenium + Panda (for Excel sheet)

This project is a simple but powerful Python automation tool that scrapes question links from **Stack Overflow** based on a search query and saves them into an Excel spreadsheet.
It uses Selenium to automate browser actions such as searching, navigating through pages, and collecting data.
You can also scrape data off multiple sites but the program will require some simple changes for that.
---

## 📌 Features

- Automates a Stack Overflow search for any keyword of your choice.
- Navigates through **all pages** of results.
- Collects **unique question links**.
- Exports the links to an **Excel file** using `pandas`.
- Displays scraping summary in the terminal.

---

## ⚙️ Technologies Used

- Python 🐍
- Selenium WebDriver
- Pandas
- ChromeDriver

---

## 🚀 How to Run the Project

### 1. 📦 Install Dependencies

Make sure you have Python installed. Then install required libraries:

```bash
pip install selenium pandas openpyxl


2. 🔧 Setup ChromeDriver
Download ChromeDriver matching your browser version from:
➡️ https://chromedriver.chromium.org/downloads

Set the path in your script:
chrome_driver = r"path\to\chromedriver.exe"

3. 🏁 Run the Script
Run your Python script from the terminal
python scraper.py

The output Excel file will be saved to:

E:\Programming data\Projects\Datascraping.xlsx (Add your on destination)



🧠 Notes for Beginners
This script simulates a real browser. Don’t run it too fast or too often to avoid being blocked.

You can change the search keyword by modifying this line
search_element.send_keys('Switch for python ')

The project uses By.CLASS_NAME = 'answer-hyperlink' but sometimes Stack Overflow updates class names. If links aren’t scraping, use a more robust selector like
driver.find_elements(By.CSS_SELECTOR, '.s-post-summary h3 a')
Always close the browser using driver.quit() to release memory

👤 Author
Rey-han-24
GitHub: @Rey-han-24



