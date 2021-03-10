#color find_element_by_css_selector
import time
from selenium import webdriver


link = "http://suninjuly.github.io/redirect_accept.html"
import math
browser = webdriver.Chrome()
browser.implicitly_wait(5)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser.get(link)
    #podtverdim alert

    btn= browser.find_element_by_css_selector("button")
    btn.click()

    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)
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
