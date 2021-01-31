from selenium import webdriver
import time
import math

link="http://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element=browser.find_element_by_id("input_value")
    x=x_element.text
    y=calc(x)

    answer_element=browser.find_element_by_id("answer")
    answer_element.send_keys(y)

    checkbox=browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radiobutton=browser.find_element_by_id("robotsRule")
    radiobutton.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла