from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("span#input_value")
    x = x_element.text
    y = calc(x)
    #vstavim otvet v pole
    answer = browser.find_element_by_css_selector("input#answer")
    answer.send_keys(y)
    checkbox = browser.find_element_by_css_selector("input#robotCheckbox").click()
    radio = browser.find_element_by_css_selector("input#robotsRule").click()
    button = browser.find_element_by_css_selector("button").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
