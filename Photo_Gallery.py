import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import requests

# Set the path for the ChromeDriver executable
chrome_driver_path = r"C:\Users\shiva\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(chrome_driver_path)

# Create a directory to save the downloaded photos
download_directory = r"C:\Users\shiva\Downloads\PhotoGallery"
os.makedirs(download_directory, exist_ok=True)

# Set Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_directory,
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": True
})

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Open the website and maximize the window
driver.get("https://labour.gov.in/")
driver.maximize_window()
time.sleep(2)

# Navigate through the menu to the photo gallery
media_menu = driver.find_element(By.LINK_TEXT, "Media")
actions = ActionChains(driver)
actions.move_to_element(media_menu).perform()
time.sleep(2)

photo_gallery = driver.find_element(By.XPATH, '//*[@id="nav"]/li[10]/ul/li[2]/a')
photo_gallery.click()
time.sleep(2)

# Find the photos on the gallery page
photos = driver.find_elements(By.TAG_NAME, "img")
photos = photos[:10]  # Get the first 10 photos

# Download each photo
for index, photo in enumerate(photos):
    photo_url = photo.get_attribute("src")
    photo_data = requests.get(photo_url).content
    with open(os.path.join(download_directory, f"photo_{index + 1}.jpg"), "wb") as photo_file:
        photo_file.write(photo_data)


driver.quit()
