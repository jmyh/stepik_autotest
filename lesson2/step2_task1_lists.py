from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link="http://suninjuly.github.io/selects1.html"
link2="http://suninjuly.github.io/selects2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link2)

    x=browser.find_element_by_id("num1").text
    y=browser.find_element_by_id("num2").text
    z=int(x)+int(y)

    select=Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(z))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла