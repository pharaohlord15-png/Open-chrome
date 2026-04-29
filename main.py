from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

GRID_URL = os.getenv("GRID_URL")

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1280,720")

driver = webdriver.Remote(
    command_executor=GRID_URL,
    options=options
)

driver.get("https://google.com")

print("Bot running 24/7...")

while True:
    time.sleep(60)
