import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set the path for the ChromeDriver executable
chrome_driver_path = r"C:\Users\shiva\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(chrome_driver_path)

# Set Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": r"C:\Users\shiva\Downloads",
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": True
})

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Open the website and maximize the window
driver.get("https://labour.gov.in/")
driver.maximize_window()
time.sleep(2)

# Navigate through the menu to the monthly report
doc_menu = driver.find_element(By.LINK_TEXT, "Documents")
actions = ActionChains(driver)
actions.move_to_element(doc_menu).perform()
time.sleep(3)

monthly_report = driver.find_element(By.XPATH, '//*[@id="nav"]/li[7]/ul/li[2]/a')
monthly_report.click()
time.sleep(2)

# Click the link to download the April monthly report
april_month_download = driver.find_element(By.XPATH, '//*[@id="fontSize"]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/a')
april_month_download.click()
time.sleep(2)

# Handle any alert that appears
try:
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(2)
except:
    pass  # No alert, continue

# Switch to the new window if opened
window_handles = driver.window_handles
if len(window_handles) > 1:
    driver.switch_to.window(window_handles[1])