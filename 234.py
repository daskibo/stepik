#color find_element_by_css_selector
import time
from selenium import webdriver


link = "http://suninjuly.github.io/alert_accept.html"
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #podtverdim alert
    time.sleep(2)
    btn= browser.find_element_by_css_selector("button.btn")
    btn.click()
    time.sleep(2)
    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(2)

    x_element = browser.find_element_by_css_selector("span#input_value")

    x = x_element.text
    y = calc(x)
    #vstavim otvet v pole
    answer = browser.find_element_by_css_selector("input#answer")
    answer.send_keys(y)
    #checkbox = browser.find_element_by_css_selector("input#robotCheckbox").click()
    #radio = browser.find_element_by_css_selector("input#robotsRule").click()
    button = browser.find_element_by_css_selector("button").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
