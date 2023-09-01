from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
browser.find_element(By.ID, "book").click()

def calc(x):
        return str(math.log(abs(12 * math.sin(x))))

# Find and store the value of x
x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text

# Calculate the result y
y = calc(int(x))

# Fill in the answer
input_element = browser.find_element(By.ID, "answer")
input_element.send_keys(y)

# Submit the form
buttn = browser.find_element(By.ID, "solve")
buttn.click()
