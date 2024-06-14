# Question 1
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

# Set the path for the ChromeDriver executable
paths = r"C:\Users\Ranga\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)

# Set Chrome options to keep the browser open after the script completes
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Wait for 2 seconds to ensure the driver is properly initialized
time.sleep(2)

# Open the CoWIN website
driver.get("https://www.cowin.gov.in/")
driver.maximize_window()

# Wait for 2 seconds to ensure the page is fully loaded
time.sleep(2)

# Find and click the FAQ link by its link text
FAQ_Link = driver.find_element(By.LINK_TEXT, 'FAQ')
FAQ_Link.click()

# Wait for 2 seconds to ensure the FAQ page is fully loaded
time.sleep(2)

# Find and click the Partners link by its XPath
Partners_Link = driver.find_element(By.XPATH, "/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a")
Partners_Link.click()

# Wait for 2 seconds to ensure the Partners page is fully loaded
time.sleep(2)

# Get the window handles of all open browser windows
Window_Handles = driver.window_handles

# Assign the window handles to variables for better readability
Main_window = Window_Handles[0]
Faq_Window = Window_Handles[1]
Partners_Window = Window_Handles[2]

# Print the window IDs (Note: The second and third print statements should be corrected to print the correct variables)
print("Main_Window ID:", Main_window)
print("FAQ_Window ID:", Faq_Window)
print("Partners_Window ID:", Partners_Window)

# Wait for 4 seconds
time.sleep(4)

# Switch to the Partners window and close it
driver.switch_to.window(Partners_Window)
driver.close()

# Wait for 2 seconds to ensure the Partners window is closed
time.sleep(2)

# Switch to the FAQ window and close it
driver.switch_to.window(Faq_Window)
driver.close()

# Wait for 2 seconds to ensure the FAQ window is closed
time.sleep(2)

# Switch back to the main window
driver.switch_to.window(Main_window)

# Print the title of the current page
print("Current Page Title:", driver.title)








